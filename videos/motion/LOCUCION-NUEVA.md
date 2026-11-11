# Locución nueva para estirar el video

[TOC]

Tres escenas que hoy no están en el video y que el informe ya tiene resueltas.
Todo sale de `entregas/entrega-final/INFORME.md`, secciones 7.1, 7.3 y 9.

Son **1:51 de locución**, toda de Jonatan, **ya grabada y recortada**. La
primera versión eran 3:30 con las mismas ideas: lo que se fue es la prosa de
enlace, no los datos. Falta una sola frase, al final de la escena 1: ver
«Qué falta grabar» más abajo.

| Escena nueva | Va en | Arranca | Dura |
| --- | --- | --- | --- |
| Bondad de ajuste de las llegadas | Parte A, al final | 151 s | 0:33 |
| Las variables del modelo | Parte B, después de los renders | 12 s | 0:38 |
| Verificación y validación | Parte B, al final | 159 s | 0:41 |

**Las tres ya están animadas en sus films.** La Parte A pasa de 151 a 184 s
(3:04) y la Parte B, de 121 a 181 s (3:01): sumó 79 s de escenas nuevas y
perdió 19 al cortar las cinco del medio a la medida de la voz. Los tiempos de
`SONIDOS-PARTE-B.md` están recalculados sobre el film de ahora.

Con esto los tres films pasan de 7:45 a 9:16, y las tres pistas de voces ya
están armadas. Para llegar a los 12
minutos el resto tiene que salir de los tramos de captura de FlexSim, que van
en la edición y no en Motion.

## Por qué estas tres y no otras

Son las tres cosas que una cátedra de Simulación busca en un TPI y que el
video hoy no muestra: que probaste las distribuciones de entrada en vez de
suponerlas, que separás verificación de validación, y que justificás el
número de réplicas. El video actual muestra los resultados pero no el método.

---

## Escena 1 · Bondad de ajuste de las llegadas

Va en la **Parte A**, después de la ficha del escenario base. En pantalla: la
tabla de las seis franjas, y la última fila destacada sobre «después de las
dos y media, cinco».

Esto es lo que quedó grabado, que es lo que vale:

> Probamos si la gente llega pareja a lo largo del turno. Para eso tomamos un
> día de servicio de pico, el primero de julio: mil ciento setenta y cinco
> raciones en seis franjas de media hora.
>
> El chi-cuadrado da doscientos noventa y dos, contra un valor crítico de
> once. Se rechaza.
>
> En la primera media hora entran trescientas cuatro personas, y después de
> las dos y media solo cinco.
>
> Por eso el modelo no usa una tasa única: usa una franja de diez minutos por
> grupo. Esto lo sacamos de los registros.

«Día de servicio de pico» es correcto: el informe trabaja con dos perfiles de
demanda, pico y bajo, y el primero de julio está en el grupo alto (dieciocho
de los treinta y dos días pasan las mil raciones).

---

## Escena 2 · Las distribuciones del modelo

Va en la **Parte B**, antes de la corrida del escenario base. En pantalla: la
tabla de variables, un renglón por vez. Cada párrafo es un renglón.

> En el modelo hay cuatro cosas que cambian de persona a persona.
>
> Lo que tarda alguien en validar el DNI sale de los registros del puesto: algo
> más de tres segundos, con una cola de gente que tarda bastante más. Esa forma
> es una lognormal.
>
> La demora con que abre la caja tampoco es fija: el modelo elige al azar uno
> de los treinta y dos días que tenemos anotados. En promedio son dos minutos,
> pero hubo días de siete.
>
> Cuántas raciones retira cada uno depende de su beca.
>
> Y la cola que ya está esperando cuando abre es la única que no medimos. Esa
> la ajustamos nosotros, y por eso la decimos como supuesto.

---

## Escena 3 · Verificación, validación y réplicas

Va en la **Parte B**, al final, antes de pasar a los escenarios alternativos.
En pantalla: dos columnas, verificación a la izquierda y validación a la
derecha, y la placa de las 30 réplicas sobre la última frase.

