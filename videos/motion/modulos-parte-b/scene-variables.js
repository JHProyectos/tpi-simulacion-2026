const { seg, eo, eio, lerp } = kit;

// Las cuatro variables aleatorias del modelo, una por renglon: que es, de donde
// sale y con que forma se sortea. Sale de la seccion 7.3 de
// entregas/entrega-final/INFORME.md. Los segundos salen de la transcripcion por
// palabra de videos/audios/jonatan/jonatan-e11-distribuciones.wav.
// t es [entra, dato, forma]: el segundo en que la voz nombra cada parte del renglon.
const VARIABLES = [
  { fig: 'curva', rotulo: 'Validaci&oacute;n del DNI', que: 'Lo que tarda el puesto con cada persona', dato: 'algo m&aacute;s de 3 s', forma: 'Lognormal', fuente: 'registros del puesto', supuesto: false, t: [4.2, 8.9, 13.8] },
  { fig: 'dias', rotulo: 'Apertura de la caja', que: 'La demora con que abre, respecto de las 12:00', dato: '2 min de media, hasta 7', forma: 'Emp&iacute;rica', fuente: '32 d&iacute;as anotados', supuesto: false, t: [16, 22.8, 20.2] },
  { fig: 'raciones', rotulo: 'Raciones por persona', que: 'Cu&aacute;ntas retira cada uno al llegar al mostrador', dato: 'seg&uacute;n la beca', forma: 'Por tipo de cliente', fuente: 'registros de reservas', supuesto: false, t: [26.5, 28.7, 28.7] },
  { fig: 'cola', rotulo: 'Cola antes de abrir', que: 'Cu&aacute;nta gente ya est&aacute; esperando a las 11:40', dato: '60 a 70 personas', forma: 'Ajustada por nosotros', fuente: 'supuesto declarado', supuesto: true, t: [30.3, 33.1, 34.3] },
];

// Las cuatro miniaturas, dibujadas una sola vez. Ninguna lleva texto: los rotulos van en HTML.
function miniatura(kit, clase) {
  if (clase === 'curva') {
    return '<path d="M8 86 C 32 86, 38 16, 64 16 S 112 60, 152 74 S 202 86, 222 88" style="fill:none;stroke:var(--linea);stroke-width:3;stroke-linecap:round"/>' +
      '<path d="M8 90 H222" style="fill:none;stroke:var(--borde);stroke-width:2"/>';
  }
  if (clase === 'dias') {
    const r = kit.rng('variables-dias');
    let s = '';
    for (let i = 0; i < 32; i++) {
      const h = 14 + r() * 62, x = 10 + i * 6.7;
      s += '<path d="M' + x.toFixed(1) + ' 88 V' + (88 - h).toFixed(1) + '" style="fill:none;stroke:var(--linea);stroke-width:4;stroke-linecap:round"/>';
    }
    return s + '<path d="M6 90 H224" style="fill:none;stroke:var(--borde);stroke-width:2"/>';
  }
  if (clase === 'raciones') {
    return [60, 118, 176].map((w, i) => '<rect x="10" y="' + (16 + i * 28) + '" width="' + w + '" height="18" rx="4" style="fill:var(--linea)"/>').join('');
  }
  let s = '<rect x="6" y="26" width="218" height="44" rx="8" style="fill:none;stroke:var(--marca);stroke-width:3;stroke-dasharray:10 9"/>';
  for (let i = 0; i < 8; i++) s += '<circle cx="' + (26 + i * 25) + '" cy="48" r="8" style="fill:var(--marca)"/>';
  return s;
}

