// Global Application State
const STATE = {
  currentMode: 'learn', // 'learn', 'locate', 'choice', 'cram', 'cheatsheet'
  currentFilter: 'all', // 'all', 'regions', 'rivers', 'wisla', 'odra', 'mistakes'
  sessionType: '86',    // '86' (default: 2x every place) or 'infinite'
  mapView: 'svg',       // 'svg', 'leaflet'
  currentItem: null,
  selectedItem: null,   // Selected object awaiting Space to confirm
  quizOptions: [],
  answeredCurrent: false,
  soundEnabled: true,
  labelsEnabled: false,
  sessionQueue: [],     // deck of questions (each item appears 2x)
  sessionIndex: 0,      // question index (0 to sessionTotal - 1)
  sessionTotal: 86,     // total questions in current session
  sessionScore: 0,      // correct answers in this session
  sessionMistakes: {},  // map of item id -> mistake count in this session
  stats: {
    mastered: [],
    mistakes: {}, // id -> count
    streak: 0,
    bestStreak: 0,
    totalAnswered: 0,
    totalCorrect: 0
  }
};

// Audio Synthesizer (Web Audio API - 100% offline)
class SoundFX {
  constructor() {
    this.ctx = null;
  }
  init() {
    if (!this.ctx && (window.AudioContext || window.webkitAudioContext)) {
      this.ctx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }
  playCorrect() {
    if (!STATE.soundEnabled) return;
    this.init();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    
    const osc1 = this.ctx.createOscillator();
    const osc2 = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    
    osc1.type = 'sine';
    osc2.type = 'sine';
    osc1.frequency.setValueAtTime(523.25, now); // C5
    osc1.frequency.setValueAtTime(659.25, now + 0.1); // E5
    osc2.frequency.setValueAtTime(783.99, now + 0.1); // G5
    
    gain.gain.setValueAtTime(0.15, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.5);
    
    osc1.connect(gain);
    osc2.connect(gain);
    gain.connect(this.ctx.destination);
    
    osc1.start(now);
    osc2.start(now + 0.1);
    osc1.stop(now + 0.5);
    osc2.stop(now + 0.5);
  }
  playWrong() {
    if (!STATE.soundEnabled) return;
    this.init();
    if (!this.ctx) return;
    const now = this.ctx.currentTime;
    
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();
    
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(220, now); // A3
    osc.frequency.exponentialRampToValueAtTime(140, now + 0.35);
    
    gain.gain.setValueAtTime(0.2, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
    
    osc.connect(gain);
    gain.connect(this.ctx.destination);
    
    osc.start(now);
    osc.stop(now + 0.35);
  }
  playStreak() {
    if (!STATE.soundEnabled) return;
    this.init();
    if (!this.ctx) return;
    const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
    notes.forEach((freq, idx) => {
      const now = this.ctx.currentTime + idx * 0.08;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(freq, now);
      gain.gain.setValueAtTime(0.15, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(now);
      osc.stop(now + 0.3);
    });
  }
}
const sfx = new SoundFX();

// SVG Zoom & Pan Controller
class SvgPanZoom {
  constructor(svgEl, containerEl) {
    this.svg = svgEl;
    this.container = containerEl;
    this.viewBox = { x: 0, y: 0, w: 850, h: 780 };
    this.defaultViewBox = { x: 0, y: 0, w: 850, h: 780 };
    this.isPanning = false;
    this.startPoint = { x: 0, y: 0 };
    this.init();
  }
  init() {
    this.applyViewBox();
    
    this.svg.addEventListener('mousedown', (e) => {
      if (e.target.closest('.map-controls-floating') || e.button !== 0) return;
      this.isPanning = true;
      this.startPoint = { x: e.clientX, y: e.clientY };
      this.svg.style.cursor = 'grabbing';
    });
    
    window.addEventListener('mousemove', (e) => {
      if (!this.isPanning) return;
      const dx = (e.clientX - this.startPoint.x) * (this.viewBox.w / this.svg.clientWidth);
      const dy = (e.clientY - this.startPoint.y) * (this.viewBox.h / this.svg.clientHeight);
      this.viewBox.x -= dx;
      this.viewBox.y -= dy;
      this.startPoint = { x: e.clientX, y: e.clientY };
      this.applyViewBox();
    });
    
    window.addEventListener('mouseup', () => {
      if (this.isPanning) {
        this.isPanning = false;
        this.svg.style.cursor = 'default';
      }
    });
    
    this.svg.addEventListener('wheel', (e) => {
      e.preventDefault();
      const zoomFactor = e.deltaY < 0 ? 0.85 : 1.15;
      this.zoomAtPoint(e.clientX, e.clientY, zoomFactor);
    }, { passive: false });
  }
  zoom(factor) {
    const cx = this.viewBox.x + this.viewBox.w / 2;
    const cy = this.viewBox.y + this.viewBox.h / 2;
    const newW = this.viewBox.w * factor;
    const newH = this.viewBox.h * factor;
    if (newW > 1200 || newW < 180) return;
    this.viewBox.x = cx - newW / 2;
    this.viewBox.y = cy - newH / 2;
    this.viewBox.w = newW;
    this.viewBox.h = newH;
    this.applyViewBox();
  }
  zoomAtPoint(clientX, clientY, factor) {
    const rect = this.svg.getBoundingClientRect();
    const px = (clientX - rect.left) / rect.width;
    const py = (clientY - rect.top) / rect.height;
    const mouseX = this.viewBox.x + px * this.viewBox.w;
    const mouseY = this.viewBox.y + py * this.viewBox.h;
    
    const newW = this.viewBox.w * factor;
    const newH = this.viewBox.h * factor;
    if (newW > 1200 || newW < 180) return;
    
    this.viewBox.x = mouseX - px * newW;
    this.viewBox.y = mouseY - py * newH;
    this.viewBox.w = newW;
    this.viewBox.h = newH;
    this.applyViewBox();
  }
  reset() {
    this.viewBox = { ...this.defaultViewBox };
    this.applyViewBox();
  }
  panTo(targetX, targetY, zoomLevel = 450) {
    this.viewBox.w = zoomLevel;
    this.viewBox.h = zoomLevel * (780 / 850);
    this.viewBox.x = targetX - this.viewBox.w / 2;
    this.viewBox.y = targetY - this.viewBox.h / 2;
    this.applyViewBox();
  }
  applyViewBox() {
    this.svg.setAttribute('viewBox', `${this.viewBox.x} ${this.viewBox.y} ${this.viewBox.w} ${this.viewBox.h}`);
  }
}

// Leaflet Map Instance (Esri Satellite, Google Satellite, Carto Voyager - 100% Reliable & Unblocked)
let leafletMap = null;
let leafletGeoLayers = {};

function initLeafletMap() {
  if (leafletMap || typeof L === 'undefined') return;
  
  // High-resolution Esri World Imagery (Satellite) - PRIMARY BASE LAYER (DEFAULT)
  const satLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    maxZoom: 18,
    attribution: 'Tiles &copy; Esri &mdash; Source: Esri, Maxar, Earthstar Geographics'
  });
  
  // Google Satellite (High Reliability Backup)
  const googleSatLayer = L.tileLayer('https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    maxZoom: 19,
    attribution: '&copy; Google Maps Satellite'
  });

