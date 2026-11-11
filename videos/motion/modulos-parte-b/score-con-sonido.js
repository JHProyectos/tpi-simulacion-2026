// Musica original, tranquila, pensada para quedar debajo de la locucion grabada.
// Parte B del video (escenas 4 a 6 del guion): renders, una corrida y los resultados del escenario base.
kit.score(function (S, T) {
  const B = 60 / 84;
  S.tempo(84, { t0: 0 });
  S.program('pad', 'pad', { rev: 0.7, gain: -5 });
  S.program('vibes', 'vibes', { rev: 0.45, gain: -4 });
  S.program('bajo', 'bass', { gain: -4 });
  S.program('pluck', 'pluck', { rev: 0.3, gain: -5 });

  // Un acorde largo por escena: el aire cambia cuando cambia el tema, como en la Parte A.
  const AIRE = [
    [T.render, 12, ['D3', 'A3', 'E4']],
    [T.corrida, 27, ['D3', 'A3', 'F4']],
    [T.replicas, 12, ['F3', 'C4', 'A4']],
    [T.numeros, 26, ['Bb2', 'F3', 'D4']],
    [T.colas, 18, ['Bb2', 'F3', 'C4']],
    [T.curvas, 12, ['D3', 'A3', 'E4']],
    [T.antes, 14, ['D3', 'A3', 'F4']],
  ];
  AIRE.forEach(function (a, i) { S.chord('pad', a[2], { t: a[0], dur: a[1] + 1.4, vel: 26 + i * 3 }); });
  S.note('bajo', 'D2', { t: T.corrida, dur: 14, vel: 34 });
  S.note('bajo', 'F2', { t: T.replicas, dur: 11, vel: 32 });
  S.note('bajo', 'Bb1', { t: T.numeros, dur: 14, vel: 36 });
  S.note('bajo', 'Bb1', { t: T.colas, dur: 12, vel: 38 });
  S.note('bajo', 'D2', { t: T.curvas, dur: 12, vel: 36 });
  S.note('bajo', 'D2', { t: T.antes, dur: 13, vel: 34 });

  // Los renders: una tilde muy suave en cada lamina nueva.
  S.ticks([0.3, 0.8], { vel: 20 });
  S.fx('pop', T.render + 4, { vel: 30 });
  S.fx('pop', T.render + 8, { vel: 32 });

  // La corrida: el reloj camina y el cuadro se parte en dos a los 14 s.
  S.ticks([2, 5, 8, 11, 17, 20, 23, 26].map(function (d) { return T.corrida + d; }), { vel: 16 });
  S.fx('whoosh', T.corrida + 13.4, { dur: 0.5, vel: 36 });
  S.fx('ding', T.corrida + 14.6, { vel: 30 });

  // Las treinta replicas: una tilde cada tres dias dibujados, y un cierre cuando estan los treinta.
  const DIAS = [];
  for (let i = 0; i < 30; i += 3) DIAS.push(T.replicas + 1.3 + i * 0.2);
  S.ticks(DIAS, { vel: 18 });
  S.fx('ding', T.replicas + 8.6, { vel: 32 });

  // La placa: una tarjeta cada 2,2 s, y un realce cuando quedan las dos colas.
  for (let i = 0; i < 6; i++) S.fx('pop', T.numeros + 2.3 + i * 2.2, { vel: 32 + i * 2 });
  S.pattern('vibes', 'x..x..x.', { from: Math.round(T.numeros / B), repeat: 7, pitch: ['A4', 'D5', 'F4'], vel: 26 });
  S.fx('revswell', T.numeros + 22.4, { dur: 1.6, vel: 42 });

  // Las dos colas: la de la caja sube, la del mostrador se queda abajo, y cierra la frase.
  S.run('pluck', ['D4', 'F4', 'A4', 'D5', 'A4'], { t: T.colas + 0.8, step: 0.9, vel: 36 });
  S.fx('ding', T.colas + 3.1, { vel: 38 });
  S.fx('tick', T.colas + 9, { vel: 26 });
  S.fx('chime', T.colas + 12.1, { vel: 44 });

  // La validacion: las dos curvas se superponen.
  S.fx('pop', T.curvas + 1, { vel: 28 });
  S.fx('pop', T.curvas + 4.6, { vel: 32 });
  S.fx('sparkle', T.curvas + 8.5, { vel: 40 });

  // Antes de abrir: las dos franjas crecen y la parte B cierra sin remate, para empalmar con la C.
  S.fx('pop', T.antes + 1.5, { vel: 30 });
  S.fx('ding', T.antes + 3.5, { vel: 36 });
  S.fx('pop', T.antes + 4.3, { vel: 32 });
  S.fx('chime', T.antes + 8.7, { vel: 42 });
  S.master({ gain: -9, fadeOut: 1.6 });
});
