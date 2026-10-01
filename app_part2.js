// Data Lookups
function getAllItems() {
  return [...GEO_DATA.regions, ...GEO_DATA.rivers];
}

function getItemById(id) {
  return getAllItems().find(it => it.id === id);
}

function getActivePool() {
  const all = getAllItems();
  switch(STATE.currentFilter) {
    case 'regions':
      return GEO_DATA.regions;
    case 'rivers':
      return GEO_DATA.rivers;
    case 'wisla':
      return GEO_DATA.rivers.filter(r => r.basin === 'wisla');
    case 'odra':
      return GEO_DATA.rivers.filter(r => r.basin === 'odra');
    case 'mistakes':
      return all.filter(it => (STATE.stats.mistakes[it.id] || 0) > 0);
    default:
      return all;
  }
}

function updateStatsDisplay() {
  const allCount = getAllItems().length;
  const masteredCount = STATE.stats.mastered.length;
  const accuracy = STATE.stats.totalAnswered > 0 
    ? Math.round((STATE.stats.totalCorrect / STATE.stats.totalAnswered) * 100) 
    : 0;
  
  const elMastered = document.getElementById('stat-mastered');
  const elAccuracy = document.getElementById('stat-accuracy');
  const elStreak = document.getElementById('stat-streak');
  const elMistakes = document.getElementById('stat-mistakes-count');
  
  if (elMastered) elMastered.innerText = `${masteredCount} / ${allCount}`;
  if (elAccuracy) elAccuracy.innerText = `${accuracy}%`;
  if (elStreak) elStreak.innerText = `${STATE.stats.streak}`;
  if (elMistakes) elMistakes.innerText = `${Object.keys(STATE.stats.mistakes).length}`;
}

// Session Queue Manager (Each place appears exactly 2 times)
function buildSessionQueue(customPool = null) {
  const pool = customPool || getActivePool();
  if (!pool || pool.length === 0) return false;
  
  // Exactly 2 occurrences of each item in the pool
  let deck = [...pool, ...pool];
  
  // Fisher-Yates shuffle
  for (let i = deck.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    const temp = deck[i];
    deck[i] = deck[j];
    deck[j] = temp;
  }
  
  // Anti-adjacent swap pass: ensure identical items are not side-by-side
  for (let i = 0; i < deck.length - 1; i++) {
    if (deck[i].id === deck[i + 1].id) {
      for (let k = i + 2; k < deck.length; k++) {
        if (deck[k].id !== deck[i].id) {
          const temp = deck[i + 1];
          deck[i + 1] = deck[k];
          deck[k] = temp;
          break;
        }
      }
    }
  }
  
  STATE.sessionQueue = deck;
  STATE.sessionIndex = 0;
  STATE.sessionTotal = deck.length;
  STATE.sessionScore = 0;
  STATE.sessionMistakes = {};
  STATE.selectedItem = null;
  STATE.currentQuestionFailed = false;
  return true;
}

function restartSession() {
  buildSessionQueue();
  if (STATE.currentMode === 'choice') {
    renderChoiceQuestion();
  } else if (STATE.currentMode === 'learn') {
    setMode('locate');
  } else {
    renderLocateQuestion();
  }
}

function advanceSession() {
  STATE.sessionIndex++;
  if (STATE.sessionIndex >= STATE.sessionTotal) {
    renderSessionSummary();
  } else {
    if (STATE.currentMode === 'choice') {
      renderChoiceQuestion();
    } else {
      renderLocateQuestion();
    }
  }
}

// Mode Management
function setMode(mode) {
  STATE.currentMode = mode;
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.mode === mode);
  });
  
  clearMapHighlights();
  
  // Anti-spoiler: in quiz modes, labels MUST BE HIDDEN by default
  const labelsGrp = document.getElementById('svg-labels');
  const labelBtn = document.getElementById('btn-toggle-labels');
  if (mode === 'learn') {
    STATE.labelsEnabled = true;
    if (labelsGrp) labelsGrp.style.display = 'block';
    if (labelBtn) labelBtn.innerText = '🏷️ Etykiety: WŁ (L)';
  } else {
    STATE.labelsEnabled = false;
    if (labelsGrp) labelsGrp.style.display = 'none';
    if (labelBtn) labelBtn.innerText = '🏷️ Etykiety: WYŁ (L)';
  }
  
  if (mode === 'cheatsheet') {
    document.getElementById('map-wrapper-col').style.display = 'none';
    document.getElementById('main-container').style.gridTemplateColumns = '1fr';
    renderCheatSheet();
    return;
  } else {
    document.getElementById('map-wrapper-col').style.display = 'flex';
    document.getElementById('main-container').style.gridTemplateColumns = window.innerWidth > 1024 ? '1fr 420px' : '1fr';
  }
  
  if (mode === 'learn') {
    // Restore pointer events on both regions and rivers in learn mode
    const riversEl = document.getElementById('svg-rivers');
    if (riversEl) riversEl.style.pointerEvents = 'all';
    renderLearnMode();
  } else if (mode === 'locate') {
    if (!STATE.sessionQueue || STATE.sessionQueue.length === 0 || STATE.sessionIndex >= STATE.sessionTotal) {
      buildSessionQueue();
    }
    renderLocateQuestion();
  } else if (mode === 'choice') {
    if (!STATE.sessionQueue || STATE.sessionQueue.length === 0 || STATE.sessionIndex >= STATE.sessionTotal) {
      buildSessionQueue();
    }
    renderChoiceQuestion();
  } else if (mode === 'cram') {
    startCramSession();
  }
}

