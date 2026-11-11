const { seg, eo, eio, lerp, TextFx } = kit;

// El armazon de la comparacion. Las barras quedan vacias a proposito: no hay resultados que poner todavia.
const FILAS = ['E0 base', 'E1', 'E2', 'E3', 'E4', 'E5'];

kit.scene('comparar', {
  init(kit) {
    kit.css('.comparar-titulo { font-family:var(--display, var(--sans, system-ui, sans-serif)); font-size:62px; font-weight:700; margin:0; line-height:1.06 }' +
      '.comparar-fila { position:absolute; left:300px; width:1320px; display:flex; align-items:center; gap:28px }' +
      '.comparar-cod { font-family:var(--mono, ui-monospace, monospace); font-size:36px; font-weight:700; min-width:168px; flex:none }' +
      '.comparar-pista { flex:1; height:62px; box-sizing:border-box; border:2px dashed var(--borde); border-radius:8px; display:flex; align-items:center; padding-left:26px; transform-origin:left center }' +
      '.comparar-falta { font-family:var(--mono, ui-monospace, monospace); font-size:24px; letter-spacing:.1em; color:var(--marca) }' +
      '.comparar-plano { transform-origin:960px 540px; opacity:.14 }' +
      '.comparar-words .line { font-size:46px; font-weight:600 }');
    const filas = FILAS.map((f, i) => '<div class="comparar-fila" style="top:' + (336 + i * 92) + 'px">' +
      '<span class="comparar-cod" style="color:' + (i ? 'var(--second)' : 'var(--marca)') + '">' + f + '</span>' +
      '<span class="comparar-pista"><span class="comparar-falta">SIN MEDIR</span></span></div>').join('');
    kit.stage.append(kit.h('<div class="ground">' +
      W.foto(kit, 'amb-bandejas.webp', 'ambiente', 'left:0; top:0; width:1920px; height:1080px') +
      '<svg class="art comparar-grilla" viewBox="0 0 1920 1080">' + W.tramas('comparar') + '</svg>' +
      '<svg class="art comparar-plano" viewBox="0 0 1920 1080">' + '' + '</svg>' +
      '<div class="edge"></div>' +
      '<div class="words" style="left:300px; top:164px; width:1300px; gap:8px">' +
      '<h2 class="comparar-titulo">Los seis escenarios, uno al lado del otro</h2>' +
      '<p class="sub comparar-sub">Tiempo total medio, con su intervalo de confianza del 95 %</p></div>' +
      filas +
      '<div class="words comparar-words" style="left:300px; top:916px; width:1320px">' +
      '<h2 class="line">Cada barra se completa cuando corran los seis escenarios con 30 r&eacute;plicas</h2></div></div>'));
    const q = (s) => kit.stage.querySelector(s);
    this.grilla = q('.comparar-grilla');
    this.plano = q('.comparar-plano');
    this.titulo = q('.comparar-titulo');
    this.sub = q('.comparar-sub');
    this.linea = q('.comparar-words .line');
    this.filas = Array.from(kit.stage.querySelectorAll('.comparar-fila'));
    this.pistas = this.filas.map((el) => el.querySelector('.comparar-pista'));
    this.faltas = this.filas.map((el) => el.querySelector('.comparar-falta'));
    this.t0 = 1.5;
    this.paso = 1.3;
  },
  render(t) {
    const push = eio(seg(t, 0, 24));
    this.grilla.style.transform = 'scale(' + lerp(1, 1.018, push) + ')';
    this.plano.style.transform = 'scale(' + lerp(1, 1.05, push) + ')';
    this.titulo.style.opacity = eo(seg(t, -0.3, 0.6));
    this.sub.style.opacity = eo(seg(t, 0.7, 1.3));
    this.filas.forEach((el, i) => {
      const t0 = this.t0 + i * this.paso, a = eo(seg(t, t0, t0 + 0.5));
      el.style.opacity = a;
      this.pistas[i].style.transform = 'scaleX(' + eio(seg(t, t0, t0 + 0.9)).toFixed(3) + ')';
      this.faltas[i].style.opacity = eo(seg(t, t0 + 0.8, t0 + 1.3)) * (0.6 + 0.24 * Math.sin((t - t0) * 1.4));
    });
    TextFx.fadeFromRight(this.linea, t, 11.4, { stagger: 0.1, dur: 0.55, dx: 24 });
  },
});
