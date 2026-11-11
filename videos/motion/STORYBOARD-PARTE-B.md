# Storyboard · Parte B del video

[TOC]

## Qué cubre

Escenas 4, 5 y 6 del guion, de 3:15 a 6:30. Son **1:27 de locución** repartida en tres archivos, y el film de Motion aporta unos **95 segundos** de animación; el resto del bloque son capturas de FlexSim con la voz encima, que van en el editor y no en Motion.

| Escena del guion | Audio | Dura |
|---|---|---|
| 4 Render 3D | `jonatan/jonatan-e04.wav` | 10,6 s |
| 5 Ejecución base | `jonatan/jonatan-e05.wav` | 25,2 s |
| 6 Resultados base | `juan-e06.ogg` | 51,6 s |

## Antes de empezar

- El film se crea desde el tipo **Motion**, no se publican archivos: todo va a la base del artifact, en `modules/`.
- Los módulos de la Parte A están en `videos/motion/modulos/`. `base.css`, `shared.js` y `scenes.json` se copian tal cual; de ahí salen los ayudantes `W.foto`, `W.tramas`, `W.curva` y `W.ejes`, que estas escenas usan.
- **La paleta está cambiada a mano en la Parte A**: el film muestra el juego claro (fondo `#f6f3ec`, azul `#1f5673`, tinta `#22282e`, acento `#d1603d`) en lugar del oscuro que dice el código. Para que las tres partes se vean iguales, la Parte B tiene que arrancar con esa paleta clara escrita en el código, no con la oscura.
- Los 12 assets ya subidos viven en el artifact de la Parte A. Los que necesita esta parte son `sala.webp`, `amb-aerea.webp`, `amb-mostrador.webp`, `cola-mostrador-1caja.mp4` y `caja-1caja.mp4`. Se copian de un artifact al otro, y si eso falla se vuelven a subir desde `3d/video/artlist/` y `videos/`.

## Las cinco escenas

### 1 · `render` — 12 s

Escena 4 del guion. Los renders del modelo en 3D, que hasta ahora casi no se usaron.

- Arranca con `sala.webp` a pantalla completa, con un empuje de escala muy lento.
- A los 4 s entra `amb-aerea.webp` por corte directo, y a los 8 s `amb-mostrador.webp`.
- Arriba a la derecha, el sello «Modelo 3D del salón», el mismo que ya usa la escena de apertura.
- Sin texto grande: la voz ya explica qué se ve.

### 2 · `corrida` — 27 s

Escena 5. El modelo corriendo en FlexSim.

- `cola-mostrador-1caja.mp4` ocupando el cuadro, con un marco fino.
- A los 14 s se parte en dos y entra `caja-1caja.mp4` al lado.
- Un reloj chico arriba a la izquierda que va de 11:40 a 16:00 a lo largo de la escena.
- Rótulo abajo: «UNA CORRIDA · DÍA COMPLETO».

### 3 · `numeros` — 26 s

Primera mitad de la escena 6. Es la **Placa 1** de `flexsim/DATOS_VIDEO.md`. Se puede partir de `scene-numeros.js`, que ya tiene la grilla de seis tarjetas armada: lo que cambia es el arreglo `TARJETAS` y el pie.

Subtítulo de la placa: «E0 · 1 puesto de caja y 3 personas sirviendo · 30 réplicas».

| Tarjeta | Valor | Barra |
|---|---|---|
| Espera máxima en la caja | 4,9 min (±0,2) | — |
| Cola máxima en la caja | 71 personas (±3) | — |
| Tiempo total medio | 68 s (±5) | — |
| Cola máxima en el mostrador | 5 personas | — |
| Utilización de la caja | 63 % | 0,63 |
| Correlación con lo real | 0,95 | — |

Las dos que hay que destacar son **cola máxima en la caja** y **cola máxima en el mostrador**: 71 contra 5 es el número que sostiene todo el resto del video.

Sale el pie viejo, «1 corrida medida · faltan las 30 réplicas del Experimenter». En su lugar: «30 RÉPLICAS · PERFIL PICO · INTERVALOS AL 95 %».

### 4 · `colas` — 18 s

Segunda mitad de la escena 6, y la escena que **hay que dar vuelta**. La versión actual dibuja la cola del mostrador disparándose y dice «el cuello de botella no está en la caja, está en el mostrador». Con los datos del Experimenter pasa lo contrario.

- Mismo eje del día, de 11:40 a 16:00, y las mismas dos curvas de `scene-colas.js`.
- La curva de la **caja** sube hasta 71 y se queda arriba durante todo el pico.
- La curva del **mostrador** se queda pegada abajo, tocando 5 como máximo.
- La frase que queda en pantalla al final: «La cola se hace en la caja. El mostrador no se llena.»

### 5 · `curvas` — 12 s

Cierre de la escena 6: la validación. `scene-curvas.js` se usa tal cual, no tiene datos viejos.

- Las raciones por franja del modelo y de los registros reales, superpuestas.
- Remate: «Correlación 0,95 · menos de 2 % de diferencia en el total».

## Lo que hay que resolver antes de grabar nada más

En el audio de la escena 6, Juan dice **73 %** de ocupación de la caja donde los datos dan **63 %**. Está marcado en `videos/audios/TRANSCRIPCION.md`. O se regraba esa frase, o la placa muestra un número que la voz contradice. No se arregla editando el audio.