function setFilter(filter) {
  STATE.currentFilter = filter;
  document.querySelectorAll('.filter-pill').forEach(pill => {
    pill.classList.toggle('active', pill.dataset.filter === filter);
  });
  
  const pool = getActivePool();
  if (pool.length === 0 && filter === 'mistakes') {
    alert('Gratulacje! Twoja lista błędów jest pusta. Nie masz żadnych zaległych pomyłek!');
    setFilter('all');
    return;
  }
  
  buildSessionQueue();
  
  if (STATE.currentMode === 'learn') {
    renderLearnMode();
  } else if (STATE.currentMode === 'choice') {
    renderChoiceQuestion();
  } else if (STATE.currentMode === 'cram') {
    startCramSession();
  } else {
    renderLocateQuestion();
  }
}

// Map Highlighting Utilities
function clearMapHighlights() {
  document.querySelectorAll('.region-path, .river-path').forEach(el => {
    el.classList.remove('target-highlight', 'correct-flash', 'wrong-flash', 'selected-highlight');
    if (el.classList.contains('region-path')) {
      el.style.fillOpacity = '0.85';
    }
  });
  const pin = document.getElementById('svg-pinpoint');
  if (pin) pin.style.display = 'none';
}

// IMPORTANT: shouldPan is false by default so the map NEVER auto-zooms unprompted!
function highlightMapItem(id, styleClass = 'target-highlight', shouldPan = false) {
  clearMapHighlights();
  const item = getItemById(id);
  if (!item) return;
  
  const el = document.getElementById(`svg-item-${id}`);
  if (el) {
    if (item.category === 'river') {
      const pathEl = el.querySelector('.river-path');
      if (pathEl) pathEl.classList.add(styleClass);
    } else {
      el.classList.add(styleClass);
    }
    
    // Position pulsing pin at center
    const pin = document.getElementById('svg-pinpoint');
    if (pin && item.projCenter) {
      pin.setAttribute('transform', `translate(${item.projCenter[0]}, ${item.projCenter[1]})`);
      pin.style.display = 'block';
    }
  }
  
  // Only pan if explicitly requested
  if (shouldPan && svgPanZoom && item.projCenter) {
    svgPanZoom.panTo(item.projCenter[0], item.projCenter[1], 460);
  }
  
  if (shouldPan && leafletMap && leafletGeoLayers[id]) {
    const layer = leafletGeoLayers[id];
    if (layer.getBounds) {
      leafletMap.fitBounds(layer.getBounds(), { padding: [40, 40], maxZoom: 8 });
    }
  }
}

// 1. LEARN MODE
function renderLearnMode(selectedId = null) {
  const pool = getActivePool();
  if (pool.length === 0) return;
  
  const current = selectedId ? getItemById(selectedId) : (STATE.currentItem || pool[0]);
  STATE.currentItem = current;
  highlightMapItem(current.id, 'target-highlight', false);
  
  const panel = document.getElementById('side-panel-content');
  const isRegion = current.category === 'region';
  
  panel.innerHTML = `
    <div class="study-card">
      <div class="card-header-badge">
        <span class="badge ${isRegion ? 'badge-green' : 'badge-blue'}">
          ${isRegion ? '🏞️ ' + current.beltName : '🌊 ' + current.basinName}
        </span>
        <span class="badge badge-purple">Ćwiartka: ${current.quadrantName}</span>
      </div>
      
      <h2 class="item-title">${current.name}</h2>
      
      <div class="mnemonic-box">
        <div class="mnemonic-title">💡 Złota zasada pamięciowa (Mnemonik)</div>
        <div>${current.mnemonic}</div>
      </div>
      
      <div class="info-grid">
        ${isRegion ? `
          <div class="info-row">
            <div class="info-label">Miasta i punkty:</div>
            <div class="info-val">${current.keyCities.join(', ')}</div>
          </div>
        ` : `
          <div class="info-row">
            <div class="info-label">Typ dopływu:</div>
            <div class="info-val">${current.tributarySide}</div>
          </div>
          <div class="info-row">
            <div class="info-label">Ujście:</div>
            <div class="info-val">${current.mouth}</div>
          </div>
          <div class="info-row">
            <div class="info-label">Miasta nad rzeką:</div>
            <div class="info-val">${current.keyTowns.join(', ')}</div>
          </div>
        `}
        <div class="info-row">
          <div class="info-label">Opis:</div>
          <div class="info-val">${current.description}</div>
        </div>
      </div>
      
      <div style="display: flex; gap: 0.5rem; margin-top: 0.5rem;">
        <button class="btn btn-primary" style="flex: 1;" onclick="testThisItem('${current.id}')">
          🎯 Przetestuj mnie z tego!
        </button>
      </div>
    </div>
    
    <div class="study-card" style="max-height: 280px; overflow-y: auto;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
        <h4 style="font-size: 0.9rem; font-weight: 700;">Szybka lista (${pool.length} obiektów):</h4>
        <input type="text" id="quick-search-input" placeholder="Szukaj obiektu..." 
               style="padding: 0.3rem 0.5rem; border: 1px solid var(--border-color); border-radius: 0.4rem; font-size: 0.78rem; width: 140px;"
               oninput="filterQuickList(this.value)">
      </div>
      <div id="quick-list-container" style="display: flex; flex-direction: column; gap: 0.35rem;">
        ${renderQuickListItems(pool, current.id)}
      </div>
    </div>
  `;
}

