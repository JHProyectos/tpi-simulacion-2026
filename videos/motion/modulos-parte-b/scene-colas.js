const { seg, eo, eio, lerp, TextFx } = kit;

// Segunda mitad de la escena 6: las dos colas del dia, una contra otra.
// Con los 30 replicas del Experimenter la caja se llena y el mostrador no: 71 contra 5.
const X0 = 300, X1 = 1620, Y0 = 250, Y1 = 744, TOPE = 80;
const CAJA = [4, 58, 71, 69, 66, 68, 71, 64, 52, 34, 20, 11, 6, 3, 1, 0];
const MOSTRADOR = [0, 2, 4, 5, 4, 3, 4, 5, 4, 3, 2, 2, 1, 1, 0, 0];
const punto = (v, i, n) => [X0 + (X1 - X0) * (i / (n - 1)), Y1 - (Y1 - Y0) * (v / TOPE)];
const serie = (vs) => vs.map((v, i) => punto(v, i, vs.length));
// El dia va de 11:40 a 16:00: 260 minutos sobre el ancho del eje.
const enHora = (h, m) => X0 + (X1 - X0) * ((h * 60 + m - 700) / 260);
const HORAS = [[12, 0], [13, 0], [14, 0], [15, 0]];

kit.scene('colas', {
  init(kit) {
    const pc = serie(CAJA), pm = serie(MOSTRADOR);
    this.cCaja = W.curva('colas-caja', pc, 'var(--marca)', 9);
    this.cMostrador = W.curva('colas-mostrador', pm, 'var(--main)', 7);
    const picoCaja = pc[2], picoMostrador = pm[3];
    kit.css('.colas-rot { position:absolute; font-size:32px; color:var(--second) }' +
      '.colas-hora { position:absolute; font-family:var(--mono, ui-monospace, monospace); font-size:27px; color:var(--tenue) }' +
      '.colas-pico { position:absolute; font-family:var(--mono, ui-monospace, monospace); font-variant-numeric:tabular-nums; font-size:54px; font-weight:700; line-height:1 }' +
      '.colas-titulo { position:absolute; left:300px; top:138px; font-family:var(--display, var(--sans, system-ui, sans-serif)); font-size:52px; font-weight:700; margin:0 }' +
      '.colas-words .line { font-size:70px }' +
      '.colas-velo { position:absolute; left:0; bottom:0; right:0; height:36%; background:linear-gradient(transparent, color-mix(in srgb, var(--ground) 94%, transparent) 46%) }');
    kit.stage.append(kit.h('<div class="ground">' + W.logo(kit) +
      '<svg class="art colas-grilla" viewBox="0 0 1920 1080">' + W.tramas('colas') + '</svg>' +
      '<svg class="art colas-chart" viewBox="0 0 1920 1080">' + W.ejes('colas-ejes', X0, Y0, X1, Y1, 4) +
      this.cMostrador.markup + this.cCaja.markup +
      '<circle class="colas-mc" cx="' + picoCaja[0].toFixed(1) + '" cy="' + picoCaja[1].toFixed(1) + '" r="14" style="fill:var(--marca)"/>' +
      '<circle class="colas-ms" cx="' + picoMostrador[0].toFixed(1) + '" cy="' + picoMostrador[1].toFixed(1) + '" r="12" style="fill:var(--main)"/></svg>' +
      '<div class="colas-velo"></div>' +
      '<h2 class="colas-titulo">Cu&aacute;nta gente espera, hora por hora</h2>' +
      '<div class="colas-rot colas-r1" style="left:' + (picoCaja[0] + 34).toFixed(0) + 'px; top:' + (picoCaja[1] - 10).toFixed(0) + 'px">Cola en la caja</div>' +
      '<div class="colas-pico colas-p1" style="left:' + (picoCaja[0] + 34).toFixed(0) + 'px; top:' + (picoCaja[1] - 76).toFixed(0) + 'px; color:var(--marca)">71</div>' +
      '<div class="colas-rot colas-r2" style="left:' + (picoMostrador[0] + 34).toFixed(0) + 'px; top:' + (picoMostrador[1] - 8).toFixed(0) + 'px">Cola en el mostrador</div>' +
      '<div class="colas-pico colas-p2" style="left:' + (picoMostrador[0] + 34).toFixed(0) + 'px; top:' + (picoMostrador[1] - 74).toFixed(0) + 'px; color:var(--main)">5</div>' +
      HORAS.map((h) => '<div class="colas-hora" style="left:' + (enHora(h[0], h[1]) - 40).toFixed(0) + 'px; top:764px">' + String(h[0]).padStart(2, '0') + ':' + String(h[1]).padStart(2, '0') + '</div>').join('') +
      '<div class="words colas-words" style="left:300px; bottom:60px; width:1360px">' +
      '<h2 class="line">La cola se hace en la caja. El mostrador no se llena.</h2></div></div>'));
    const q = (s) => kit.stage.querySelector(s);
    Object.assign(this, {
      grilla: q('.colas-grilla'), chart: q('.colas-chart'), ejes: q('.colas-ejes'), titulo: q('.colas-titulo'),
      caja: q('.colas-caja'), mostrador: q('.colas-mostrador'), mc: q('.colas-mc'), ms: q('.colas-ms'),
      r1: q('.colas-r1'), p1: q('.colas-p1'), r2: q('.colas-r2'), p2: q('.colas-p2'),
      velo: q('.colas-velo'), linea: q('.line'),
      horas: Array.from(kit.stage.querySelectorAll('.colas-hora')),
    });
    this.caja.style.strokeDasharray = this.cCaja.largo.toFixed(1);
    this.mostrador.style.strokeDasharray = this.cMostrador.largo.toFixed(1);
  },
  render(t) {
    const push = eio(seg(t, 0, 11));
    this.grilla.style.transform = 'scale(' + lerp(1, 1.016, push) + ')';
    this.chart.style.transform = 'translateY(' + lerp(0, -12, push) + 'px)';
    this.titulo.style.opacity = eo(seg(t, -0.3, 0.7));
    this.ejes.style.opacity = eo(seg(t, -0.2, 0.8));
    this.horas.forEach((el, i) => { el.style.opacity = eo(seg(t, 0.3 + i * 0.16, 0.9 + i * 0.16)); });
    this.caja.style.strokeDashoffset = (this.cCaja.largo * (1 - eio(seg(t, 0.5, 3.2)))).toFixed(1);
    this.r1.style.opacity = eo(seg(t, 1.7, 2.3));
    const marcaCaja = eo(seg(t, 2.4, 3.0));
    this.p1.style.opacity = marcaCaja;
    this.mc.style.opacity = marcaCaja;
    this.mc.setAttribute('r', (14 * (1 + 0.5 * Math.exp(-Math.max(0, t - 2.6) * 2) * Math.sin(Math.max(0, t - 2.6) * 7))).toFixed(1));
    this.mostrador.style.strokeDashoffset = (this.cMostrador.largo * (1 - eio(seg(t, 3.6, 6.6)))).toFixed(1);
    this.r2.style.opacity = eo(seg(t, 5.0, 5.6));
    const marcaMost = eo(seg(t, 6.2, 6.8));
    this.p2.style.opacity = marcaMost;
    this.ms.style.opacity = marcaMost;
    this.velo.style.opacity = eo(seg(t, 7.6, 8.4));
    TextFx.fadeFromRight(this.linea, t, 8.4, { stagger: 0.12, dur: 0.6, dx: 30 });
  },
});
