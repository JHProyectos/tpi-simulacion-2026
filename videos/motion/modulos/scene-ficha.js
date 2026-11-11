const { seg, eo, eio, lerp, TextFx } = kit;

// Cada renglon de la ficha: el segundo en que Jonatan lo dice, el rotulo, el valor
// y, si el dato todavia no esta cerrado, su marca de pendiente.
// Los segundos salen de la transcripcion por palabra de videos/audios/jonatan/jonatan-e03.wav.
const FILAS = [
  [6.8, 'Apertura de la caja', '~12:00', 'demora media de 1,9 min'],
  [10.2, 'Empieza la fila', '11:40', 'supuesto declarado'],
  [33.3, 'Llegadas', 'cada 10 min', 'registros de reservas, por tipo de cliente'],
  [38.7, 'Puestos de validaci&oacute;n', '1', ''],
  [43.4, 'Tiempo por DNI', '4 s', 'registros del puesto'],
  [51.6, 'Personas sirviendo', '3', 'una atiende el men&uacute; vegetariano'],
  [53.9, 'Tiempo por raci&oacute;n', '17 s', 'supuesto declarado'],
];

kit.scene('ficha', {
  init(kit) {
    kit.css('.ficha-caja { position:absolute; left:1138px; top:124px; width:650px }' +
      '.ficha-titulo { font-family:var(--display, var(--sans, system-ui, sans-serif)); font-size:62px; font-weight:700; line-height:1.08; margin:0; color:var(--tinta) }' +
      '.ficha-fila { display:flex; justify-content:space-between; align-items:flex-start; gap:36px; padding:15px 0; border-top:1px solid var(--borde) }' +
      '.ficha-col { display:flex; flex-direction:column; align-items:flex-end; gap:5px }' +
      '.ficha-valor { font-family:var(--mono, ui-monospace, monospace); font-variant-numeric:tabular-nums; font-size:40px; font-weight:700; line-height:1.1; text-align:right; color:var(--tinta) }' +
      '.ficha-nota { font-size:23px; color:var(--tenue); text-align:right }' +
      '.ficha-planta { transform-origin:center }' +
      '.ficha-pie { position:absolute; left:150px; top:900px }');
    const filas = FILAS.map((f) => '<div class="ficha-fila"><span class="rotulo">' + f[1] + '</span>' +
      '<span class="ficha-col"><span class="ficha-valor">' + f[2] + '</span>' +
      (f[3] ? '<span class="' + (f[3] === 'A CONFIRMAR' ? 'pendiente' : 'ficha-nota') + '">' + f[3] + '</span>' : '') + '</span></div>').join('');
    kit.stage.append(kit.h('<div class="ground">' + W.logo(kit) +
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
  },
  render(t) {
    const push = eio(seg(t, 0, 72));
    this.grilla.style.transform = 'scale(' + lerp(1.02, 1.04, push) + ')';
    const entra = eo(seg(t, 0, 1.1));
    this.planta.style.opacity = entra;
    this.planta.style.transform = 'scale(' + lerp(0.965, 1.02, push).toFixed(4) + ') translateY(' + lerp(18, 0, entra).toFixed(1) + 'px)';
    this.pie.style.opacity = eo(seg(t, 1.4, 2.1)) * 0.9;
    this.titulo.style.opacity = eo(seg(t, 0.6, 1.3));
    this.sub.style.opacity = eo(seg(t, 2.6, 3.4));
    this.filas.forEach((el, i) => {
      const a = eo(seg(t, FILAS[i][0], FILAS[i][0] + 0.6));
      el.style.opacity = a;
      el.style.transform = 'translateX(' + lerp(34, 0, a) + 'px)';
    });
  },
});
