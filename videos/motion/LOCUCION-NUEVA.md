# Locución nueva para estirar el video

[TOC]

Tres escenas que hoy no están en el video y que el informe ya tiene resueltas.
Todo sale de `entregas/entrega-final/INFORME.md`, secciones 7.1, 7.3 y 9.

Son **2:05 de locución**, toda de Jonatan. La primera versión eran 3:30 con
las mismas ideas: lo que se fue es la prosa de enlace, no los datos.

| Escena nueva | Va en | Dura |
| --- | --- | --- |
| Bondad de ajuste de las llegadas | Parte A, después de la ficha | 0:36 |
| Las distribuciones del modelo | Parte B, antes de la corrida | 0:44 |
| Verificación, validación y réplicas | Parte B, al final | 0:46 |

Con esto los tres films pasan de 7:45 a unos 9:50. Para llegar a los 12
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

> Probamos si la gente llega pareja a lo largo del turno. Un día de servicio,
> el primero de julio: mil ciento setenta y cinco raciones en seis franjas de
> media hora. El chi-cuadrado da doscientos noventa y dos, contra un valor
> crítico de once. Se rechaza.
>
> En la primera media hora entran trescientas cuatro personas. Después de las
> dos y media, cinco.
>
> Por eso el modelo no usa una tasa única: usa una por franja de diez minutos
> y por grupo, sacada de los registros. Un proceso de Poisson no homogéneo.

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

| Escena | Archivo |
| --- | --- |
| 1 | `videos/audios/jonatan/jonatan-e10-ajuste.wav` |
| 2 | `videos/audios/jonatan/jonatan-e11-distribuciones.wav` |
| 3 | `videos/audios/jonatan/jonatan-e12-verificacion.wav` |

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
