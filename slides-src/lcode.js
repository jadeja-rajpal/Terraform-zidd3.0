(async function () {
  await document.fonts.ready;
  const NS = 'http://www.w3.org/2000/svg';
  const slide = document.querySelector('.slide');
  const sr = slide.getBoundingClientRect();
  const svg = document.createElementNS(NS, 'svg');
  svg.setAttribute('class', 'ov');
  svg.setAttribute('viewBox', '0 0 1920 1080');
  slide.appendChild(svg);
  const COL = { purple: '#8b7fe0', teal: '#2fb58a', coral: '#e2825f' };

  document.querySelectorAll('.pill[data-for]').forEach((p) => {
    const ids = p.dataset.for.split(' ');
    let x1 = 1e9, y1 = 1e9, x2 = -1e9, y2 = -1e9;
    ids.forEach((id) => {
      const el = document.querySelector('[data-k="' + id + '"]');
      if (!el) { console.error('missing target', id); return; }
      const r = el.getBoundingClientRect();
      x1 = Math.min(x1, r.left - sr.left); y1 = Math.min(y1, r.top - sr.top);
      x2 = Math.max(x2, r.right - sr.left); y2 = Math.max(y2, r.bottom - sr.top);
    });
    const padx = +(p.dataset.padx || 8), pady = +(p.dataset.pady || 4);
    x1 -= padx; x2 += padx; y1 -= pady; y2 += pady;
    const color = ['purple', 'teal', 'coral'].find((c) => p.classList.contains(c));

    const o = document.createElement('div');
    o.className = 'outline ' + color;
    o.style.left = x1 + 'px'; o.style.top = y1 + 'px';
    o.style.width = (x2 - x1) + 'px'; o.style.height = (y2 - y1) + 'px';
    slide.appendChild(o);

    const pr = p.getBoundingClientRect();
    const px = pr.left - sr.left, py = pr.top - sr.top, pw = pr.width, ph = pr.height;
    const from = p.dataset.from || 'bottom', to = p.dataset.to || 'top';
    const fx = +(p.dataset.fx || 0), fy = +(p.dataset.fy || 0);
    const tx = +(p.dataset.tx || 0), ty = +(p.dataset.ty || 0);
    let sx, sy, ex, ey;
    if (from === 'bottom') { sx = px + pw / 2 + fx; sy = py + ph; }
    if (from === 'top') { sx = px + pw / 2 + fx; sy = py; }
    if (from === 'left') { sx = px; sy = py + ph / 2 + fy; }
    if (from === 'right') { sx = px + pw; sy = py + ph / 2 + fy; }
    if (to === 'top') { ex = (x1 + x2) / 2 + tx; ey = y1; }
    if (to === 'bottom') { ex = (x1 + x2) / 2 + tx; ey = y2; }
    if (to === 'left') { ex = x1; ey = (y1 + y2) / 2 + ty; }
    if (to === 'right') { ex = x2; ey = (y1 + y2) / 2 + ty; }

    const ln = document.createElementNS(NS, 'line');
    ln.setAttribute('x1', sx); ln.setAttribute('y1', sy);
    ln.setAttribute('x2', ex); ln.setAttribute('y2', ey);
    ln.setAttribute('stroke', COL[color]); ln.setAttribute('stroke-width', '3');
    ln.setAttribute('stroke-dasharray', '9 7'); ln.setAttribute('stroke-linecap', 'round');
    svg.appendChild(ln);
    const dot = document.createElementNS(NS, 'circle');
    dot.setAttribute('cx', ex); dot.setAttribute('cy', ey); dot.setAttribute('r', 7);
    dot.setAttribute('fill', COL[color]);
    svg.appendChild(dot);
  });
  document.body.dataset.ready = '1';
})();
