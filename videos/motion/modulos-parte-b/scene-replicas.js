const { seg, eo, eio, lerp } = kit;

// Entrada de la escena 6: las 30 replicas. Treinta dias simulados, cada uno con sus llegadas.
// Cada cuadrito dibuja el perfil de llegadas de un dia, sacado de su propia semilla.
const COLS = 6, FILAS = 5, BW = 210, BH = 92, GX = 28, GY = 20, PX = 260, PY = 356;
const PERFIL = [0.1, 0.34, 0.68, 0.94, 1, 0.86, 0.9, 0.76, 0.6, 0.46, 0.31, 0.2, 0.11, 0.04];

kit.scene('replicas', {
  init(kit) {
    kit.css('.replicas-titulo { font-family:var(--display, var(--sans, system-ui, sans-serif)); font-size:64px; font-weight:700; margin:0; line-height:1.06 }' +
      '.replicas-marco { fill:none; stroke:var(--borde); stroke-width:2 }' +
      '.replicas-piso { fill:none; stroke:var(--grilla); stroke-width:1 }');
    let marcos = '', curvas = [];
    for (let i = 0; i < COLS * FILAS; i++) {
      const x = PX + (i % COLS) * (BW + GX), y = PY + Math.floor(i / COLS) * (BH + GY);
      const r = kit.rng(140 + i * 7), amp = 0.7 + r() * 0.52;
      const pts = PERFIL.map((v, j) => [x + BW * (j / (PERFIL.length - 1)), y + BH - (BH - 16) * Math.min(1, v * amp * (0.86 + r() * 0.28))]);
      marcos += '<rect class="replicas-marco" x="' + x + '" y="' + y + '" width="' + BW + '" height="' + BH + '" rx="5"/>' +
        '<path class="replicas-piso" d="M' + x + ' ' + (y + BH) + ' H' + (x + BW) + '"/>';
      curvas.push(W.curva('replicas-c', pts, 'var(--main)', 3));
    }
    kit.stage.append(kit.h('<div class="ground">' + W.logo(kit) +
      '<svg class="art replicas-grilla" viewBox="0 0 1920 1080">' + W.tramas('replicas') + '</svg>' +
      '<svg class="art replicas-panel" viewBox="0 0 1920 1080"><g class="replicas-marcos">' + marcos + '</g>' +
      curvas.map((c) => c.markup).join('') + '</svg>' +
      '<div class="edge"></div>' +
      '<div class="words" style="left:260px; top:144px; width:1280px; gap:12px">' +
      '<h2 class="replicas-titulo">Treinta d&iacute;as simulados, no uno</h2>' +
      '<p class="sub replicas-sub">30 r&eacute;plicas de cada escenario, cada una con llegadas distintas</p></div>' +
      '<p class="pendiente replicas-nota" style="position:absolute; left:260px; bottom:70px">CADA CUADRO ES UN D&Iacute;A &middot; MISMAS REGLAS, OTRAS LLEGADAS</p></div>'));
    const q = (s) => kit.stage.querySelector(s);
    this.largos = curvas.map((c) => c.largo);
    this.curvas = Array.from(kit.stage.querySelectorAll('.replicas-c'));
    this.curvas.forEach((el, i) => { el.style.strokeDasharray = this.largos[i].toFixed(1); });
    this.marcos = q('.replicas-marcos');
    this.panel = q('.replicas-panel');
    this.grilla = q('.replicas-grilla');
    this.titulo = q('.replicas-titulo');
    this.sub = q('.replicas-sub');
    this.nota = q('.replicas-nota');
  },
  render(t) {
    const push = eio(seg(t, 0, 10));
    this.grilla.style.transform = 'scale(' + lerp(1, 1.016, push) + ')';
    this.panel.style.transform = 'translateY(' + lerp(0, -10, push) + 'px)';
    this.titulo.style.opacity = eo(seg(t, -0.4, 0.6));
    this.sub.style.opacity = eo(seg(t, 0.6, 1.3));
    this.marcos.style.opacity = (eo(seg(t, -0.5, 0.7)) * 0.7).toFixed(3);
    this.nota.style.opacity = eo(seg(t, 8.4, 9.2)) * 0.9;
    // Los treinta dias se dibujan uno tras otro, de arriba a la izquierda hacia abajo.
    this.curvas.forEach((el, i) => {
      const a = eio(seg(t, 1 + i * 0.2, 1 + i * 0.2 + 0.7));
      el.style.strokeDashoffset = (this.largos[i] * (1 - a)).toFixed(1);
      el.style.opacity = (0.45 + 0.55 * a).toFixed(3);
    });
  },
});