function renderQuickListItems(items, activeId) {
  return items.map(it => {
    const isMastered = STATE.stats.mastered.includes(it.id);
    const hasMistake = (STATE.stats.mistakes[it.id] || 0) > 0;
    const isActive = it.id === activeId;
    return `
      <div onclick="renderLearnMode('${it.id}')" 
           style="padding: 0.4rem 0.6rem; border-radius: 0.4rem; font-size: 0.82rem; cursor: pointer; display: flex; align-items: center; justify-content: space-between; background: ${isActive ? 'var(--primary-light)' : 'var(--bg-primary)'}; color: ${isActive ? 'var(--primary)' : 'var(--text-main)'}; font-weight: ${isActive ? '700' : '500'};">
        <span>${it.category === 'region' ? '🏞️' : '🌊'} ${it.name}</span>
        <span>${isMastered ? '⭐' : (hasMistake ? '⚠️' : '')}</span>
      </div>
    `;
  }).join('');
}

function filterQuickList(term) {
  const norm = term.toLowerCase().trim();
  const pool = getActivePool();
  const filtered = pool.filter(it => it.name.toLowerCase().includes(norm));
  document.getElementById('quick-list-container').innerHTML = renderQuickListItems(filtered, STATE.currentItem ? STATE.currentItem.id : '');
}

function testThisItem(id) {
  STATE.currentItem = getItemById(id);
  setMode('locate');
}

// 2. LOCATE ON MAP MODE (Click to Select, Space to Confirm)
function renderLocateQuestion() {
  if (!STATE.sessionQueue || STATE.sessionQueue.length === 0) {
    buildSessionQueue();
  }
  
  if (STATE.sessionIndex >= STATE.sessionTotal) {
    renderSessionSummary();
    return;
  }
  
  STATE.currentItem = STATE.sessionQueue[STATE.sessionIndex];
  STATE.selectedItem = null;
  STATE.answeredCurrent = false;
  STATE.currentQuestionFailed = false;
  
  // CRITICAL FIX: If target is a region, disable river hitboxes so rivers don't intercept clicks!
  const isRegion = STATE.currentItem.category === 'region';
  const riversGroup = document.getElementById('svg-rivers');
  if (riversGroup) {
    riversGroup.style.pointerEvents = isRegion ? 'none' : 'all';
  }
  
  clearMapHighlights();
  renderLocateCard();
}

function renderLocateCard() {
  const item = STATE.currentItem;
  const isRegion = item.category === 'region';
  const panel = document.getElementById('side-panel-content');
  const currentNum = STATE.sessionIndex + 1;
  const totalNum = STATE.sessionTotal;
  const progressPct = Math.round((STATE.sessionIndex / totalNum) * 100);
  
  panel.innerHTML = `
    <div class="study-card">
      <div class="progress-container">
        <div class="progress-labels">
          <span><b>Pytanie ${currentNum} / ${totalNum}</b> (2x każdy obiekt)</span>
          <span>Wynik sesji: <b>${STATE.sessionScore}</b> / ${STATE.sessionIndex}</span>
        </div>
        <div class="progress-bar-bg" style="height: 9px; margin-top: 4px;">
          <div class="progress-bar-fill" style="width: ${progressPct}%;"></div>
        </div>
      </div>

      <div class="card-header-badge" style="margin-top: 0.2rem;">
        <span class="badge ${isRegion ? 'badge-green' : 'badge-blue'}">
          ${isRegion ? '🏞️ Region Polski' : '🌊 Rzeka / Dopływ'}
        </span>
        <span class="badge badge-purple">Ćwiartka: ${item.quadrantName}</span>
      </div>
      
      <div style="margin: 0.4rem 0;">
        <div id="locate-instruction-text" style="font-size: 0.85rem; color: var(--text-muted); font-weight: 600;">
          Wskaż na mapie obiekt:
        </div>
        <div style="font-size: 1.65rem; font-weight: 900; color: var(--primary); margin-top: 0.2rem; line-height: 1.2;">
          ${item.name}
        </div>
        <div style="font-size: 0.78rem; color: var(--text-muted); margin-top: 0.35rem;">
          👆 <b>Krok 1:</b> Kliknij obiekt na mapie &bull; ⌨️ <b>Krok 2:</b> Naciśnij <b>SPACJĘ</b>, aby zatwierdzić.
        </div>
      </div>

      <!-- Live Selection Box -->
      <div id="locate-selection-box" style="display: none;"></div>
      
      <div id="locate-hint-box" style="display: none;" class="mnemonic-box">
        <div class="mnemonic-title">💡 Podpowiedź geograficzna:</div>
        <div>${item.hint}</div>
        <div style="font-size: 0.8rem; margin-top: 0.3rem;"><b>Ćwiartka:</b> ${item.quadrantName} &bull; <b>Kategoria:</b> ${isRegion ? item.beltName : item.basinName}</div>
      </div>
      
      <div id="locate-feedback" class="feedback-banner"></div>
      
      <div id="locate-actions-box" style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: 0.4rem;">
        <button id="btn-confirm-selection" class="btn btn-success" style="display: none; padding: 0.75rem; font-size: 1rem;" onclick="confirmSelection()">
          ✅ Zatwierdź wybór (Spacja)
        </button>
        <button id="btn-hint" class="btn btn-outline" onclick="showLocateHint()">
          💡 Pokaż podpowiedź (H)
        </button>
        <button id="btn-reveal" class="btn btn-outline" onclick="revealLocateAnswer()">
          👁️ Pokaż gdzie to jest (R)
        </button>
        <button id="btn-next-locate" class="btn btn-primary" style="display: none; padding: 0.75rem; font-size: 1rem;" onclick="advanceSession()">
          ${currentNum < totalNum ? `Następne pytanie (${currentNum + 1}/${totalNum}) (Spacja) ➔` : '🏁 Zakończ sesję i zobacz wyniki (Spacja) ➔'}
        </button>
      </div>
    </div>
    
    <div class="study-card" style="font-size: 0.82rem; color: var(--text-muted);">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.3rem;">
        <strong style="color: var(--text-main);">Ochrona przed missclickiem:</strong>
        <button class="btn btn-outline" style="font-size: 0.72rem; padding: 0.15rem 0.4rem;" onclick="restartSession()">
          🔄 Nowa sesja 1/86
        </button>
      </div>
      <div>Kliknięcie podświetla Twój wybór na błękitno bez utraty punktów. Możesz klikać dowolną liczbę razy, a odpowiedź sprawdzana jest dopiero po wciśnięciu <b>SPACJI</b>!</div>
    </div>
  `;
}

