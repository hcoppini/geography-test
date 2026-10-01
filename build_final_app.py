# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
import json
import geo_regions
import geo_rivers
import template_css
import template_js
import template_js_part2

# Projection settings
SCALE_X = 74.0
ASPECT = 1.623  # 1 / cos(52 deg)
SCALE_Y = SCALE_X * ASPECT
ORIGIN_LON = 14.0
ORIGIN_LAT = 55.0
OFFSET_X = 45.0
OFFSET_Y = 25.0

def proj(lat, lon):
    x = (lon - ORIGIN_LON) * SCALE_X + OFFSET_X
    y = (ORIGIN_LAT - lat) * SCALE_Y + OFFSET_Y
    return round(x, 1), round(y, 1)

def chaikin(points, iterations=2, closed=True):
    pts = list(points)
    for _ in range(iterations):
        if len(pts) < 3:
            break
        new_pts = []
        n = len(pts)
        if closed:
            for i in range(n):
                p0 = pts[i]
                p1 = pts[(i + 1) % n]
                new_pts.append((0.75 * p0[0] + 0.25 * p1[0], 0.75 * p0[1] + 0.25 * p1[1]))
                new_pts.append((0.25 * p0[0] + 0.75 * p1[0], 0.25 * p0[1] + 0.75 * p1[1]))
        else:
            new_pts.append(pts[0])
            for i in range(len(pts) - 1):
                p0 = pts[i]
                p1 = pts[i + 1]
                new_pts.append((0.75 * p0[0] + 0.25 * p1[0], 0.75 * p0[1] + 0.25 * p1[1]))
                new_pts.append((0.25 * p0[0] + 0.75 * p1[0], 0.25 * p0[1] + 0.75 * p1[1]))
            new_pts.append(pts[-1])
        pts = new_pts
    return pts

def path_d(coords, closed=True, smooth=True):
    pts = [proj(lat, lon) for lat, lon in coords]
    if smooth and len(pts) >= 3:
        pts = chaikin(pts, iterations=2, closed=closed)
    if not pts:
        return ""
    d = f"M {pts[0][0]:.1f} {pts[0][1]:.1f}"
    for p in pts[1:]:
        d += f" L {p[0]:.1f} {p[1]:.1f}"
    if closed:
        d += " Z"
    return d

for r in geo_regions.REGIONS_DATA:
    r["projCenter"] = proj(r["center"][0], r["center"][1])
    r["svgPath"] = path_d(r["polygon"], closed=True, smooth=True)

for rv in geo_rivers.RIVERS_DATA:
    rv["projCenter"] = proj(rv["center"][0], rv["center"][1])
    rv["svgPath"] = path_d(rv["path"], closed=False, smooth=True)

baseline_svg = []
for br in geo_rivers.BASELINE_RIVERS:
    d = path_d(br["path"], closed=False, smooth=True)
    baseline_svg.append(f'<path class="baseline-river" d="{d}"><title>{br["name"]}</title></path>')

poland_border_d = path_d(geo_rivers.POLAND_BORDER, closed=True, smooth=True)

svg_elements = []
svg_elements.append("""
  <defs>
    <filter id="shadow" x="-5%" y="-5%" width="115%" height="115%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.12"/>
    </filter>
    <filter id="river-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#0284c7" />
    </marker>
  </defs>
""")

svg_elements.append(f'<path id="poland-border" class="poland-boundary" d="{poland_border_d}" />')

svg_elements.append("""
  <!-- Róża wiatrów -->
  <g transform="translate(740, 90)" opacity="0.65">
    <circle cx="0" cy="0" r="28" fill="white" stroke="#cbd5e1" stroke-width="1.5" />
    <path d="M 0 -24 L 6 -5 L 0 -1 L -6 -5 Z" fill="#dc2626" />
    <path d="M 0 24 L 6 5 L 0 1 L -6 5 Z" fill="#64748b" />
    <path d="M -24 0 L -5 -6 L -1 0 L -5 6 Z" fill="#64748b" />
    <path d="M 24 0 L 5 -6 L 1 0 L 5 6 Z" fill="#64748b" />
    <text x="0" y="-30" text-anchor="middle" font-size="11" font-weight="900" fill="#dc2626">N</text>
    <text x="0" y="38" text-anchor="middle" font-size="10" font-weight="700" fill="#64748b">S</text>
    <text x="-32" y="4" text-anchor="end" font-size="10" font-weight="700" fill="#64748b">W</text>
    <text x="32" y="4" text-anchor="start" font-size="10" font-weight="700" fill="#64748b">E</text>
  </g>
""")

