# Transcripción de la locución y cortes por escena

[TOC]

La transcripción la hizo Whisper (modelo medium), así que algunos nombres salen mal escritos ("Jonathan Harvards", "flexim"). Los tiempos son de la grabación original, en segundos.

## Audios listos por escena

Los de Jonatan están en `jonatan/`, ya recortados. Los de Juan no necesitaron cortes: cada archivo tiene una sola toma limpia.

| Escena | Archivo | Duración | Tramos usados de `Grabaciones-Jonatan.m4a` |
|---|---|---|---|
| 0 Apertura | `jonatan/jonatan-e00.wav` | 9,0 s | 7,9 – 16,3 (toma 2) |
| 3 Escenario base | `jonatan/jonatan-e03.wav` | 71,0 s | 23,1 – 60,4 y 85,1 – 117,6 (toma 3 desde "Hay un solo puesto") |
| 4 Render 3D | `jonatan/jonatan-e04.wav` | 10,6 s | 124,4 – 134,3 |
| 5 Ejecución base | `jonatan/jonatan-e05.wav` | 25,2 s | 145,2 – 169,8 |
| 6 Resultados base | `juan-e06.ogg` | 51,6 s | — |
| 7 Introducción | `juan-e07-a.ogg` | 9,4 s | — |
| 7 E1 | `jonatan/jonatan-e07-e1.wav` | 16,6 s | 204,2 – 220,3 (toma 3) |
| 7 E2 | `juan-e07-b.ogg` | 11,6 s | — |
| 7 E3 | `jonatan/jonatan-e07-e3.wav` | 15,2 s | 224,1 – 238,8 |
| 7 E4 | `juan-e07-c.ogg` | 10,3 s | — |
| 7 E5 | `jonatan/jonatan-e07-e5.wav` | 15,1 s | 242,0 – 256,5 |
| 8 Comparación | `jonatan/jonatan-e08.wav` | 45,3 s | 281,2 – 311,2 y 321,6 – 335,9 (toma 2 + retoma de "En promedio") |
| 9 Conclusión (Juan) | `juan-e09.ogg` | 25,2 s | — |
| 9 Conclusión (Jonatan) | `jonatan/jonatan-e09.wav` | 18,4 s | 364,4 – 382,2 (toma 2) |

Se sacaron los "Escena N" dichos en voz alta, las tomas cortadas y los silencios entre tomas. Donde se unen dos tomas queda una pausa de 0,45 s, y cada archivo tiene 0,3 s de silencio al principio y al final.

## Diferencias con el guion

- [ ] **Juan, escena 6:** dice «**73 %**» de ocupación de la caja; el guion dice **63 %**. Hay que regrabar esa frase o corregir el texto en pantalla.
- [ ] **Jonatan, escena 3:** «Lo que pudimos sacar de los … viene de ahí»: parece que falta «registros». Escuchalo en el segundo 105 aprox.
- [ ] **Jonatan, E5:** no dice «2,4 minutos» después de «igual que en el escenario 1». Se entiende igual.
- **Jonatan, E3:** «menos que un segundo **por** puesto» (el guion dice «un segundo puesto»).
- **Jonatan, E1:** «no desapareció: **solo** se mudó al mostrador». Funciona bien.
- **Juan, E4:** «el cambio es ínfimo» en lugar de «no cambia casi nada». Mismo sentido.
- **Escena 3:** el corte entre «tipo de cliente» y el retome de «Hay un solo puesto» queda pegado a la palabra siguiente. Revisá que no se oiga un pedacito de «hay».

## Transcripción completa: Grabaciones-Jonatan.m4a (6:30)

Las tomas descartadas están ~~tachadas~~.