function showLocateHint() {
  const box = document.getElementById('locate-hint-box');
  if (box) box.style.display = 'block';
}

function revealLocateAnswer() {
  if (STATE.answeredCurrent) return;
  STATE.answeredCurrent = true;
  STATE.currentQuestionFailed = true;
  
  const target = STATE.currentItem;
  highlightMapItem(target.id, 'target-highlight', false);
  
  STATE.stats.totalAnswered++;
  STATE.stats.streak = 0;
  STATE.stats.mistakes[target.id] = (STATE.stats.mistakes[target.id] || 0) + 1;
  STATE.sessionMistakes[target.id] = (STATE.sessionMistakes[target.id] || 0) + 1;
  
  saveCurrentState();
  updateStatsDisplay();
  
  const selBox = document.getElementById('locate-selection-box');
  if (selBox) selBox.style.display = 'none';
  
  const confirmBtn = document.getElementById('btn-confirm-selection');
  if (confirmBtn) confirmBtn.style.display = 'none';
  
  const fb = document.getElementById('locate-feedback');
  fb.className = 'feedback-banner error';
  fb.innerHTML = `
    <div><b>Prawidłowe położenie:</b> ${target.name}</div>
    <div style="font-size: 0.85rem; margin-top: 0.3rem;">💡 <b>Mnemonik:</b> ${target.mnemonic}</div>
  `;
  
  const nextBtn = document.getElementById('btn-next-locate');
  if (nextBtn) {
    const currentNum = STATE.sessionIndex + 1;
    const totalNum = STATE.sessionTotal;
    nextBtn.innerText = currentNum < totalNum ? `Następne pytanie (${currentNum + 1}/${totalNum}) (Spacja) ➔` : '🏁 Zakończ sesję i zobacz wyniki (Spacja) ➔';
    nextBtn.style.display = 'block';
  }
}

// Map Click Handler (Dispatched from SVG and Leaflet)
function handleItemClick(clickedId) {
  if (STATE.currentMode === 'learn') {
    renderLearnMode(clickedId);
    return;
  }
  
  if (STATE.currentMode === 'locate') {
    if (STATE.answeredCurrent) return;
    
    const clickedItem = getItemById(clickedId);
    if (!clickedItem) return;
    
    // Select this item without penalizing for misclicks!
    STATE.selectedItem = clickedItem;
    
    // Highlight selected item on map with special cyan glow, NEVER auto-zoom!
    highlightMapItem(clickedId, 'selected-highlight', false);
    
    // Update live selection card
    const selBox = document.getElementById('locate-selection-box');
    if (selBox) {
      selBox.style.display = 'block';
      selBox.className = 'selection-card';
      selBox.innerHTML = `
        <div style="font-size: 0.75rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">
          📍 Wybrano na mapie:
        </div>
        <div style="font-size: 1.25rem; font-weight: 900; color: var(--primary); margin: 0.2rem 0;">
          ${clickedItem.category === 'region' ? '🏞️' : '🌊'} ${clickedItem.name}
        </div>
        <div style="font-size: 0.78rem; color: var(--text-muted);">
          Naciśnij <b>SPACJĘ</b> lub kliknij zielony przycisk poniżej, aby zatwierdzić. (Jeśli kliknięto obok, po prostu kliknij inny obiekt!).
        </div>
      `;
    }
    
    // Show confirm button
    const confirmBtn = document.getElementById('btn-confirm-selection');
    if (confirmBtn) {
      confirmBtn.style.display = 'block';
      confirmBtn.innerHTML = `✅ Zatwierdź: <b>${clickedItem.name}</b> (Spacja)`;
    }
  }
}