svg_elements.append('<g id="svg-regions">')
# Render larger regions first, and small regions (Pieniny, Tatry, Żuławy) last so they sit on the very top and are 100% clickable!
top_regions = {'pieniny', 'tatry', 'zulawy_wislane', 'kaszuby', 'niecka_nidzianska'}
sorted_regions = sorted(geo_regions.REGIONS_DATA, key=lambda r: 10 if r['id'] in top_regions else 1)
for r in sorted_regions:
    belt_class = f"region-{r['belt']}"
    svg_elements.append(f"""
      <path id="svg-item-{r['id']}" 
            class="region-path {belt_class}" 
            data-id="{r['id']}" 
            data-name="{r['name']}"
            d="{r['svgPath']}" 
            onclick="handleItemClick('{r['id']}')"
            onmouseenter="showSvgTooltip(event, '{r['name']}', '{r['beltName']}')"
            onmousemove="moveSvgTooltip(event)"
            onmouseleave="hideSvgTooltip()">
      </path>
    """)
svg_elements.append('</g>')

svg_elements.append('<g id="svg-baseline-rivers">')
svg_elements.extend(baseline_svg)
w_x, w_y = proj(52.23, 21.01)
o_x, o_y = proj(51.11, 17.03)
svg_elements.append(f'<text x="{w_x+8}" y="{w_y-8}" fill="#60a5fa" font-size="11" font-weight="700" font-style="italic">Wisła</text>')
svg_elements.append(f'<text x="{o_x-32}" y="{o_y-12}" fill="#60a5fa" font-size="11" font-weight="700" font-style="italic">Odra</text>')
svg_elements.append('</g>')

svg_elements.append('<g id="svg-rivers">')
for rv in geo_rivers.RIVERS_DATA:
    svg_elements.append(f"""
      <g id="svg-item-{rv['id']}" class="river-group" data-id="{rv['id']}">
        <path class="river-hitbox" 
              d="{rv['svgPath']}" 
              onclick="handleItemClick('{rv['id']}')"
              onmouseenter="showSvgTooltip(event, 'Rzeka {rv['name']}', '{rv['basinName']} ({rv['tributarySide']})')"
              onmousemove="moveSvgTooltip(event)"
              onmouseleave="hideSvgTooltip()" />
        <path class="river-path" 
              d="{rv['svgPath']}" 
              pointer-events="none" />
      </g>
    """)
svg_elements.append('</g>')

svg_elements.append('<g id="svg-labels" style="pointer-events: none; display: none;">')
for r in geo_regions.REGIONS_DATA:
    cx, cy = r["projCenter"]
    label_txt = r['name'].split(' / ')[0]
    svg_elements.append(f'<text x="{cx}" y="{cy}" text-anchor="middle" font-size="9" font-weight="700" fill="#334155" opacity="0.85">{label_txt}</text>')
for rv in geo_rivers.RIVERS_DATA:
    cx, cy = rv["projCenter"]
    svg_elements.append(f'<text x="{cx}" y="{cy-5}" text-anchor="middle" font-size="8.5" font-weight="800" fill="#0369a1" opacity="0.9">{rv["name"]}</text>')
svg_elements.append('</g>')

svg_elements.append("""
  <g id="svg-pinpoint" style="display: none; pointer-events: none;">
    <circle cx="0" cy="0" r="28" fill="#3b82f6" fill-opacity="0.25">
      <animate attributeName="r" values="8;36;8" dur="2s" repeatCount="indefinite" />
      <animate attributeName="fill-opacity" values="0.45;0.05;0.45" dur="2s" repeatCount="indefinite" />
    </circle>
    <circle cx="0" cy="0" r="7" fill="#2563eb" stroke="#ffffff" stroke-width="2.5" />
    <path d="M 0 -18 L 4 -10 L -4 -10 Z" fill="#2563eb" />
  </g>
""")

svg_full = f'<svg id="svg-map" viewBox="0 0 850 780" xmlns="http://www.w3.org/2000/svg">{"".join(svg_elements)}</svg>'

geo_data_dict = {
    "regions": geo_regions.REGIONS_DATA,
    "rivers": geo_rivers.RIVERS_DATA,
    "border": geo_rivers.POLAND_BORDER
}

geo_data_json = json.dumps(geo_data_dict, ensure_ascii=False)

