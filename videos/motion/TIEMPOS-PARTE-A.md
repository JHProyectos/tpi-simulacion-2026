# Tiempos de la Parte A

[TOC]

El film dura **3:04** y cada escena dura lo que dura su locución. Los segundos salen de la transcripción palabra por palabra de los cuatro audios, hecha con Whisper, así que tienen un margen de unos 0,2 s. Los textos entran un poco después de la palabra, nunca antes: que aparezcan antes se lee como spoiler.

## Dónde va cada audio

| Escena | Empieza | Dura | Audio | Dura el audio |
|---|---|---|---|---|
| `abrir` | 0:00 | 16 s | `jonatan/jonatan-e00.wav` | 9,0 s |
| `recorrido` | 0:16 | 29 s | `editados/juan_escena01.wav` | 27,7 s |
| `pregunta` | 0:45 | 34 s | `editados/juan_escena02.wav` | 32,9 s |
| `ficha` | 1:19 | 72 s | `jonatan/jonatan-e03.wav` | 70,8 s |
| `ajuste` | 2:31 | 33 s | `jonatan/jonatan-e10-ajuste.wav` | 32,6 s |

En el editor, cada audio arranca en el segundo de la columna «Empieza». Los sobrantes de uno o dos segundos al final de cada escena son aire para que la voz no quede pegada a la siguiente.

## La pista ya armada

`videos/audios/parte-a-voces.wav` tiene las cinco locuciones en su lugar: dura
184 s justos, igual que el film, así que se monta sobre el video exportado sin
correr nada. Es mono, 48 kHz, PCM de 16 bits.

La arma `analisis/armar_pista_voces.py`, que es la única fuente de verdad de los
tiempos. Si cambia una escena, se toca ahí y se corre de nuevo:

```bash
python analisis/armar_pista_voces.py parte-a
```

### Los volúmenes están emparejados

Los originales venían muy desparejos entre las dos voces, hasta 7 dB de
diferencia, y el audio nuevo además pasaba el techo:

| Audio | Voz | Venía en | Pico |
| --- | --- | --- | --- |
| `jonatan-e00.wav` | Jonatan | −24,0 LUFS | −5,6 dB |
| `juan_escena01.wav` | Juan | −16,9 LUFS | −1,5 dB |
| `juan_escena02.wav` | Juan | −16,5 LUFS | −1,5 dB |
| `jonatan-e03.wav` | Jonatan | −22,7 LUFS | −4,4 dB |
| `jonatan-e10-ajuste.wav` | Jonatan | −17,5 LUFS | **+0,9 dB** |

La pista lleva los cinco a **−16 LUFS** con el pico real en **−1,5 dB**, que
deja lugar para la música encima. Los archivos originales no se tocaron: todo
el emparejado pasa dentro del script.

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

## Una retoma en el audio de la escena 3

Lo que antes figuraba acá como «un hueco de 5,3 segundos» es en realidad **una
retoma**. Transcribiendo el tramo aislado se escucha la frase dos veces:

| Segundo de `jonatan-e03.wav` | Qué se escucha |
| --- | --- |
| 25,1 a 27,1 | «Después de la apertura, las llegadas salen…» y se corta |
| 27,1 a 30,1 | aire, respiración, nada dicho |
| 30,1 en adelante | «Después de la apertura, las llegadas salen de los registros reales de reservas, por franjas de 10 minutos y por tipo de cliente» |

Por eso el renglón de las llegadas entra recién a los 33,3: si entrara antes,
queda colgado sobre el arranque fallido.

**Se puede sacar.** Cortando de 24,9 a 30,05 se van la frase repetida y el aire,
y el audio pasa de 70,8 a 65,6 s. A cambio hay que rehacer la escena: todos los
renglones de abajo de los 25 se corren 5,15 s (33,3 → 28,15; 38,7 → 33,55;
43,4 → 38,25; 51,6 → 46,45; 53,9 → 48,75) y la escena puede bajar de 72 a 67 s.
Está sin hacer.
