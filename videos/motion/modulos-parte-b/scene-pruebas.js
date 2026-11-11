const { seg, eo, eio, lerp } = kit;

// Verificacion y validacion, una al lado de la otra, y abajo por que alcanzan 30
// replicas. Sale de la seccion 9 de entregas/entrega-final/INFORME.md. Los
// segundos salen de la transcripcion por palabra de
// videos/audios/jonatan/jonatan-e12-verificacion.wav.
const COLUMNAS = [
  {
    clase: 'verificacion', x: 180, cabecera: 'Verificaci&oacute;n', pregunta: '&iquest;El modelo hace lo que dise&ntilde;amos?',
    t: [1.5, 2.4],
    filas: [[4.2, 'Secuencia de tiempos', 'en orden'], [5.5, 'Raciones del d&iacute;a', '1.369 vs 1.381'], [10.1, 'Al cerrar el turno', '0 en las filas']],
  },
  {
    clase: 'validacion', x: 990, cabecera: 'Validaci&oacute;n', pregunta: '&iquest;Se parece al comedor real?',
    t: [12.9, 13.7],
    filas: [[15.7, 'Correlaci&oacute;n en la curva de raciones', '0,95'], [19.4, 'Diferencia en el total', '1,5 %'], [22.1, 'Cola m&aacute;xima en la caja', '66 vs 60 a 70']],
  },
];
// La franja de abajo: por que una corrida de un dia alcanza y por que son 30.
const CHIPS = [[29, 'Simulaci&oacute;n terminante'], [31.3, 'Cada r&eacute;plica arranca vac&iacute;a'], [34.2, 'Sin calentamiento'], [36.4, '30 r&eacute;plicas por escenario'], [39.5, 'Intervalos al 95 %']];

kit.scene('pruebas', {
  init(kit) {
    kit.css('.pruebas-titulo { font-family:var(--display, var(--sans, system-ui, sans-serif)); font-size:64px; font-weight:700; margin:0; line-height:1.06; color:var(--tinta) }' +
      '.pruebas-col { position:absolute; top:296px; width:750px; box-sizing:border-box; background:var(--panel); border:1px solid var(--borde); border-radius:12px; padding:34px 40px 40px }' +
      '.pruebas-cabecera { font-family:var(--display, var(--sans, system-ui, sans-serif)); font-size:52px; font-weight:700; margin:0; line-height:1.06; color:var(--tinta) }' +
      '.pruebas-pregunta { font-size:30px; color:var(--tenue); margin:10px 0 18px; line-height:1.25 }' +
      '.pruebas-fila { display:flex; justify-content:space-between; align-items:baseline; gap:28px; padding:20px 0; border-top:1px solid var(--borde) }' +
      '.pruebas-valor { font-family:var(--mono, ui-monospace, monospace); font-variant-numeric:tabular-nums; font-size:42px; font-weight:700; color:var(--tinta); line-height:1; text-align:right; white-space:nowrap }' +
      '.pruebas-franja { position:absolute; left:180px; top:884px; width:1560px; display:flex; gap:20px; align-items:center }' +
      '.pruebas-franja .etiqueta { position:static }');
    const cols = COLUMNAS.map((c) => '<div class="pruebas-col pruebas-' + c.clase + '" style="left:' + c.x + 'px">' +
      '<h3 class="pruebas-cabecera">' + c.cabecera + '</h3>' +
      '<p class="pruebas-pregunta">' + c.pregunta + '</p>' +
      c.filas.map((f) => '<div class="pruebas-fila"><span class="rotulo">' + f[1] + '</span>' +
        '<span class="pruebas-valor">' + f[2] + '</span></div>').join('') + '</div>').join('');
    kit.stage.append(kit.h('<div class="ground">' + W.logo(kit) +
      '<svg class="art pruebas-grilla" viewBox="0 0 1920 1080">' + W.tramas('pruebas') + '</svg>' +
      '<div class="edge"></div>' +
      '<div class="words pruebas-cab" style="left:180px; top:138px; width:1320px; gap:12px">' +
      '<h2 class="pruebas-titulo">Dos pruebas distintas</h2>' +
      '<p class="sub pruebas-sub">Una mira el modelo contra lo que dise&ntilde;amos; la otra, contra el comedor.</p></div>' +
      cols +
      '<div class="pruebas-franja">' + CHIPS.map((c) => '<span class="etiqueta">' + c[1] + '</span>').join('') + '</div></div>'));
    const q = (s) => kit.stage.querySelector(s);
    this.grilla = q('.pruebas-grilla');
    this.titulo = q('.pruebas-titulo');
    this.sub = q('.pruebas-sub');
    this.cols = COLUMNAS.map((c) => kit.stage.querySelector('.pruebas-' + c.clase));
    this.cabeceras = this.cols.map((el) => el.querySelector('.pruebas-cabecera'));
    this.preguntas = this.cols.map((el) => el.querySelector('.pruebas-pregunta'));
    this.filas = this.cols.map((el) => Array.from(el.querySelectorAll('.pruebas-fila')));
    this.chips = Array.from(kit.stage.querySelectorAll('.pruebas-franja .etiqueta'));
  },
  render(t) {
    const push = eio(seg(t, 0, 41));
    this.grilla.style.transform = 'scale(' + lerp(1, 1.018, push) + ')';
    this.titulo.style.opacity = eo(seg(t, 0, 0.8));
    this.sub.style.opacity = eo(seg(t, 0.8, 1.6));
    COLUMNAS.forEach((c, i) => {
      const a = eo(seg(t, c.t[0], c.t[0] + 0.7));
      this.cols[i].style.opacity = a;
      this.cols[i].style.transform = 'translateY(' + lerp(26, 0, a) + 'px)';
      this.preguntas[i].style.opacity = eo(seg(t, c.t[1], c.t[1] + 0.6));
      c.filas.forEach((f, j) => {
        const b = eo(seg(t, f[0], f[0] + 0.55));
        this.filas[i][j].style.opacity = b;
        this.filas[i][j].style.transform = 'translateX(' + lerp(24, 0, b) + 'px)';
      });
    });
    CHIPS.forEach((c, i) => {
      const a = eo(seg(t, c[0], c[0] + 0.6));
      this.chips[i].style.opacity = a * 0.95;
      this.chips[i].style.transform = 'translateY(' + lerp(14, 0, a) + 'px)';
    });
  },
});
