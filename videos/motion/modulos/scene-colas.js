const { seg, eo, eio, lerp, TextFx } = kit;

// La mesa de dibujo tambien sirve para los graficos: ejes y curvas se dibujan sobre el mismo plano.
Object.assign(W, {
  // Una grilla de lineas horizontales y los dos ejes. Sin palabras: los rotulos van en HTML.
  ejes(cls, x0, y0, x1, y1, lineas) {
    let s = '<g class="' + cls + '">';
    for (let i = 1; i <= lineas; i++) {
      const y = (y1 - (y1 - y0) * (i / lineas)).toFixed(1);
      s += '<path d="M' + x0 + ' ' + y + ' H' + x1 + '" style="fill:none;stroke:var(--grilla);stroke-width:1"/>';
    }
    return s + '<path d="M' + x0 + ' ' + y0 + ' V' + y1 + ' H' + x1 + '" style="fill:none;stroke:var(--borde);stroke-width:3"/></g>';
  },
  // Una curva y su largo exacto, para revelarla con stroke-dashoffset sin medir nada en pantalla.
  curva(cls, pts, color, ancho) {
    let L = 0;
    for (let i = 1; i < pts.length; i++) L += Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]);
    const d = pts.map((p, i) => (i ? 'L' : 'M') + p[0].toFixed(1) + ' ' + p[1].toFixed(1)).join(' ');
    return { largo: L, markup: '<path class="' + cls + '" d="' + d + '" style="fill:none;stroke:' + color + ';stroke-width:' + ancho + ';stroke-linejoin:round;stroke-linecap:round"/>' };
  },
});

const X0 = 300, X1 = 1620, Y0 = 260, Y1 = 760, TOPE = 160;
const CAJA = [66, 40, 22, 14, 10, 8, 9, 11, 9, 7, 6, 5, 4, 3, 2, 0];
const SERVICIO = [8, 34, 62, 88, 108, 122, 131, 128, 118, 100, 82, 60, 40, 22, 8, 0];
const punto = (v, i, n) => [X0 + (X1 - X0) * (i / (n - 1)), Y1 - (Y1 - Y0) * (v / TOPE)];
const serie = (vs) => vs.map((v, i) => punto(v, i, vs.length));

