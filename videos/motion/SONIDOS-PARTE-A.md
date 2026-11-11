# Sonidos de la Parte A

[TOC]

El film de la Parte A quedó mudo: le saqué la música y los efectos para que los
pongas vos en la edición. Acá está todo lo que sonaba, con el segundo exacto
contado desde el arranque del film, no desde el arranque de la escena.

Los tres films se exportan por separado, así que cada uno tiene su propio
archivo de sonidos y sus propios tiempos desde cero. Este cubre solo la Parte A.

La columna **vel** es la intensidad con la que sonaba cada golpe, de 0 a 127.
Sirve para saber cuál iba más fuerte que cuál, no como un valor en decibeles.

## Dónde empieza cada escena

| Escena | Empieza | Dura |
| --- | --- | --- |
| Apertura | 0,0 s | 16 s |
| El recorrido | 16,0 s | 29 s |
| La pregunta | 45,0 s | 34 s |
| Ficha del modelo | 79,0 s | 72 s |

El film entero dura 151 s (2:31).

## Efectos puntuales

Estos son los que importan para la edición: cada uno cae en un cuadro concreto.

| Segundo | Sonido | vel | Qué acompaña |
| --- | --- | --- | --- |
| 0,20 | tick | 22 | el salón se dibuja a línea fina |
| 0,45 | tick | 22 | ídem |
| 0,70 | tick | 22 | ídem |
| 0,95 | tick | 22 | ídem |
| 1,20 | tick | 22 | ídem |
| 1,45 | tick | 22 | ídem |
| 3,10 | tick | 22 | ídem |
| 4,90 | tick | 22 | ídem |
| 6,80 | tick | 22 | ídem |
| 8,60 | tick | 22 | ídem |
| 11,40 | revswell | 44 | entra el color en el plano (dura 1,6 s) |
| 13,00 | chime | 48 | queda firme el título |
| 29,40 | pop | 40 | arranca la traza del recorrido |
| 32,00 | pop | 40 | segundo rótulo del recorrido |
| 35,10 | pop | 40 | tercer rótulo del recorrido |
| 37,40 | ding | 34 | se abre la caja |
| 56,90 | tick | 18 | la pregunta se escribe, palabra por palabra |
| 58,10 | tick | 18 | ídem |
| 59,30 | tick | 18 | ídem |
| 60,50 | tick | 18 | ídem |
| 61,70 | tick | 18 | ídem |
| 62,90 | tick | 18 | ídem |
| 64,00 | tick | 18 | ídem |
| 65,00 | tick | 18 | ídem |
| 85,80 | pop | 34 | renglón «Apertura de la caja» |
| 89,20 | pop | 36 | renglón «Empieza la fila» |
| 112,30 | pop | 38 | renglón «Llegadas» |
| 117,70 | pop | 40 | renglón «Puestos de validación» |
| 122,40 | pop | 42 | renglón «Tiempo por DNI» |
| 130,60 | pop | 44 | renglón «Personas sirviendo» |
| 132,90 | pop | 46 | renglón «Tiempo por ración» |

## La música

Todo esto iba a 84 BPM, o sea un tiempo cada 0,714 s. Lo anoto por si querés
que lo que pongas encima caiga en la misma grilla.

### Acordes de fondo (pad)

Uno largo por escena, para que el aire cambie cuando cambia el tema.

| Entra | Dura | Acorde | vel |
| --- | --- | --- | --- |
| 0,0 s | 17,4 s | D3 A3 E4 | 30 |
| 16,0 s | 30,4 s | D3 A3 F4 | 34 |
| 45,0 s | 35,4 s | Bb2 F3 D4 | 38 |
| 79,0 s | 73,4 s | D3 A3 E4 | 42 |

### Bajo

| Entra | Dura | Nota | vel |
| --- | --- | --- | --- |
| 45,0 s | 12 s | Bb1 | 36 |
| 79,0 s | 16 s | D2 | 38 |

### Arpegio del recorrido (pluck)

Seis notas desde **29,5 s**, una cada 0,714 s, vel 38: D4, F4, A4, D5, A4, F4.
La última cae en 33,1 s.

### Vibráfono de la ficha

Patrón `x..x..x.` sobre una grilla de un tiempo por paso, desde **79,3 s**,
doce repeticiones, vel 30, alternando A4, D5 y F4. Suena en los pasos 1, 4 y 7
de cada compás de ocho, o sea tres golpes cada 5,71 s, y termina en 146,4 s.

### Mezcla

El conjunto iba 8 dB por debajo del máximo, con un cierre de 1,4 s al final del
film.

## Lo que no está acá

- Las locuciones, que son archivos aparte en `videos/audios/editados/`.
- Los sonidos de las Partes B y C, que están en sus propios archivos.