// Confirmation of Selection (Called via Space key or confirm button)
function confirmSelection() {
  if (STATE.answeredCurrent || !STATE.selectedItem) return;
  
  const target = STATE.currentItem;
  const selected = STATE.selectedItem;
  STATE.answeredCurrent = true;
  
  const selBox = document.getElementById('locate-selection-box');
  if (selBox) selBox.style.display = 'none';
  
  const confirmBtn = document.getElementById('btn-confirm-selection');
  if (confirmBtn) confirmBtn.style.display = 'none';
  
  const fb = document.getElementById('locate-feedback');
  const nextBtn = document.getElementById('btn-next-locate');
  const currentNum = STATE.sessionIndex + 1;
  const totalNum = STATE.sessionTotal;
  
  if (selected.id === target.id) {
    // CORRECT!
    STATE.stats.totalAnswered++;
    if (!STATE.currentQuestionFailed) {
      STATE.sessionScore++;
      STATE.stats.totalCorrect++;
      STATE.stats.streak++;
      if (STATE.stats.streak > STATE.stats.bestStreak) STATE.stats.bestStreak = STATE.stats.streak;
      
      if (STATE.stats.mistakes[target.id]) {
        STATE.stats.mistakes[target.id] = Math.max(0, STATE.stats.mistakes[target.id] - 1);
        if (STATE.stats.mistakes[target.id] === 0) delete STATE.stats.mistakes[target.id];
      }
      if (!STATE.stats.mastered.includes(target.id)) {
        STATE.stats.mastered.push(target.id);
      }
    }
    
    sfx.playCorrect();
    // Highlight green, NO AUTO-ZOOM!
    highlightMapItem(target.id, 'correct-flash', false);
    
    fb.className = 'feedback-banner success';
    fb.innerHTML = `
      <div>🎉 <b>Świetnie!</b> To jest ${target.name}.</div>
      <div style="font-size: 0.83rem; margin-top: 0.2rem;">💡 ${target.mnemonic}</div>
    `;
    
    if (STATE.stats.streak >= 5) sfx.playStreak();
    
    if (nextBtn) {
      nextBtn.innerText = currentNum < totalNum 
        ? `Następne pytanie (${currentNum + 1}/${totalNum}) (Spacja) ➔` 
        : '🏁 Zakończ sesję i zobacz wyniki (Spacja) ➔';
      nextBtn.style.display = 'block';
    }
    
    saveCurrentState();
    updateStatsDisplay();
    
  } else {
    // WRONG!
    sfx.playWrong();
    STATE.currentQuestionFailed = true;
    STATE.stats.streak = 0;
    STATE.stats.totalAnswered++;
    STATE.stats.mistakes[target.id] = (STATE.stats.mistakes[target.id] || 0) + 1;
    STATE.sessionMistakes[target.id] = (STATE.sessionMistakes[target.id] || 0) + 1;
    
    // Highlight wrong item red, NO AUTO-ZOOM!
    highlightMapItem(selected.id, 'wrong-flash', false);
    
    // Also show pulsing pin on correct target
    const pin = document.getElementById('svg-pinpoint');
    if (pin && target.projCenter) {
      pin.setAttribute('transform', `translate(${target.projCenter[0]}, ${target.projCenter[1]})`);
      pin.style.display = 'block';
    }
    
    fb.className = 'feedback-banner error';
    fb.innerHTML = `
      <div>❌ <b>Pomyłka!</b> Wybrano: <b>${selected.name}</b>.</div>
      <div style="font-size: 0.83rem; margin-top: 0.2rem;">Prawidłowa pozycja <b>${target.name}</b> została oznaczona pulsującym punktem na mapie.</div>
      <div style="font-size: 0.83rem; margin-top: 0.2rem;">💡 <b>Mnemonik:</b> ${target.mnemonic}</div>
    `;
    
    if (nextBtn) {
      nextBtn.innerText = currentNum < totalNum 
        ? `Przejdź dalej (${currentNum + 1}/${totalNum}) (Spacja) ➔` 
        : '🏁 Zakończ sesję (Spacja) ➔';
      nextBtn.style.display = 'block';
    }
    
    saveCurrentState();
    updateStatsDisplay();
  }
}

// 3. MULTIPLE CHOICE MODE (1 z 4)
function renderChoiceQuestion() {
  if (!STATE.sessionQueue || STATE.sessionQueue.length === 0) {
    buildSessionQueue();
  }
  
  if (STATE.sessionIndex >= STATE.sessionTotal) {
    renderSessionSummary();
    return;
  }
  
  const target = STATE.sessionQueue[STATE.sessionIndex];
  STATE.currentItem = target;
  STATE.answeredCurrent = false;
  STATE.currentQuestionFailed = false;
  
  const sameCat = getAllItems().filter(it => it.category === target.category && it.id !== target.id);
  const shuffledDistractors = [...sameCat].sort(() => 0.5 - Math.random());
  const distractors = shuffledDistractors.slice(0, 3);
  
  const options = [target, ...distractors].sort(() => 0.5 - Math.random());
  STATE.quizOptions = options;
  
  // Highlight target on map without zooming!
  highlightMapItem(target.id, 'target-highlight', false);
  renderChoiceCard();
}

function renderChoiceCard() {
  const target = STATE.currentItem;
  const isRegion = target.category === 'region';
  const panel = document.getElementById('side-panel-content');
  const currentNum = STATE.sessionIndex + 1;
  const totalNum = STATE.sessionTotal;
  const progressPct = Math.round((STATE.sessionIndex / totalNum) * 100);
  
  panel.innerHTML = `
    <div class="study-card">
      <div class="progress-container">
        <div class="progress-labels">
          <span><b>Pytanie ${currentNum} / ${totalNum}</b> (2x każdy obiekt)</span>
          <span>Wynik sesji: <b>${STATE.sessionScore}</b> / ${STATE.sessionIndex}</span>
        </div>
        <div class="progress-bar-bg" style="height: 9px; margin-top: 4px;">
          <div class="progress-bar-fill" style="width: ${progressPct}%;"></div>
        </div>
      </div>

      <div class="card-header-badge" style="margin-top: 0.2rem;">
        <span class="badge ${isRegion ? 'badge-green' : 'badge-blue'}">
          ${isRegion ? 'Typ: Region Polski' : 'Typ: Rzeka Polski'}
        </span>
        <span class="badge badge-purple">Quiz: Wybór 1 z 4</span>
      </div>
      
      <div style="margin: 0.4rem 0;">
        <h3 style="font-size: 1.15rem; font-weight: 800;">Co wskazuje podświetlony element na mapie?</h3>
        <p style="font-size: 0.82rem; color: var(--text-muted); margin-top: 0.2rem;">
          Spójrz na pulsujący obiekt na mapie i wybierz właściwą nazwę (klawisze 1-4).
        </p>
      </div>
      
      <div class="quiz-options-list">
        ${STATE.quizOptions.map((opt, idx) => `
          <button id="opt-btn-${idx}" class="quiz-opt-btn" onclick="handleChoiceAnswer(${idx})">
            <span class="opt-key">${idx + 1}</span>
            <span>${opt.name}</span>
          </button>
        `).join('')}
      </div>
      
      <div id="choice-feedback" class="feedback-banner"></div>
      
      <button id="btn-next-choice" class="btn btn-primary" style="display: none; margin-top: 0.5rem;" onclick="advanceSession()">
        ${currentNum < totalNum ? `Następne pytanie (${currentNum + 1}/${totalNum}) (Spacja) ➔` : '🏁 Zakończ sesję i zobacz wyniki (Spacja) ➔'}
      </button>
    </div>
  `;
}