kit.scene('colas', {
  init(kit) {
    const pc = serie(CAJA), ps = serie(SERVICIO);
    this.cCaja = W.curva('colas-caja', pc, 'var(--second)', 7);
    this.cServicio = W.curva('colas-servicio', ps, 'var(--marca)', 9);
    const picoCaja = pc[0], picoServicio = ps[6];
    kit.css('.colas-rot { position:absolute; font-size:32px; color:var(--second) }' +
      '.colas-hora { position:absolute; font-family:var(--mono, ui-monospace, monospace); font-size:27px; color:var(--tenue) }' +
      '.colas-pico { position:absolute; font-family:var(--mono, ui-monospace, monospace); font-variant-numeric:tabular-nums; font-size:54px; font-weight:700; line-height:1 }' +
      '.colas-words .line { font-size:72px }' +
      '.colas-velo { position:absolute; left:0; bottom:0; right:0; height:34%; background:linear-gradient(transparent, color-mix(in srgb, var(--ground) 94%, transparent) 46%) }');
    kit.stage.append(kit.h('<div class="ground">' +
      '<svg class="art colas-grilla" viewBox="0 0 1920 1080">' + W.tramas('colas') + '</svg>' +
      '<svg class="art colas-chart" viewBox="0 0 1920 1080">' + W.ejes('colas-ejes', X0, Y0, X1, Y1, 4) +
      this.cCaja.markup + this.cServicio.markup +
      '<circle class="colas-mc" cx="' + picoCaja[0].toFixed(1) + '" cy="' + picoCaja[1].toFixed(1) + '" r="12" style="fill:var(--second)"/>' +
      '<circle class="colas-ms" cx="' + picoServicio[0].toFixed(1) + '" cy="' + picoServicio[1].toFixed(1) + '" r="14" style="fill:var(--marca)"/></svg>' +
      '<div class="colas-velo"></div>' +
      '<div class="colas-rot colas-r1" style="left:330px; top:' + (picoCaja[1] - 86).toFixed(0) + 'px">Cola en caja</div>' +
      '<div class="colas-pico colas-p1" style="left:330px; top:' + (picoCaja[1] - 44).toFixed(0) + 'px; color:var(--second)">66</div>' +
      '<div class="colas-rot colas-r2" style="left:' + (picoServicio[0] - 20).toFixed(0) + 'px; top:' + (picoServicio[1] - 96).toFixed(0) + 'px">Cola en servicio</div>' +
      '<div class="colas-pico colas-p2" style="left:' + (picoServicio[0] - 20).toFixed(0) + 'px; top:' + (picoServicio[1] - 54).toFixed(0) + 'px; color:var(--marca)">131</div>' +
      '<div class="colas-hora" style="left:284px; top:778px">12:00</div>' +
      '<div class="colas-hora" style="left:812px; top:778px">13:00</div>' +
      '<div class="colas-hora" style="left:1340px; top:778px">14:00</div>' +
      '<div class="pendiente colas-nota" style="position:absolute; right:300px; top:188px">ESQUEMA &middot; REEMPLAZAR POR EL DASHBOARD</div>' +
      '<div class="words colas-words" style="left:300px; bottom:52px; width:1340px">' +
      '<h2 class="line">El cuello de botella no est&aacute; en la caja, est&aacute; en el mostrador</h2></div></div>'));
    const q = (s) => kit.stage.querySelector(s);
    Object.assign(this, {
      grilla: q('.colas-grilla'), chart: q('.colas-chart'), ejes: q('.colas-ejes'),
      caja: q('.colas-caja'), servicio: q('.colas-servicio'), mc: q('.colas-mc'), ms: q('.colas-ms'),
      r1: q('.colas-r1'), p1: q('.colas-p1'), r2: q('.colas-r2'), p2: q('.colas-p2'),
      nota: q('.colas-nota'), velo: q('.colas-velo'), linea: q('.line'),
      horas: Array.from(kit.stage.querySelectorAll('.colas-hora')),
    });
    this.caja.style.strokeDasharray = this.cCaja.largo.toFixed(1);
    this.servicio.style.strokeDasharray = this.cServicio.largo.toFixed(1);
  },
  render(t) {
    const push = eio(seg(t, 0, 20));
    this.grilla.style.transform = 'scale(' + lerp(1, 1.016, push) + ')';
    this.chart.style.transform = 'translateY(' + lerp(0, -14, push) + 'px)';
    this.ejes.style.opacity = eo(seg(t, -0.4, 0.8));
    this.horas.forEach((el, i) => { el.style.opacity = eo(seg(t, 0.3 + i * 0.18, 0.9 + i * 0.18)); });
    this.caja.style.strokeDashoffset = (this.cCaja.largo * (1 - eio(seg(t, 0.6, 4.4)))).toFixed(1);
    this.r1.style.opacity = eo(seg(t, 1.6, 2.2));
    this.p1.style.opacity = eo(seg(t, 2.1, 2.7));
    this.mc.style.opacity = eo(seg(t, 2.1, 2.7));
    this.servicio.style.strokeDashoffset = (this.cServicio.largo * (1 - eio(seg(t, 5.2, 10.4)))).toFixed(1);
    this.r2.style.opacity = eo(seg(t, 6.4, 7));
    const marca = eo(seg(t, 9.4, 10));
    this.p2.style.opacity = marca;
    this.ms.style.opacity = marca;
    this.ms.setAttribute('r', (14 * (1 + 0.5 * Math.exp(-Math.max(0, t - 9.6) * 2) * Math.sin(Math.max(0, t - 9.6) * 7))).toFixed(1));
    this.nota.style.opacity = eo(seg(t, 10.6, 11.4)) * 0.9;
    this.velo.style.opacity = eo(seg(t, 11.4, 12.4));
    TextFx.fadeFromRight(this.linea, t, 12.2, { stagger: 0.14, dur: 0.6, dx: 30 });
  },
});
