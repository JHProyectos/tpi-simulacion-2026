# Tiempos de la Parte A

[TOC]

El film dura **2:31** y cada escena dura lo que dura su locución. Los segundos salen de la transcripción palabra por palabra de los cuatro audios, hecha con Whisper, así que tienen un margen de unos 0,2 s. Los textos entran un poco después de la palabra, nunca antes: que aparezcan antes se lee como spoiler.

## Dónde va cada audio

| Escena | Empieza | Dura | Audio | Dura el audio |
|---|---|---|---|---|
| `abrir` | 0:00 | 16 s | `jonatan/jonatan-e00.wav` | 9,0 s |
| `recorrido` | 0:16 | 29 s | `editados/juan_escena01.wav` | 27,7 s |
| `pregunta` | 0:45 | 34 s | `editados/juan_escena02.wav` | 32,9 s |
| `ficha` | 1:19 | 72 s | `jonatan/jonatan-e03.wav` | 70,8 s |

En el editor, cada audio arranca en el segundo de la columna «Empieza». Los sobrantes de uno o dos segundos al final de cada escena son aire para que la voz no quede pegada a la siguiente.

## Qué aparece y cuándo

Los segundos de esta tabla son **desde el principio de cada escena**, no desde el principio del film.

### `abrir`

| Segundo | Qué entra | Lo que se escucha |
|---|---|---|
| 0,7 | Jonatan Harbertz · Juan Chávez | «Jonatan Harbertz» |
| 3,3 | Trabajo integrador de Simulación · 2026 | «nuestro trabajo integrador de simulación» |
| 5,4 | La fila de un comedor universitario | «la fila de un comedor universitario» |
| 8,1 | Sello «Modelo 3D del salón» | «simulada en FlexSim» |

### `recorrido`

| Segundo | Qué entra | Lo que se escucha |
|---|---|---|
| 2,4 | Nota «ilustración a partir del modelo» | — |
| 13,4 | Empieza a dibujarse el recorrido | «Al llegar, cada persona realiza una fila» |
| 13,5 | Arranca a caminar la persona | ídem |
| 16,0 | Paso por la caja | «valida su reserva presentando su DNI» |
| 19,1 | Paso a la segunda fila | «pasa a otra fila» |
| 21,3 | Se marca el mostrador | «retirar la bandeja en el mostrador» |
| 23,0 | Se va la persona | «Simulamos ese recorrido» |

### `pregunta`

| Segundo | Qué entra | Lo que se escucha |
|---|---|---|
| 9,5 | La regla y el rótulo | «La pregunta que nos hicimos» |
| 11,9 | Se empieza a escribir la pregunta | «qué combinación de puestos…» |
| 20,0 | Termina de escribirse | «…al mostrador» |

La pregunta tiene 23 palabras y Juan la dice en 8,2 segundos, así que entra una palabra cada 0,36 s.

### `ficha`

| Segundo | Renglón | Lo que se escucha |
|---|---|---|
| 0,6 | Título «Escenario base» | «Este es el escenario base» |
| 2,6 | Subtítulo del caso mixto | «la situación de partida» |
| 6,8 | Apertura de la caja · ~12:00 | «La caja abre alrededor de las 12» |
| 10,2 | Empieza la fila · 11:40 | «la fila empieza a formarse a las 11:40» |
| 33,3 | Llegadas · cada 10 min | «salen de los registros reales de reservas» |
| 38,7 | Puestos de validación · 1 | «Hay un solo puesto de validación» |
| 43,4 | Tiempo por DNI · 4 s | «cada DNI lleva unos 4 segundos» |
| 51,6 | Personas sirviendo · 3 | «tres personas sirven» |
| 53,9 | Tiempo por ración · 17 s | «17 segundos por ración» |

Los dos primeros renglones cambiaron de orden respecto de la versión anterior: Jonatan nombra la apertura de la caja antes que el horario en que empieza la fila.

## Un hueco en el audio de la escena 3

En `jonatan/jonatan-e03.wav` hay **5,3 segundos de silencio entre el segundo 26,8 y el 32,2**, en medio de la frase «las llegadas salen de… los registros reales de reservas». Por eso el renglón de las llegadas entra recién a los 33,3: si entrara antes, queda colgado durante el silencio.

Ese hueco se puede apretar y recuperar unos 5 segundos, pero hay que rehacer la escena, porque todos los segundos de abajo de los 27 se corren.
