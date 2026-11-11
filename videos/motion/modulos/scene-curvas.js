const { seg, eo, eio, lerp } = kit;

// Raciones por franja de 10 minutos, de 12:00 a 14:30. Los dos vectores salen de la validacion de E0.
const REAL = [103.4, 134.9, 124.8, 119.3, 117.8, 104.6, 119.3, 126.9, 119.8, 99, 75.4, 75.6, 72.4, 81.7, 62.4, 8.4];
const MODELO = [100, 109, 132, 126, 115, 98, 118, 136, 123, 94, 94, 68, 87, 70, 49, 3];
const X0 = 300, X1 = 1620, Y0 = 258, Y1 = 762, TOPE = 150;
const serie = (vs) => vs.map((v, i) => [X0 + (X1 - X0) * (i / (vs.length - 1)), Y1 - (Y1 - Y0) * (v / TOPE)]);

kit.scene('curvas', {
  init(kit) {
    const pr = serie(REAL), pm = serie(MODELO);
    this.cReal = W.curva('curvas-real', pr, 'var(--second)', 7);
    this.cModelo = W.curva('curvas-modelo', pm, 'var(--marca)', 7);
    kit.css('.curvas-titulo { font-family:var(--display, var(--sans, system-ui, sans-serif)); font-size:58px; font-weight:700; margin:0; line-height:1.06 }' +
      '.curvas-leyenda { position:absolute; display:flex; align-items:center; gap:14px; font-size:32px; color:var(--second) }' +
      '.curvas-raya { width:46px; height:7px; border-radius:4px; display:block }' +
      '.curvas-hora { position:absolute; font-family:var(--mono, ui-monospace, monospace); font-size:27px; color:var(--tenue) }' +
      '.curvas-stat { position:absolute; display:flex; flex-direction:column; gap:4px }' +
      '.curvas-stat .dato { font-size:52px }');
    kit.stage.append(kit.h('<div class="ground">' +
      '<svg class="art curvas-grilla" viewBox="0 0 1920 1080">' + W.tramas('curvas') + '</svg>' +
      '<svg class="art curvas-chart" viewBox="0 0 1920 1080">' + W.ejes('curvas-ejes', X0, Y0, X1, Y1, 3) +
      this.cReal.markup + this.cModelo.markup + '</svg>' +
      '<div class="words" style="left:300px; top:118px; width:1280px; gap:8px">' +
      '<h2 class="curvas-titulo">Las raciones del modelo contra los registros reales</h2>' +
      '<p class="sub curvas-sub">Por franja de 10 minutos, de 12:00 a 14:30</p></div>' +
      '<div class="curvas-leyenda curvas-l1" style="left:1150px; top:800px"><span class="curvas-raya" style="background:var(--second)"></span>Registros reales</div>' +
      '<div class="curvas-leyenda curvas-l2" style="left:1150px; top:852px"><span class="curvas-raya" style="background:var(--marca)"></span>Modelo</div>' +
      '<div class="curvas-hora" style="left:284px; top:784px">12:00</div>' +
      '<div class="curvas-hora" style="left:812px; top:784px">13:00</div>' +
      '<div class="curvas-hora" style="left:1340px; top:784px">14:00</div>' +
      '<div class="curvas-stat curvas-s1" style="left:300px; top:812px"><span class="rotulo">Correlaci&oacute;n</span><span class="dato">0,95</span></div>' +
      '<div class="curvas-stat curvas-s2" style="left:620px; top:812px"><span class="rotulo">Diferencia en el total</span><span class="dato">-1,5 %</span></div></div>'));
    const q = (s) => kit.stage.querySelector(s);
    Object.assign(this, {
      grilla: q('.curvas-grilla'), chart: q('.curvas-chart'), ejes: q('.curvas-ejes'),
      real: q('.curvas-real'), modelo: q('.curvas-modelo'), titulo: q('.curvas-titulo'), sub: q('.curvas-sub'),
      l1: q('.curvas-l1'), l2: q('.curvas-l2'), s1: q('.curvas-s1'), s2: q('.curvas-s2'),
      horas: Array.from(kit.stage.querySelectorAll('.curvas-hora')),
    });
    this.real.style.strokeDasharray = this.cReal.largo.toFixed(1);
    this.modelo.style.strokeDasharray = this.cModelo.largo.toFixed(1);
  },
  render(t) {
    const push = eio(seg(t, 0, 14));
    this.grilla.style.transform = 'scale(' + lerp(1, 1.014, push) + ')';
    this.chart.style.transform = 'translateY(' + lerp(0, -12, push) + 'px)';
    this.titulo.style.opacity = eo(seg(t, -0.3, 0.6));
    this.sub.style.opacity = eo(seg(t, 0.6, 1.2));
    this.ejes.style.opacity = eo(seg(t, 0.2, 1));
    this.horas.forEach((el, i) => { el.style.opacity = eo(seg(t, 0.6 + i * 0.16, 1.2 + i * 0.16)); });
    this.real.style.strokeDashoffset = (this.cReal.largo * (1 - eio(seg(t, 1, 4.4)))).toFixed(1);
    this.l1.style.opacity = eo(seg(t, 2.2, 2.8));
    this.modelo.style.strokeDashoffset = (this.cModelo.largo * (1 - eio(seg(t, 4.8, 8.2)))).toFixed(1);
    this.l2.style.opacity = eo(seg(t, 5.8, 6.4));
    [this.s1, this.s2].forEach((el, i) => {
      const a = eo(seg(t, 8.8 + i * 0.7, 9.4 + i * 0.7));
      el.style.opacity = a;
      el.style.transform = 'translateY(' + lerp(20, 0, a) + 'px)';
    });
  },
});