function handleChoiceAnswer(chosenIdx) {
  if (STATE.answeredCurrent) return;
  STATE.answeredCurrent = true;
  
  const target = STATE.currentItem;
  const chosen = STATE.quizOptions[chosenIdx];
  const fb = document.getElementById('choice-feedback');
  const nextBtn = document.getElementById('btn-next-choice');
  
  STATE.stats.totalAnswered++;
  
  STATE.quizOptions.forEach((opt, idx) => {
    const btn = document.getElementById(`opt-btn-${idx}`);
    btn.disabled = true;
    if (opt.id === target.id) {
      btn.classList.add('correct');
    } else if (idx === chosenIdx) {
      btn.classList.add('wrong');
    }
  });
  
  if (chosen.id === target.id) {
    if (!STATE.currentQuestionFailed) {
      STATE.sessionScore++;
      STATE.stats.totalCorrect++;
      STATE.stats.streak++;
      if (STATE.stats.streak > STATE.stats.bestStreak) STATE.stats.bestStreak = STATE.stats.streak;
      if (!STATE.stats.mastered.includes(target.id)) STATE.stats.mastered.push(target.id);
      if (STATE.stats.mistakes[target.id]) delete STATE.stats.mistakes[target.id];
    }
    
    sfx.playCorrect();
    highlightMapItem(target.id, 'correct-flash', false);
    
    fb.className = 'feedback-banner success';
    fb.innerHTML = `
      <div>🎉 <b>Prawidłowo!</b> To jest ${target.name}.</div>
      <div style="font-size: 0.83rem; margin-top: 0.2rem;">💡 ${target.mnemonic}</div>
    `;
    if (STATE.stats.streak >= 5) sfx.playStreak();
  } else {
    sfx.playWrong();
    STATE.currentQuestionFailed = true;
    STATE.stats.streak = 0;
    STATE.stats.mistakes[target.id] = (STATE.stats.mistakes[target.id] || 0) + 1;
    STATE.sessionMistakes[target.id] = (STATE.sessionMistakes[target.id] || 0) + 1;
    
    fb.className = 'feedback-banner error';
    fb.innerHTML = `
      <div>❌ <b>Pomyłka!</b> Prawidłowa odpowiedź to <b>${target.name}</b>.</div>
      <div style="font-size: 0.83rem; margin-top: 0.2rem;">💡 ${target.mnemonic}</div>
    `;
  }
  
  if (nextBtn) {
    const currentNum = STATE.sessionIndex + 1;
    const totalNum = STATE.sessionTotal;
    nextBtn.innerText = currentNum < totalNum ? `Następne pytanie (${currentNum + 1}/${totalNum}) (Spacja) ➔` : '🏁 Zakończ sesję i zobacz wyniki (Spacja) ➔';
    nextBtn.style.display = 'block';
  }
  saveCurrentState();
  updateStatsDisplay();
}

// 4. CRAM EXAM (SPACED REPETITION)
function startCramSession() {
  const pool = getActivePool();
  const unmastered = pool.filter(it => !STATE.stats.mastered.includes(it.id));
  const hasMistakes = pool.filter(it => (STATE.stats.mistakes[it.id] || 0) > 0);
  const targetPool = [...new Set([...unmastered, ...hasMistakes])];
  
  if (targetPool.length === 0) {
    const panel = document.getElementById('side-panel-content');
    panel.innerHTML = `
      <div class="study-card" style="text-align: center; padding: 2rem;">
        <div style="font-size: 3rem; margin-bottom: 0.5rem;">🏆</div>
        <h2 style="font-size: 1.5rem; font-weight: 800; color: var(--success);">100% OPANOWANE!</h2>
        <p style="font-size: 0.9rem; color: var(--text-muted); margin: 0.75rem 0;">
          Wszystkie obiekty z tej kategorii zostały przez Ciebie opanowane bezbłędnie. Jesteś w pełni gotowy na jutrzejszy sprawdzian!
        </p>
        <button class="btn btn-primary" onclick="restartSession()">Rozpocznij pełną sesję 86 pytań</button>
      </div>
    `;
    return;
  }
  
  buildSessionQueue(targetPool);
  renderLocateQuestion();
}