| Tiempo | Texto |
|---|---|
| 1,6 – 4,7 | ~~escena 0 y Jonatan Harbertz~~ |
| 6,4 – 15,9 | escena 0 · y Jonatan Harbertz. En este video presentamos nuestro trabajo integrador de simulación: la fila de un comedor universitario, simulada en FlexSim. |
| 21,7 – 28,5 | escena 3 · Este es el escenario base, la situación de partida contra la que comparamos todo. |
| 29,0 – 46,5 | La caja abre alrededor de las 12, pero la gente llega antes. Suponemos que la fila empieza a formarse a las 11:40. Ese horario no lo medimos; lo elegimos porque con él el modelo reproduce la fila que se ve en el comedor. La caja casi nunca abre en punto, y esa demora sí sale de los registros. |
| 47,9 – 60,4 | Después de la apertura, las llegadas salen de los registros reales de reservas, por franjas de 10 minutos y por tipo de cliente. |
| 60,4 – 70,7 | ~~Hay un solo puesto de validación. Cada persona presenta un DNI por ración y cada DNI lleva unos 4 segundos, un tiempo que sacamos de los registros del puesto.~~ |
| 73,8 – 82,5 | ~~Hay un solo puesto de validación. Cada persona presenta un DNI por ración y cada DNI lleva unos 4 segundos. Un tiempo…~~ |
| 85,2 – 95,3 | Hay un solo puesto de validación. Cada persona presenta un DNI por ración, y cada DNI lleva unos cuatro segundos aproximadamente. Este tiempo lo sacamos de los registros del puesto. |
| 96,4 – 117,3 | Después pasa a la fila de servicio, donde tres personas sirven, a unos 17 segundos por ración aproximadamente. Una de ellas atiende el menú vegetariano. Lo que pudimos sacar de los (…) viene de ahí; lo que no pudimos medir, como el tiempo de servicio o cuántas raciones retira cada persona, lo estimamos y lo declaramos como supuesto. |
| 122,3 – 134,1 | escena 4 · Esta es la representación tridimensional del comedor. Por este pasillo se forma la fila de caja, y acá están los puestos de validación, y por acá la gente avanza hacia el mostrador. |
| 142,6 – 143,5 | escena 5 |
| 145,3 – 169,5 | Corremos el escenario base en el día pico. Antes de que abra la caja ya hay unas setenta personas esperando. Abre la caja y la fila empieza a bajar, pero tarda: con un solo puesto, en el pico llega gente casi tan rápido como se la atiende. Después del mostrador, en cambio, no se junta casi nadie: la fila de servicio no pasa de 5 personas. En el escenario base, el cuello de botella es la caja. |
| 179,8 – 180,8 | Escena 7 |
| 181,7 – 192,2 | ~~Escenario 1, dos puestos de caja todo el turno. La espera más larga de la caja baja a la mitad, de 5 a 2,4 minutos. Pero miren el mostrador, la caja…~~ |
| 195,0 – 200,2 | ~~Escenario 1, 2 puestos de caja todo el turno. La espera más larga de la caja…~~ |
| 204,3 – 220,0 | Escenario 1: 2 puestos de caja todo el turno. La espera más larga en la caja baja a la mitad, de 5 a 2,4 minutos. Pero miren el mostrador: la cola pasa de 5 a 31 personas. La cola no desapareció: solo se mudó al mostrador. |
| 224,2 – 238,5 | Escenario 3: validación con código QR, que tarda un 60 % de lo que tarda el DNI. Mejora la caja, pero menos que un segundo por puesto: 2,9 minutos. Y también corre la cola al mostrador: unas 23 personas. |
| 242,1 – 256,2 | Escenario 5: 2 puestos y 4 personas sirviendo. La caja mejora igual que en el escenario 1, y la cola de mostrador queda en 16 personas, la mitad que en el escenario 1. Es el que logra el menor tiempo total. |
| 265,3 – 266,4 | Escena 8 |
| 267,5 – 273,7 | ~~Pongamos todo junto ahora. A la izquierda la caja: todo lo que agrega capacidad en la caja la mejora.~~ |
| 281,3 – 310,9 | Ahora pongamos todo junto. A la izquierda, la caja: todo lo que agrega capacidad en la caja la mejora, y reforzar solo el mostrador no le hace nada. A la derecha, el mostrador: todo lo que mejora la caja le manda gente. La única combinación que mejora la caja y contiene el mostrador es la del escenario 5. Como las 30 réplicas de cada escenario usan las mismas llegadas, comparamos réplica por réplica, y todas estas diferencias son estadísticamente significativas. |
| 311,6 – 319,5 | ~~En promedio, el tiempo total baja unos 13 segundos por persona. Parece poco, pero el promedio incluye a la mayoría, que llega cuando…~~ |
| 321,7 – 335,6 | En promedio, el tiempo total baja unos 13 segundos por persona. Parece poco, pero el promedio incluye a la mayoría, que llega cuando no hay fila. La mejora la siente quien llega en el pico: su espera se reduce a la mitad. |
| 347,2 – 359,8 | ~~Escena nueve. Dos aclaraciones para cerrar. Ningún escenario cambia la espera de quienes llegan antes de la apertura. Eso depende de a qué hora llega la gente y de la caja.~~ |
| 364,5 – 381,9 | Dos aclaraciones para cerrar. Ningún escenario cambia la espera de quienes llegan antes de la apertura: eso depende de a qué hora llega la gente y de que la caja abra puntual. Y el tiempo de servicio por ración no lo pudimos cronometrar: es un supuesto, y el siguiente paso sería medirlo en el comedor. Gracias por mirar. |

