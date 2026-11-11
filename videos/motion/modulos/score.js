// Musica original, tranquila: un aire que cambia por escena, y sonidos puntuales en cada entrada.
// Parte A del video (escenas 0 a 3 del guion): apertura, recorrido, pregunta y ficha del modelo.
kit.score(function (S, T) {
  const B = 60 / 84;
  S.tempo(84, { t0: 0 });
  S.program('pad', 'pad', { rev: 0.7, gain: -5 });
  S.program('vibes', 'vibes', { rev: 0.45, gain: -4 });
  S.program('bajo', 'bass', { gain: -4 });
  S.program('pluck', 'pluck', { rev: 0.3, gain: -5 });

  // Un acorde largo por escena: el aire cambia cuando cambia el tema.
  const AIRE = [
    [T.abrir, 16, ['D3', 'A3', 'E4']],
    [T.recorrido, 29, ['D3', 'A3', 'F4']],
    [T.pregunta, 34, ['Bb2', 'F3', 'D4']],
    [T.ficha, 72, ['D3', 'A3', 'E4']],
  ];
  AIRE.forEach(function (a, i) { S.chord('pad', a[2], { t: a[0], dur: a[1] + 1.4, vel: 30 + i * 4 }); });
  S.note('bajo', 'Bb1', { t: T.pregunta, dur: 12, vel: 36 });
  S.note('bajo', 'D2', { t: T.ficha, dur: 16, vel: 38 });

  // La apertura: tildes muy suaves sobre el dibujo en lineas y un swell cuando entra el color.
  S.ticks([0.2, 0.45, 0.7, 0.95, 1.2, 1.45, 3.1, 4.9, 6.8, 8.6], { vel: 22 });
  S.fx('revswell', 11.4, { dur: 1.6, vel: 44 });
  S.fx('chime', 13, { vel: 48 });

  // El recorrido: la persona camina y cada rotulo entra con un pop.
  S.run('pluck', ['D4', 'F4', 'A4', 'D5', 'A4', 'F4'], { t: T.recorrido + 13.5, step: 1, vel: 38 });
  [13.4, 16, 19.1].forEach(function (d) { S.fx('pop', T.recorrido + d, { vel: 40 }); });
  S.fx('ding', T.recorrido + 21.4, { vel: 34 });

  // La pregunta se escribe: una tilde muy suave cada tres palabras.
  S.ticks([11.9, 13.1, 14.3, 15.5, 16.7, 17.9, 19, 20].map(function (d) { return T.pregunta + d; }), { vel: 18 });

  // La ficha se arma renglon por renglon y la parte A cierra abierta, sin remate.
  [6.8, 10.2, 33.3, 38.7, 43.4, 51.6, 53.9].forEach(function (d, i) { S.fx('pop', T.ficha + d, { vel: 34 + i * 2 }); });
  S.pattern('vibes', 'x..x..x.', { from: Math.round(T.ficha / B), repeat: 12, pitch: ['A4', 'D5', 'F4'], vel: 30 });
  S.master({ gain: -8, fadeOut: 1.4 });
});