// 5. SESSION SUMMARY MODAL / SCREEN (After 86 questions complete)
function renderSessionSummary() {
  clearMapHighlights();
  const panel = document.getElementById('side-panel-content');
  const total = STATE.sessionTotal;
  const score = STATE.sessionScore;
  const pct = total > 0 ? Math.round((score / total) * 100) : 0;
  
  let gradeBadge = '';
  let gradeDesc = '';
  if (pct >= 90) {
    gradeBadge = '<span class="badge badge-green" style="font-size: 1rem; padding: 0.3rem 0.8rem;">🌟 Celujący (6)</span>';
    gradeDesc = 'Perfekcyjne przygotowanie! Znasz mapę Polski w najdrobniejszych szczegółach!';
  } else if (pct >= 75) {
    gradeBadge = '<span class="badge badge-blue" style="font-size: 1rem; padding: 0.3rem 0.8rem;">👍 Bardzo Dobry (5)</span>';
    gradeDesc = 'Świetna orientacja na mapie! Tylko nieliczne drobiazgi do dopracowania.';
  } else if (pct >= 60) {
    gradeBadge = '<span class="badge badge-amber" style="font-size: 1rem; padding: 0.3rem 0.8rem;">📖 Dobry (4)</span>';
    gradeDesc = 'Dobra baza, ale przejrzyj listę błędów poniżej i powtórz trudniejsze obiekty.';
  } else {
    gradeBadge = '<span class="badge badge-purple" style="font-size: 1rem; padding: 0.3rem 0.8rem;">⚠️ Wymaga Powtórzenia</span>';
    gradeDesc = 'Zrób szybką sesję powtórkową z samych błędów, aby utrwalić położenie obiektów przed jutrem.';
  }
  
  const mistakeIds = Object.keys(STATE.sessionMistakes);
  const mistakeItems = mistakeIds.map(id => ({ item: getItemById(id), count: STATE.sessionMistakes[id] })).filter(m => m.item);
  
  panel.innerHTML = `
    <div class="study-card" style="border: 2px solid var(--primary);">
      <div style="text-align: center; padding: 0.5rem 0;">
        <div style="font-size: 2.8rem; margin-bottom: 0.2rem;">🏆</div>
        <h2 style="font-size: 1.45rem; font-weight: 900; color: var(--primary);">Koniec Sesji Egzaminacyjnej!</h2>
        <div style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.2rem;">
          Ukończono <b>${total} pytań</b> (każdy obiekt przetestowany 2 razy).
        </div>
      </div>

      <div style="background: var(--bg-primary); border-radius: 0.75rem; padding: 1rem; text-align: center; border: 1px solid var(--border-color);">
        <div style="font-size: 0.8rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase;">Twój Wynik:</div>
        <div style="font-size: 2.4rem; font-weight: 900; color: ${pct >= 75 ? 'var(--success)' : (pct >= 60 ? 'var(--primary)' : 'var(--danger)')};">
          ${score} / ${total}
        </div>
        <div style="font-size: 1.1rem; font-weight: 800; margin-bottom: 0.5rem;">
          Skuteczność: ${pct}%
        </div>
        <div style="margin-top: 0.4rem;">${gradeBadge}</div>
        <div style="font-size: 0.82rem; color: var(--text-muted); margin-top: 0.5rem;">${gradeDesc}</div>
      </div>

      <div style="display: flex; flex-direction: column; gap: 0.5rem; margin-top: 0.5rem;">
        <button class="btn btn-primary" onclick="restartSession()">
          🔁 Rozpocznij nową sesję (86 pytań)
        </button>
        ${mistakeItems.length > 0 ? `
          <button class="btn btn-outline" style="border-color: var(--danger); color: var(--danger);" onclick="retryMistakesSession()">
            ⚠️ Przetestuj tylko błędy z tej sesji (${mistakeItems.length})
          </button>
        ` : ''}
        <button class="btn btn-outline" onclick="setMode('learn')">
          🎓 Wróć do trybu nauki i mnemoników
        </button>
      </div>
    </div>

    ${mistakeItems.length > 0 ? `
      <div class="study-card" style="max-height: 320px; overflow-y: auto;">
        <h4 style="font-size: 0.95rem; font-weight: 800; color: var(--danger); margin-bottom: 0.5rem;">
          ⚠️ Obiekty do powtórzenia (${mistakeItems.length}):
        </h4>
        <div style="display: flex; flex-direction: column; gap: 0.5rem;">
          ${mistakeItems.map(m => `
            <div style="padding: 0.5rem 0.75rem; border-radius: 0.5rem; background: var(--bg-primary); border-left: 3px solid var(--danger); font-size: 0.82rem;">
              <div style="display: flex; justify-content: space-between; align-items: center; font-weight: 700;">
                <span>${m.item.category === 'region' ? '🏞️' : '🌊'} ${m.item.name}</span>
                <span style="color: var(--danger); font-size: 0.75rem;">Błędy: ${m.count}x</span>
              </div>
              <div style="font-size: 0.78rem; color: var(--text-muted); margin-top: 0.2rem;">
                💡 <b>Mnemonik:</b> ${m.item.mnemonic}
              </div>
              <button class="btn btn-outline" style="font-size: 0.72rem; padding: 0.15rem 0.4rem; margin-top: 0.3rem;" onclick="highlightMapItem('${m.item.id}', 'target-highlight', false)">
                👁️ Pokaż na mapie
              </button>
            </div>
          `).join('')}
        </div>
      </div>
    ` : `
      <div class="study-card" style="text-align: center; background: var(--success-light); border-color: #bbf7d0;">
        <div style="font-size: 1.8rem;">🎉</div>
        <div style="font-weight: 800; color: var(--success); font-size: 1rem;">Czyste konto!</div>
        <div style="font-size: 0.82rem; color: #166534; margin-top: 0.2rem;">
          W tej sesji nie popełniono ani jednego błędu! Jesteś w pełni przygotowany na sprawdzian.
        </div>
      </div>
    `}
  `;
}

function retryMistakesSession() {
  const mistakeIds = Object.keys(STATE.sessionMistakes);
  const mistakeItems = mistakeIds.map(id => getItemById(id)).filter(Boolean);
  if (mistakeItems.length === 0) {
    alert('Brak błędów do powtórzenia!');
    return;
  }
  buildSessionQueue(mistakeItems);
  setMode('locate');
}

