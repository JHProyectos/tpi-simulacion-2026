const { seg, eo, eio, lerp, TextFx } = kit;

// Cada renglon de la ficha: rotulo, valor y, si el dato todavia no esta cerrado, su marca de pendiente.
const FILAS = [
  ['Llegadas', '11:40 a 14:30', 'registros reales, franjas de 10 min'],
  ['Apertura de la caja', '~12:00', 'demora media de 1,9 min'],
  ['Puestos de validaci&oacute;n', '1', ''],
  ['Tiempo por DNI', '4 s', ''],
  ['Personas sirviendo', '3', ''],
  ['Tiempo por raci&oacute;n', '17 s', 'supuesto declarado'],
];

kit.scene('ficha', {
  init(kit) {
    kit.css('.ficha-caja { position:absolute; left:1138px; top:150px; width:650px }' +
      '.ficha-titulo { font-family:var(--display, var(--sans, system-ui, sans-serif)); font-size:62px; font-weight:700; line-height:1.08; margin:0 }' +
      '.ficha-fila { display:flex; justify-content:space-between; align-items:flex-start; gap:36px; padding:17px 0; border-top:1px solid var(--borde) }' +
      '.ficha-col { display:flex; flex-direction:column; align-items:flex-end; gap:5px }' +
      '.ficha-valor { font-family:var(--mono, ui-monospace, monospace); font-variant-numeric:tabular-nums; font-size:42px; font-weight:700; line-height:1.1; text-align:right }' +
      '.ficha-nota { font-size:24px; color:var(--tenue); text-align:right }' +
      '.ficha-planta { transform-origin:center }' +
      '.ficha-pie { position:absolute; left:150px; top:900px }');
    const filas = FILAS.map((f) => '<div class="ficha-fila"><span class="rotulo">' + f[0] + '</span>' +
      '<span class="ficha-col"><span class="ficha-valor">' + f[1] + '</span>' +
      (f[2] ? '<span class="' + (f[2] === 'A CONFIRMAR' ? 'pendiente' : 'ficha-nota') + '">' + f[2] + '</span>' : '') + '</span></div>').join('');
    kit.stage.append(kit.h('<div class="ground">' +
      '<svg class="art ficha-grilla" viewBox="0 0 1920 1080">' + W.tramas('ficha') + '</svg>' +
      W.foto(kit, 'planta.webp', 'ficha-planta marco', 'left:150px; top:214px; width:760px; height:664px') +
      '<div class="edge"></div>' +
      '<div class="etiqueta ficha-pie">Planta del modelo, vista desde arriba</div>' +
      '<div class="words ficha-caja" style="gap:14px">' +
      '<h2 class="ficha-titulo">Escenario base</h2>' +
      '<p class="sub ficha-sub">Caso mixto: las llegadas y la validaci&oacute;n salen de registros reales; el resto queda declarado como supuesto.</p>' +
      '<div class="ficha-filas">' + filas + '</div></div></div>'));
    const q = (s) => kit.stage.querySelector(s);
    this.grilla = q('.ficha-grilla');
    this.planta = q('.ficha-planta');
    this.pie = q('.ficha-pie');
    this.titulo = q('.ficha-titulo');
    this.sub = q('.ficha-sub');
    this.filas = Array.from(kit.stage.querySelectorAll('.ficha-fila'));
    this.t0 = 2.2;
    this.paso = 2.1;
  },
  render(t) {
    const push = eio(seg(t, 0, 22));
    this.grilla.style.transform = 'scale(' + lerp(1.02, 1.04, push) + ')';
    const entra = eo(seg(t, 0, 1.1));
    this.planta.style.opacity = entra;
    this.planta.style.transform = 'scale(' + lerp(0.965, 1.02, push).toFixed(4) + ') translateY(' + lerp(18, 0, entra).toFixed(1) + 'px)';
    this.pie.style.opacity = eo(seg(t, 1.4, 2.1)) * 0.9;
    this.titulo.style.opacity = eo(seg(t, 0.2, 0.9));
    this.sub.style.opacity = eo(seg(t, 1, 1.7));
    this.filas.forEach((el, i) => {
      const a = eo(seg(t, this.t0 + i * this.paso, this.t0 + i * this.paso + 0.6));
      el.style.opacity = a;
      el.style.transform = 'translateX(' + lerp(34, 0, a) + 'px)';
    });
  },
});