> Dos pruebas distintas. Verificación: ¿el modelo hace lo que diseñamos? Los
> tiempos van en orden, el total del día da mil trescientas sesenta y nueve
> contra mil trescientas ochenta y una, y al final no queda nadie en las filas.
>
> Validación: ¿se parece al comedor real? Correlación de cero coma noventa y
> cinco en la curva de raciones, un uno y medio por ciento de diferencia en el
> total, y una cola máxima de sesenta y seis personas contra las sesenta a
> setenta observadas.
>
> Es una simulación terminante: cada réplica es un día que arranca vacío, así
> que no hay período de calentamiento. Treinta réplicas por escenario, y de ahí
> salen los intervalos al noventa y cinco por ciento.

---

## Antes de grabar

- **Leelas en voz alta cronometrando.** Están calculadas a 2,6 palabras por
  segundo, que es el ritmo de los audios ya grabados. Si sale más lento, las
  escenas se estiran y no pasa nada.
- Van **apretadas**: cada frase tiene un dato. Conviene hacer una pausa corta
  entre párrafo y párrafo, porque en pantalla ahí cambia lo que se muestra.
- **Un archivo por escena**, mismo micrófono y mismo lugar que el resto, con
  tres segundos de silencio al principio y al final.
- Si te trabás, **repetí la oración entera** en vez de retomar a mitad.

| Escena | Archivo | Dura |
| --- | --- | --- |
| 1 | `videos/audios/jonatan/jonatan-e10-ajuste.wav` | 32,6 s |
| 2 | `videos/audios/jonatan/jonatan-e11-distribuciones.wav` | 37,5 s |
| 3 | `videos/audios/jonatan/jonatan-e12-verificacion.wav` | 41,0 s |

Los tres salen de `videos/audios/jonatan-locucion-nueva.ogg`, que es la toma
cruda completa y queda en el repo por si hay que volver a cortar.

## Qué falta grabar

**Una sola frase**, de unos tres segundos, para pegar al final de la escena 1:

> Un proceso de Poisson no homogéneo.

Es el único pedazo del guion que no quedó en la toma. Nombra el método con el
término que la cátedra busca, y hoy la escena 1 termina en «esto lo sacamos de
los registros», que describe de dónde salen los números pero no cómo se
modelan las llegadas. Grabala suelta, con el mismo micrófono, y se concatena
al final del `jonatan-e10-ajuste.wav`.

Todo lo demás está completo. Las dos retomas que habías dejado en la toma
cruda (un arranque falso al principio de la escena 1, y otro en medio de la
escena 2) ya quedaron fuera de los recortes.

## Un detalle de nivel

La toma nueva está **4,5 dB más fuerte** que los audios ya grabados (−19,4 dB
medios contra −23,9 dB) y llega a 0,0 dB de pico, o sea que en algún momento
toca el techo. No se tocó nada: si se monta así, la voz nueva va a sonar más
alta que la vieja. Se arregla en la edición, bajando estos tres archivos, o
acá con un `loudnorm` antes de montarlos.

## El pendiente de la sección 7.1

Ya está averiguado el día: es el **1 de julio de 2026**. Tiene 1.175 raciones
consumidas, no 1.176, y las seis franjas dan 304, 236, 276, 191, 163 y 5.

Lo que **no** se pudo reconstruir es la probabilidad teórica de cada franja.
No sale del promedio de los días registrados ni de ningún día en particular:
el promedio de los otros 31 días le da un 15,3 % a la franja de las 14:00 y la
tabla del informe le da un 4,5 %. Esa diferencia sola aporta 237 de los 305,90
del chi-cuadrado, o sea que el rechazo depende casi entero de un número cuyo
origen no está documentado.

Por eso el texto de la escena 1 usa una prueba distinta, que sí se puede
reproducir: contra un reparto parejo entre las seis franjas. Da 292,4 contra
11,07 con 5 grados de libertad, rechaza igual, y la conclusión del informe
—tasa por franja en vez de tasa única— se sostiene.

La sección 7.1 del informe ya quedó cambiada con esta prueba, en `INFORME.md`
y en `INFORME_fuente.md`. El texto de la escena 1 y el informe dicen lo mismo.
