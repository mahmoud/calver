/* timeline.js: renders /timeline.html from the JSON inlined by custom.py.
   Vanilla ES2020, no dependencies. State (hidden kinds, order, collapsed
   eras) lives in the URL hash as k=v pairs: #hide=a,b&order=asc&closed=x,y */
(function () {
  'use strict';

  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  var GAP_MAX = 6;

  var root = document.getElementById('timeline');
  var dataEl = document.getElementById('timeline-data');
  if (!root || !dataEl) return;  // validation failed at build; .tl-error is already on the page

  function el(tag, cls, text) {
    var node = document.createElement(tag);
    if (cls) node.className = cls;
    if (text != null) node.textContent = text;
    return node;
  }

  function fail(msg) {
    root.textContent = '';
    root.appendChild(el('p', 'tl-error', msg));
  }

  var data;
  try {
    data = JSON.parse(dataEl.textContent);
  } catch (e) {
    fail('timeline data could not be parsed');
    return;
  }
  var noscript = root.querySelector('noscript');
  if (noscript) noscript.remove();

  // --- normalize ---------------------------------------------------------
  var kinds = data.kinds;
  var kindIds = Object.keys(kinds);
  var eras = data.eras;
  var eraById = {};
  eras.forEach(function (era) { eraById[era.id] = era; });

  var events = data.events.map(function (ev, index) {
    var date = String(ev.date);
    var year = +date.slice(0, 4);
    var month = date.length >= 7 ? +date.slice(5, 7) : null;
    var day = date.length === 10 ? +date.slice(8, 10) : null;
    var t = year + ((month == null ? 7 : month) - 1) / 12 + ((day == null ? 15 : day) - 1) / 365;
    var era = null;
    for (var i = 0; i < eras.length; i++) {
      if (eras[i].start <= year && year <= eras[i].end) { era = eras[i]; break; }
    }
    return {
      index: index, year: year, month: month, day: day, t: t, era: era,
      title: ev.title, detail: ev.detail, kind: ev.kind, url: ev.url
    };
  });
  events.sort(function (a, b) { return (a.t - b.t) || (a.index - b.index); });

  var totals = {};
  events.forEach(function (ev) { totals[ev.kind] = (totals[ev.kind] || 0) + 1; });

  // --- state <-> hash ----------------------------------------------------
  var state = { hidden: new Set(), order: 'desc', closed: new Set() };

  function readHash() {
    var params = new URLSearchParams(location.hash.slice(1));
    state.hidden = new Set((params.get('hide') || '').split(',').filter(function (k) { return k in kinds; }));
    state.order = params.get('order') === 'asc' ? 'asc' : 'desc';
    state.closed = new Set((params.get('closed') || '').split(',').filter(function (id) { return id in eraById; }));
  }

  function writeHash() {
    var params = new URLSearchParams();
    if (state.hidden.size) params.set('hide', kindIds.filter(function (k) { return state.hidden.has(k); }).join(','));
    if (state.order === 'asc') params.set('order', 'asc');
    if (state.closed.size) params.set('closed', eras.map(function (e) { return e.id; }).filter(function (id) { return state.closed.has(id); }).join(','));
    var hash = params.toString().replace(/%2C/g, ',');
    history.replaceState(null, '', hash ? '#' + hash : location.pathname + location.search);
  }

  readHash();

  // --- toolbar -----------------------------------------------------------
  var toolbar = el('div', 'tl-toolbar');
  var legend = el('fieldset', 'tl-legend');
  legend.appendChild(el('legend', 'sr-only', 'Show kinds'));
  kindIds.forEach(function (kind) {
    var label = el('label', 'tl-kind');
    label.dataset.kind = kind;
    var box = el('input');
    box.type = 'checkbox';
    box.checked = !state.hidden.has(kind);
    box.addEventListener('change', function () {
      if (box.checked) state.hidden.delete(kind); else state.hidden.add(kind);
      renderList();
      writeHash();
    });
    label.appendChild(box);
    label.appendChild(el('span', 'tl-swatch'));
    label.appendChild(el('span', null, kinds[kind]));
    label.appendChild(el('span', 'tl-count', ' (' + (totals[kind] || 0) + ')'));
    legend.appendChild(label);
  });
  toolbar.appendChild(legend);

  var orderBtn = el('button', 'tl-btn');
  orderBtn.id = 'tl-order';
  orderBtn.type = 'button';
  orderBtn.addEventListener('click', function () {
    state.order = state.order === 'desc' ? 'asc' : 'desc';
    renderList();
    writeHash();
  });
  toolbar.appendChild(orderBtn);

  var foldBtn = el('button', 'tl-btn');
  foldBtn.id = 'tl-fold';
  foldBtn.type = 'button';
  foldBtn.addEventListener('click', function () {
    var open = anyOpen();
    visibleEras().forEach(function (d) { d.open = !open; });
    if (open) eras.forEach(function (e) { state.closed.add(e.id); });
    else state.closed.clear();
    relabel();
    writeHash();
  });
  toolbar.appendChild(foldBtn);
  root.appendChild(toolbar);

  function visibleEras() {
    return Array.prototype.slice.call(root.querySelectorAll('.tl-era:not([hidden])'));
  }
  function anyOpen() {
    return visibleEras().some(function (d) { return d.open; });
  }
  function relabel() {
    orderBtn.textContent = state.order === 'desc' ? 'Oldest first' : 'Newest first';
    foldBtn.textContent = anyOpen() ? 'Collapse all' : 'Expand all';
  }

  // --- list --------------------------------------------------------------
  function renderEvent(ev, prev) {
    var li = el('li', 'tl-ev');
    li.dataset.kind = ev.kind;
    var g = prev ? Math.min(GAP_MAX, Math.max(0, Math.abs(ev.t - prev.t))) : 0;
    li.style.setProperty('--gap', String(Math.round(g * 10) / 10));

    var when = el('div', 'tl-when');
    when.appendChild(el('span', 'tl-year', String(ev.year)));
    if (ev.month != null) {
      var md = MONTHS[ev.month - 1] || String(ev.month);
      if (ev.day != null) md += ' ' + ev.day;
      when.appendChild(el('span', 'tl-md', md));
    }
    li.appendChild(when);

    var dot = el('span', 'tl-dot');
    dot.setAttribute('aria-hidden', 'true');
    li.appendChild(dot);

    var body = el('div', 'tl-body');
    var title = el('div', 'tl-title');
    var a = el('a', null, ev.title);
    a.href = ev.url;
    a.target = '_blank';
    a.rel = 'noopener';
    title.appendChild(a);
    title.appendChild(el('span', 'tl-tag', kinds[ev.kind] || ev.kind));
    body.appendChild(title);
    body.appendChild(el('p', 'tl-detail', ev.detail));
    li.appendChild(body);
    return li;
  }

  function renderEra(era, evs) {
    var details = el('details', 'tl-era');
    details.id = 'era-' + era.id;
    details.open = !state.closed.has(era.id);

    var summary = el('summary');
    var h = el('h2', 'tl-era-h', era.title);
    var span = era.start === era.end ? String(era.start) : era.start + '\u2013' + era.end;
    h.appendChild(el('span', 'tl-era-span', span + ' \u00b7 ' + evs.length + (evs.length === 1 ? ' event' : ' events')));
    summary.appendChild(h);
    details.appendChild(summary);
    details.appendChild(el('p', 'tl-era-blurb', era.blurb));

    var ol = el('ol', 'tl-list');
    var prev = null;
    evs.forEach(function (ev) {
      ol.appendChild(renderEvent(ev, prev));
      prev = ev;
    });
    details.appendChild(ol);

    details.addEventListener('toggle', function () {
      if (details.open) state.closed.delete(era.id); else state.closed.add(era.id);
      relabel();
      writeHash();
    });
    return details;
  }

  function renderList() {
    while (toolbar.nextSibling) toolbar.nextSibling.remove();
    var visible = events.filter(function (ev) { return !state.hidden.has(ev.kind); });
    if (state.order === 'desc') visible = visible.slice().reverse();
    if (!visible.length) {
      root.appendChild(el('p', 'tl-empty', 'No kinds selected.'));
      relabel();
      return;
    }
    var byEra = {};
    visible.forEach(function (ev) {
      var id = ev.era ? ev.era.id : '';
      (byEra[id] = byEra[id] || []).push(ev);
    });
    var ordered = state.order === 'desc' ? eras.slice().reverse() : eras;
    ordered.forEach(function (era) {
      if (byEra[era.id]) root.appendChild(renderEra(era, byEra[era.id]));
    });
    relabel();
  }

  renderList();

  // --- deep link ---------------------------------------------------------
  var hash = location.hash.slice(1);
  if (hash && hash.indexOf('=') === -1) {
    var target = document.getElementById(hash);
    if (target && target.classList.contains('tl-era')) target.scrollIntoView();
  }
})();