kit.scene('variables', {
  init(kit) {
    kit.css('.variables-titulo { font-family:var(--display, var(--sans, system-ui, sans-serif)); font-size:64px; font-weight:700; margin:0; line-height:1.06; color:var(--tinta) }' +
      '.variables-fila { position:absolute; left:200px; width:1520px; box-sizing:border-box; display:flex; align-items:center; gap:40px; padding:22px 0; border-top:1px solid var(--borde) }' +
      '.variables-fig { width:230px; height:96px; flex:none; overflow:visible }' +
      '.variables-texto { flex:1; display:flex; flex-direction:column; gap:7px }' +
      '.variables-rotulo { font-size:36px; font-weight:700; color:var(--tinta) }' +
      '.variables-que { font-size:27px; color:var(--tenue); line-height:1.25 }' +
      '.variables-col { width:430px; flex:none; display:flex; flex-direction:column; align-items:flex-end; gap:7px; text-align:right }' +
      '.variables-dato { font-family:var(--mono, ui-monospace, monospace); font-variant-numeric:tabular-nums; font-size:40px; font-weight:700; color:var(--tinta); line-height:1.05 }' +
      '.variables-forma { font-family:var(--mono, ui-monospace, monospace); font-size:26px; letter-spacing:.05em; color:var(--tenue) }' +
      '.variables-forma.es-supuesto { color:var(--marca-texto) }');
    const filas = VARIABLES.map((v, i) => '<div class="variables-fila" style="top:' + (296 + i * 172) + 'px">' +
      '<svg class="variables-fig" viewBox="0 0 230 96">' + miniatura(kit, v.fig) + '</svg>' +
      '<div class="variables-texto"><span class="variables-rotulo">' + v.rotulo + '</span>' +
      '<span class="variables-que">' + v.que + '</span></div>' +
      '<div class="variables-col"><span class="variables-dato">' + v.dato + '</span>' +
      '<span class="variables-forma' + (v.supuesto ? ' es-supuesto' : '') + '">' + v.forma + ' &middot; ' + v.fuente + '</span></div></div>').join('');
    kit.stage.append(kit.h('<div class="ground">' + W.logo(kit) +
      '<svg class="art variables-grilla" viewBox="0 0 1920 1080">' + W.tramas('variables') + '</svg>' +
      '<div class="edge"></div>' +
      '<div class="words variables-cab" style="left:200px; top:132px; width:1320px; gap:12px">' +
      '<h2 class="variables-titulo">Cuatro cosas que cambian de persona a persona</h2>' +
      '<p class="sub variables-sub">Las variables aleatorias del modelo: tres salen de registros, una queda declarada como supuesto.</p></div>' +
      filas + '</div>'));
    const q = (s) => kit.stage.querySelector(s);
    this.grilla = q('.variables-grilla');
    this.titulo = q('.variables-titulo');
    this.sub = q('.variables-sub');
    this.filas = Array.from(kit.stage.querySelectorAll('.variables-fila'));
    this.figuras = this.filas.map((el) => el.querySelector('.variables-fig'));
    this.datos = this.filas.map((el) => el.querySelector('.variables-dato'));
    this.formas = this.filas.map((el) => el.querySelector('.variables-forma'));
  },
  render(t) {
    const push = eio(seg(t, 0, 38));
    this.grilla.style.transform = 'scale(' + lerp(1, 1.018, push) + ')';
    this.titulo.style.opacity = eo(seg(t, 0.5, 1.5));
    this.sub.style.opacity = eo(seg(t, 2.2, 3.2));
    VARIABLES.forEach((v, i) => {
      const a = eo(seg(t, v.t[0], v.t[0] + 0.6));
      this.filas[i].style.opacity = a;
      this.filas[i].style.transform = 'translateY(' + lerp(24, 0, a) + 'px)';
      const dibuja = eio(seg(t, v.t[0] + 0.3, v.t[0] + 1.3));
      this.figuras[i].style.opacity = dibuja;
      this.figuras[i].style.transform = 'scale(' + lerp(0.94, 1, dibuja).toFixed(3) + ')';
      this.datos[i].style.opacity = eo(seg(t, v.t[1], v.t[1] + 0.5));
      this.formas[i].style.opacity = eo(seg(t, v.t[2], v.t[2] + 0.5));
    });
  },
});