  // CARTO Voyager (Clean physical/road map, 100% reliable, no 403 block)
  const cartoLayer = L.tileLayer('https://basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
    maxZoom: 19,
    attribution: '&copy; CARTO &copy; OpenStreetMap contributors'
  });

  // Esri World Topo Map (Topographic elevation & relief)
  const topoLayer = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}', {
    maxZoom: 18,
    attribution: 'Tiles &copy; Esri'
  });
  
  leafletMap = L.map('leaflet-map', {
    center: [52.1, 19.4],
    zoom: 6,
    layers: [satLayer]
  });
  
  const baseLayers = {
    "🛰️ Zdjęcia Satelitarne (Esri Satellite)": satLayer,
    "🛰️ Zdjęcia Satelitarne (Google)": googleSatLayer,
    "🗺️ Czysta Mapa Terenowa (CARTO Voyager)": cartoLayer,
    "⛰️ Rzeźba i Topografia (Esri Topo)": topoLayer
  };
  L.control.layers(baseLayers).addTo(leafletMap);
  
  GEO_DATA.regions.forEach(reg => {
    const latlngs = reg.polygon.map(p => [p[0], p[1]]);
    const poly = L.polygon(latlngs, {
      color: '#38bdf8',
      weight: 2.5,
      fillColor: '#38bdf8',
      fillOpacity: 0.35
    }).addTo(leafletMap);
    poly.bindPopup(`<b>${reg.name}</b><br><small>${reg.beltName}</small>`);
    poly.on('click', () => handleItemClick(reg.id));
    leafletGeoLayers[reg.id] = poly;
  });
  
  GEO_DATA.rivers.forEach(riv => {
    const latlngs = riv.path.map(p => [p[0], p[1]]);
    const line = L.polyline(latlngs, {
      color: '#06b6d4',
      weight: 4.5,
      opacity: 0.95
    }).addTo(leafletMap);
    line.bindPopup(`<b>Rzeka ${riv.name}</b><br><small>${riv.basinName} (${riv.tributarySide})</small>`);
    line.on('click', () => handleItemClick(riv.id));
    leafletGeoLayers[riv.id] = line;
  });
}

function loadSavedState() {
  try {
    const saved = localStorage.getItem('poland_geo_quiz_v2');
    if (saved) {
      const parsed = JSON.parse(saved);
      if (parsed.stats) STATE.stats = Object.assign(STATE.stats, parsed.stats);
      if (typeof parsed.soundEnabled === 'boolean') STATE.soundEnabled = parsed.soundEnabled;
      if (parsed.sessionType) STATE.sessionType = parsed.sessionType;
    }
  } catch(e) { console.warn('Could not load localStorage', e); }
  updateStatsDisplay();
}

function saveCurrentState() {
  try {
    localStorage.setItem('poland_geo_quiz_v2', JSON.stringify({
      stats: STATE.stats,
      soundEnabled: STATE.soundEnabled,
      sessionType: STATE.sessionType
    }));
  } catch(e) {}
}

function resetProgress() {
  if (!confirm('Czy na pewno chcesz zresetować wszystkie postępy i statystyki nauki?')) return;
  STATE.stats = {
    mastered: [],
    mistakes: {},
    streak: 0,
    bestStreak: 0,
    totalAnswered: 0,
    totalCorrect: 0
  };
  saveCurrentState();
  updateStatsDisplay();
  setMode(STATE.currentMode);
}