// 6. CHEAT SHEET (ŚCIĄGA DO DRUKU)
function renderCheatSheet() {
  const panel = document.getElementById('side-panel-content');
  panel.innerHTML = `
    <div class="study-card cheatsheet-section">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
        <h2 style="font-size: 1.35rem; font-weight: 800;">📋 Ekspresowa Ściąga Geograficzna do Druku</h2>
        <button class="btn btn-primary" onclick="window.print()">🖨️ Drukuj / Zapisz jako PDF</button>
      </div>
      
      <h3 style="font-size: 1.1rem; font-weight: 800; color: #166534; margin: 1rem 0 0.5rem;">🏞️ 24 Regiony Fizycznogeograficzne Polski</h3>
      <table class="cheatsheet-table">
        <thead>
          <tr>
            <th>Nazwa Regionu</th>
            <th>Pas rzeźby</th>
            <th>Główne miasta / obiekty</th>
            <th>Zasada pamięciowa (Mnemonik)</th>
          </tr>
        </thead>
        <tbody>
          ${GEO_DATA.regions.map(r => `
            <tr>
              <td><b>${r.name}</b></td>
              <td>${r.beltName}</td>
              <td>${r.keyCities.join(', ')}</td>
              <td>${r.mnemonic}</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
      
      <h3 style="font-size: 1.1rem; font-weight: 800; color: #1e40af; margin: 1.5rem 0 0.5rem;">🌊 19 Rzek i Dopływów (+ Wisła i Odra)</h3>
      <table class="cheatsheet-table">
        <thead>
          <tr>
            <th>Rzeka</th>
            <th>Dorzecze</th>
            <th>Ujście i kierunek</th>
            <th>Zasada pamięciowa (Mnemonik)</th>
          </tr>
        </thead>
        <tbody>
          ${GEO_DATA.rivers.map(r => `
            <tr>
              <td><b>${r.name}</b></td>
              <td>${r.basinName}</td>
              <td>${r.tributarySide}, ${r.mouth}</td>
              <td>${r.mnemonic}</td>
            </tr>
          `).join('')}
        </tbody>
      </table>
    </div>
  `;
}

// Keyboard shortcuts (Space = confirm selection, or advance to next)
window.addEventListener('keydown', (e) => {
  if (['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;
  
  if (e.key === ' ' || e.code === 'Space') {
    e.preventDefault();
    if (STATE.currentMode === 'locate') {
      if (!STATE.answeredCurrent) {
        if (STATE.selectedItem) {
          confirmSelection();
        } else {
          // Tell user to select first
          const prompt = document.getElementById('locate-instruction-text');
          if (prompt) {
            prompt.style.color = 'var(--danger)';
            prompt.innerHTML = '👆 <b>Najpierw kliknij na mapie obiekt, który chcesz wskazać!</b>';
            setTimeout(() => {
              if (prompt) {
                prompt.style.color = 'var(--text-muted)';
                prompt.innerText = 'Wskaż na mapie obiekt:';
              }
            }, 2000);
          }
        }
      } else {
        advanceSession();
      }
    } else if (STATE.currentMode === 'choice') {
      const btn = document.getElementById('btn-next-choice');
      if (btn && btn.style.display !== 'none') advanceSession();
    }
  } else if (['1', '2', '3', '4'].includes(e.key)) {
    if (STATE.currentMode === 'choice') {
      const idx = parseInt(e.key, 10) - 1;
      handleChoiceAnswer(idx);
    }
  } else if (e.key.toLowerCase() === 'h') {
    if (STATE.currentMode === 'locate') showLocateHint();
  } else if (e.key.toLowerCase() === 'r') {
    if (STATE.currentMode === 'locate') revealLocateAnswer();
  } else if (e.key.toLowerCase() === 'm') {
    toggleMapView();
  } else if (e.key.toLowerCase() === 'l') {
    toggleLabels();
  }
});

// View toggles
function toggleMapView() {
  const isSvg = STATE.mapView === 'svg';
  STATE.mapView = isSvg ? 'leaflet' : 'svg';
  
  document.getElementById('btn-view-svg').classList.toggle('active', !isSvg);
  document.getElementById('btn-view-leaflet').classList.toggle('active', isSvg);
  
  document.getElementById('svg-map').style.display = isSvg ? 'none' : 'block';
  document.getElementById('leaflet-map').style.display = isSvg ? 'block' : 'none';
  
  if (STATE.mapView === 'leaflet') {
    initLeafletMap();
    if (leafletMap) leafletMap.invalidateSize();
  }
}

function toggleLabels() {
  STATE.labelsEnabled = !STATE.labelsEnabled;
  const labelsGrp = document.getElementById('svg-labels');
  if (labelsGrp) {
    labelsGrp.style.display = STATE.labelsEnabled ? 'block' : 'none';
  }
  document.getElementById('btn-toggle-labels').innerText = STATE.labelsEnabled ? '🏷️ Etykiety: WŁ (L)' : '🏷️ Etykiety: WYŁ (L)';
}

function toggleSound() {
  STATE.soundEnabled = !STATE.soundEnabled;
  saveCurrentState();
  document.getElementById('btn-toggle-sound').innerText = STATE.soundEnabled ? '🔊 Dźwięk: WŁ' : '🔇 Dźwięk: WYŁ';
}

function toggleTheme() {
  const isDark = document.body.getAttribute('data-theme') === 'dark';
  document.body.setAttribute('data-theme', isDark ? 'light' : 'dark');
  document.getElementById('btn-toggle-theme').innerText = isDark ? '🌙 Tryb ciemny' : '☀️ Tryb jasny';
}
