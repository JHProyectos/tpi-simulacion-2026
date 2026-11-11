// Musica original, tranquila, pensada para quedar debajo de la voz: un acorde largo por escena
// y sonidos puntuales en cada entrada. Parte C del video: los cinco escenarios, la comparacion y el cierre.
kit.score(function (S, T) {
  const B = 60 / 84;
  S.tempo(84, { t0: 0 });
  S.program('pad', 'pad', { rev: 0.7, gain: -6 });
  S.program('vibes', 'vibes', { rev: 0.45, gain: -5 });
  S.program('bajo', 'bass', { gain: -5 });
  S.program('pluck', 'pluck', { rev: 0.3, gain: -6 });

  // Un acorde largo por escena: el aire cambia cuando cambia el escenario.
  const AIRE = [
    [T.cambios, 20, ['D3', 'A3', 'E4']],
    [T.e1, 18, ['D3', 'A3', 'F4']],
    [T.e2, 13, ['D3', 'A3', 'F4']],
    [T.e3, 16, ['C3', 'G3', 'E4']],
    [T.e4, 11, ['Bb2', 'F3', 'D4']],
    [T.e5, 16, ['F3', 'C4', 'A4']],
    [T.comparar, 30.4, ['D3', 'A3', 'E4']],
    [T.pendiente, 15.6, ['F3', 'C4', 'A4']],
    [T.respuesta, 26, ['F3', 'C4', 'A4']],
    [T.limites, 19, ['D3', 'A3', 'E4']],
    [T.cierre, 6, ['D3', 'A3', 'F4', 'D5']],
  ];
  AIRE.forEach(function (a, i) { S.chord('pad', a[2], { t: a[0], dur: a[1] + 1.4, vel: 26 + (i % 4) * 3 }); });

  // Las cinco fichas de los escenarios entran de a una.
  for (let i = 0; i < 5; i++) S.fx('pop', T.cambios + 1.5 + i * 1.4, { vel: 34 + i * 2 });
  S.fx('revswell', T.cambios + 1.3, { dur: 1.2, vel: 36 });

  // Cada placa de escenario: las dos cifras entran cuando la voz las nombra y el remate cierra con un ding.
  // Las columnas son: escena, primera cifra, segunda cifra, remate, todas sobre el audio medido.
  [[T.e1, 4.3, 8.6, 13.2], [T.e2, 5, 5.9, 8], [T.e3, 5.6, 12, 11.5], [T.e4, 3.5, 5.2, 8.4], [T.e5, 3.8, 8.6, 12.6]].forEach(function (p) {
    S.fx('pop', p[0] + p[1], { vel: 36 });
    S.fx('pop', p[0] + p[2], { vel: 36 });
    S.fx('ding', p[0] + p[3], { vel: 32 });
  });
  // El haz del QR barre el codigo tres veces.
  for (let i = 0; i < 3; i++) S.fx('tick', T.e3 + 2 + i * 2.6, { vel: 22 });
  // E4 es la bisagra: el sello cae y abajo queda una nota sola.
  S.fx('thud', T.e4 + 7.9, { vel: 48 });
  S.note('bajo', 'Bb1', { t: T.e4 + 7.9, dur: 3, vel: 40 });
  // E5 suma las dos cosas.
  S.fx('boing', T.e5 + 1.9, { vel: 34 });
  S.run('pluck', ['D4', 'F4', 'A4', 'D5'], { t: T.e5 + 12.6, step: 0.5, vel: 36 });

  // La comparacion, sobre los tiempos medidos de la locucion: primero el panel de la caja (2,4),
  // a los 10,4 el del mostrador, y la marca de E5 recien a los 19,7, cuando la voz dice "escenario 5".
  for (let i = 0; i < 6; i++) S.fx('pop', T.comparar + 2.4 + i * 0.95, { vel: 30 + i * 2 });
  S.fx('whoosh', T.comparar + 9.4, { dur: 0.5, vel: 30 });
  for (let i = 0; i < 6; i++) S.fx('pop', T.comparar + 10.4 + i * 0.72, { vel: 32 + i * 2 });
  S.pattern('vibes', 'x..x..x.', { from: Math.round(T.comparar / B), repeat: 8, pitch: ['A4', 'D5', 'F4'], vel: 24 });
  S.fx('chime', T.comparar + 19.7, { vel: 46 });
  S.note('bajo', 'D2', { t: T.comparar, dur: 14, vel: 34 });

  // El tiempo total: seis barras desde 3,2 y la marca de E5 con el cartel de los 13 segundos.
  for (let i = 0; i < 6; i++) S.fx('pop', T.pendiente + 3.2 + i * 0.9, { vel: 30 + i * 2 });
  S.fx('chime', T.pendiente + 8.8, { vel: 42 });
  S.note('bajo', 'F1', { t: T.pendiente + 3.2, dur: 9, vel: 36 });

  // La respuesta: el recuadro entra con un swell y las dos razones con un pop cada una.
  S.fx('revswell', T.respuesta + 1, { dur: 1.4, vel: 46 });
  [5.8, 10.5].forEach(function (d, i) { S.fx('pop', T.respuesta + d, { vel: 34 + i * 3 }); });
  S.fx('ding', T.respuesta + 17, { vel: 34 });
  S.run('pluck', ['A3', 'D4', 'F4', 'A4', 'D5'], { t: T.respuesta + 1.5, step: 0.7, vel: 34 });

  // Los limites: dos renglones, muy tranquilo.
  S.ticks([2.5, 10.1].map(function (d) { return T.limites + d; }), { vel: 20 });

  // El cierre cae en el tiempo fuerte y el ultimo acorde queda sonando.
  S.fx('chime', T.cierre, { vel: 56 });
  S.note('bajo', 'D2', { t: T.cierre, dur: 6, vel: 42 });
  S.run('vibes', ['D5', 'A4', 'F4', 'D4'], { t: T.cierre + 0.8, step: 0.7, vel: 34 });
  S.master({ gain: -10, fadeOut: 1.8 });
});