HTML_SKELETON = """<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Polska: Regiony i Rzeki — Mistrz Mapy (Quiz & Cram App)</title>
  
  <!-- Leaflet CSS & JS for Satellite & OpenStreetMap -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" crossorigin=""/>
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" crossorigin=""></script>
  
  <style>
/*__CSS_PLACEHOLDER__*/
  </style>
</head>
<body>

  <header>
    <div class="brand">
      <span style="font-size: 1.5rem;">🇵🇱</span>
      <div>
        <h1>Polska: Regiony i Rzeki</h1>
        <div style="font-size: 0.72rem; color: var(--text-muted); font-weight: 600;">Interaktywny Trener Mapy przed Egzaminem</div>
      </div>
      <span class="brand-badge">24 Regiony + 19 Rzek</span>
    </div>

    <div class="stats-bar">
      <div class="stat-pill" title="Liczba trwale opanowanych obiektów">
        <span>⭐ Opanowane:</span>
        <strong id="stat-mastered">0 / 43</strong>
      </div>
      <div class="stat-pill" title="Aktualna seria poprawnych trafień z rzędu">
        <span>🔥 Seria:</span>
        <strong id="stat-streak">0</strong>
      </div>
      <div class="stat-pill" title="Procentowa skuteczność trafień">
        <span>🎯 Skuteczność:</span>
        <strong id="stat-accuracy">0%</strong>
      </div>
      <div class="stat-pill" title="Obiekty wymagające powtórzenia">
        <span>⚠️ Błędy:</span>
        <strong id="stat-mistakes-count">0</strong>
      </div>
    </div>

    <div class="top-actions">
      <button id="btn-toggle-sound" class="btn" onclick="toggleSound()">🔊 Dźwięk: WŁ</button>
      <button id="btn-toggle-theme" class="btn" onclick="toggleTheme()">🌙 Ciemny</button>
      <button class="btn btn-primary" onclick="restartSession()" title="Rozpocznij nową sesję 86 pytań (2x każdy obiekt)">🔁 Nowa sesja (86)</button>
      <button class="btn btn-outline" onclick="resetProgress()" title="Wyczyść statystyki sesji">🔄 Resetuj</button>
    </div>
  </header>

  <div class="sub-nav">
    <div class="mode-tabs">
      <button class="tab-btn active" data-mode="learn" onclick="setMode('learn')">
        🎓 Tryb Nauki & Mnemoniki
      </button>
      <button class="tab-btn" data-mode="locate" onclick="setMode('locate')">
        🎯 Wskaż na mapie (86 pytań)
      </button>
      <button class="tab-btn" data-mode="choice" onclick="setMode('choice')">
        ❓ Wybór 1 z 4 (86 pytań)
      </button>
      <button class="tab-btn" data-mode="cram" onclick="setMode('cram')">
        ⚡ Ekspresowy Egzamin (Błędy)
      </button>
      <button class="tab-btn" data-mode="cheatsheet" onclick="setMode('cheatsheet')">
        📋 Ściąga do druku
      </button>
    </div>

    <div class="filter-pills">
      <button class="filter-pill active" data-filter="all" onclick="setFilter('all')">Wszystko (43)</button>
      <button class="filter-pill" data-filter="regions" onclick="setFilter('regions')">🏞️ Regiony (24)</button>
      <button class="filter-pill" data-filter="rivers" onclick="setFilter('rivers')">🌊 Rzeki (19)</button>
      <button class="filter-pill" data-filter="wisla" onclick="setFilter('wisla')">Dorzecze Wisły</button>
      <button class="filter-pill" data-filter="odra" onclick="setFilter('odra')">Dorzecze Odry</button>
      <button class="filter-pill" data-filter="mistakes" onclick="setFilter('mistakes')">⚠️ Tylko błędy</button>
    </div>
  </div>

  <main id="main-container">
    
    <div id="map-wrapper-col" class="map-wrapper">
      <div class="map-toolbar">
        <div class="map-view-switcher">
          <span style="font-weight: 700; margin-right: 0.3rem;">Widok mapy:</span>
          <div class="toggle-btn-group">
            <button id="btn-view-svg" class="active" onclick="if(STATE.mapView!=='svg') toggleMapView()">
              🗺️ Szkolna Konturowa (SVG)
            </button>
            <button id="btn-view-leaflet" onclick="if(STATE.mapView!=='leaflet') toggleMapView()">
              🛰️ Satelita / OSM
            </button>
          </div>
        </div>

        <div style="display: flex; gap: 0.5rem; align-items: center;">
          <button id="btn-toggle-labels" class="btn" style="padding: 0.25rem 0.5rem; font-size: 0.78rem;" onclick="toggleLabels()">
            🏷️ Etykiety: WŁ (L)
          </button>
          <span style="font-size: 0.75rem;">Skróty: M (mapa), Spacja (dalej)</span>
        </div>
      </div>

      <div class="map-container" id="map-canvas-container">
        <!--__SVG_PLACEHOLDER__-->

        <div id="leaflet-map"></div>

        <div class="map-controls-floating">
          <button class="floating-btn" onclick="svgPanZoom.zoom(0.8)" title="Przybliż">+</button>
          <button class="floating-btn" onclick="svgPanZoom.zoom(1.2)" title="Oddal">−</button>
          <button class="floating-btn" onclick="svgPanZoom.reset()" title="Zresetuj widok">⟲</button>
        </div>

        <div class="legend-box">
          <div style="font-weight: 800; font-size: 0.75rem; margin-bottom: 0.2rem;">Pasy Rzeźby Polski:</div>
          <div class="legend-grid">
            <div class="legend-item"><span class="legend-color" style="background: #a7f3d0;"></span> Pobrzeża</div>
            <div class="legend-item"><span class="legend-color" style="background: #bae6fd;"></span> Pojezierza</div>
            <div class="legend-item"><span class="legend-color" style="background: #d9f99d;"></span> Niziny Środkowe</div>
            <div class="legend-item"><span class="legend-color" style="background: #fde68a;"></span> Wyżyny Polskie</div>
            <div class="legend-item"><span class="legend-color" style="background: #fbcfe8;"></span> Kotliny Podkarpackie</div>
            <div class="legend-item"><span class="legend-color" style="background: #fecaca;"></span> Góry (Karpaty / Sudety)</div>
          </div>
          <div style="margin-top: 0.2rem; display: flex; align-items: center; gap: 0.4rem;">
            <span style="width: 14px; height: 3px; background: #0284c7; display: inline-block;"></span>
            <span>Rzeki i dopływy (19 rzek)</span>
          </div>
        </div>

        <div id="map-tooltip" class="map-tooltip"></div>
      </div>
    </div>

    <div id="side-panel-col" class="side-panel">
      <div id="side-panel-content">
      </div>
    </div>

  </main>

  <script>
    const GEO_DATA = /*__GEO_DATA_PLACEHOLDER__*/;
/*__JS_PART1_PLACEHOLDER__*/
/*__JS_PART2_PLACEHOLDER__*/

    // Anti-spoiler tooltip logic: do not show names when in quiz mode!
    const tooltipEl = document.getElementById('map-tooltip');
    function showSvgTooltip(e, name, extra) {
      if (STATE.currentMode !== 'learn') {
        tooltipEl.innerHTML = `<span style="font-weight: 600; color: #93c5fd;">🎯 Kliknij, aby wskazać ten obiekt</span>`;
        tooltipEl.style.display = 'block';
        moveSvgTooltip(e);
        return;
      }
      tooltipEl.innerHTML = `<strong>${name}</strong><br><small style="opacity: 0.85">${extra}</small>`;
      tooltipEl.style.display = 'block';
      moveSvgTooltip(e);
    }
    function moveSvgTooltip(e) {
      const container = document.getElementById('map-canvas-container').getBoundingClientRect();
      tooltipEl.style.left = (e.clientX - container.left) + 'px';
      tooltipEl.style.top = (e.clientY - container.top) + 'px';
    }
    function hideSvgTooltip() {
      tooltipEl.style.display = 'none';
    }

    let svgPanZoom;
    window.addEventListener('DOMContentLoaded', () => {
      const svgEl = document.getElementById('svg-map');
      const containerEl = document.getElementById('map-canvas-container');
      svgPanZoom = new SvgPanZoom(svgEl, containerEl);
      
      loadSavedState();
      setMode('learn');
    });
  </script>
</body>
</html>
"""

with open('app.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

with open('app_part1.js', 'r', encoding='utf-8') as f:
    js_content_part1 = f.read()

with open('app_part2.js', 'r', encoding='utf-8') as f:
    js_content_part2 = f.read()

final_html = (
    HTML_SKELETON
    .replace("/*__CSS_PLACEHOLDER__*/", css_content)
    .replace("<!--__SVG_PLACEHOLDER__-->", svg_full)
    .replace("/*__GEO_DATA_PLACEHOLDER__*/", geo_data_json)
    .replace("/*__JS_PART1_PLACEHOLDER__*/", js_content_part1)
    .replace("/*__JS_PART2_PLACEHOLDER__*/", js_content_part2)
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("SUCCESS: index.html has been completely regenerated with smoothed lines, anti-spoiler tooltips, and fixed geography!")