## Transcripción: audios de Juan

### juan-e06.ogg (escena 6)

| Tiempo | Texto |
|---|---|
| 0,0 – 8,0 | Para tener resultados confiables, corrimos 30 réplicas de cada escenario: 30 días simulados, cada uno con llegadas distintas. |
| 8,2 – 16,2 | En el pico, quien llega antes de la apertura espera unos 13 minutos. Una vez abierta la caja, la espera más larga es de 5 minutos. |
| 16,7 – 20,2 | La caja está ocupada el **73 %** del tiempo. |
| 21,0 – 26,5 | En el mostrador, la cola máxima es de 5 personas, y la espera media es de 1 segundo. |
| 26,5 – 51,1 | Para validar el modelo, comparamos las raciones validadas cada 10 minutos con los registros reales. La curva coincide, con una correlación de 0,95, y el total difiere en menos de un 2 %. La cola antes de la apertura y su espera también caen en lo que se observa en el comedor: entre 60 y 70 personas y entre 10 y 15 minutos. |

### juan-e07-a.ogg (escena 7, introducción)

| Tiempo | Texto |
|---|---|
| 0,0 – 8,4 | Ahora probamos 5 cambios sobre el escenario base. En cada uno cambiamos solo una cosa, así sabemos qué causa la diferencia. |

### juan-e07-b.ogg (escena 7, E2)

| Tiempo | Texto |
|---|---|
| 0,0 – 11,0 | Escenario 2: el segundo puesto solo en el pico, de 12 a 13:30. Da exactamente lo mismo que el escenario 1. Después de las 13:30 alcanza con un solo puesto. |

### juan-e07-c.ogg (escena 7, E4)

| Tiempo | Texto |
|---|---|
| 0,0 – 9,5 | Escenario 4: un solo puesto y cuatro personas sirviendo. El cambio es ínfimo: el mostrador ya alcanzaba, y el problema estaba en la caja. |

### juan-e09.ogg (escena 9)

| Tiempo | Texto |
|---|---|
| 0,0 – 24,3 | Volvamos a la pregunta. Con dos puestos de validación en el pico y cuatro personas sirviendo. Abrir el segundo puesto, solo, no alcanza: la cola se pasa al mostrador. Reforzar solo el mostrador tampoco, porque el problema estaba en la caja. Hay que hacer las dos cosas juntas. Nuestra recomendación es abrir el segundo puesto de 12 a 13:30 y sumar una persona al mostrador en ese horario. |
