# Qué mirar en la Parte C

[TOC]

La Parte C se armó entera sin reproducirla: los tiempos salen de medir los
audios, y las decisiones de color se razonaron sobre los valores, no sobre el
cuadro. Esta es la lista de lo que hay que mirar la primera vez que la abras,
en orden de qué tan probable es que esté mal.

El artifact es `https://claude.ai/artifact/S1ArXvHJ4GMTC8bkurTVCT` y el film
dura 191 s (3:11), once escenas.

## Lo primero

### El sello de E4 y el cartel de los 13 segundos

Los dos quedaron con texto naranja oscuro y borde del naranja claro, el mismo
color en dos tonos. Sobre papel se razona bien, pero es el tipo de combinación
que puede verse sucia o lavada en el cuadro, sobre todo si el borde se ve fino.

- El sello **LA CAJA NO SE MUEVE** cae en el segundo **74,9** del film.
- El cartel **13 s menos que la base** aparece en el **133,2**.

Si se ve mal, lo más simple es llevar el borde al mismo `--marca-texto` que el
texto, o engrosarlo.

### La foto de ambiente al 14 %

Venía al 30 % y la bajamos para que no metiera textura abajo de los números.
Puede haber quedado tan tenue que la escena se vea plana y sin fondo. Pasa en
cuatro escenas: `cambios` (0 s), `e2` (38 s), `e4` (67 s) y `respuesta` (140 s).

### El conteo largo de E3

En E3 la cifra de la caja rueda de 4,9 a 2,9 durante **3,5 segundos**, de los
57,4 a los 60,9 del film. Es así de lento a propósito, para que el 2,9 aterrice
justo cuando Jonatan lo dice. En el papel cierra, pero un número rodando tanto
tiempo puede verse raro.

## Los tiempos contra la voz

Todas las entradas se corrieron a los segundos medidos de los ocho audios, pero
medidos sobre el archivo de audio, no vistos contra la imagen. Vale mirar que
cada cifra aparezca cuando se la nombra, sobre todo acá.

| Escena | Empieza | Qué mirar |
| --- | --- | --- |
| E1 | 20,0 s | la cifra del mostrador no se mueve hasta «de 5 a 31 personas» |
| E3 | 51,0 s | el remate va **antes** que la cifra del mostrador, como lo dice él |
| E4 | 67,0 s | el sello cae en «el problema estaba en la caja», no antes |
| E5 | 78,0 s | nada marca el E5 hasta que lo nombra |
| Tiempo total | 124,4 s | la segunda línea entra en el 137,3 y la escena corta en el 140,0: son 2,7 s para catorce palabras, puede quedar corto |

## Cosas que ya sabemos y no son errores

- **El film se exporta mudo.** La música y los efectos se sacaron a propósito;
  el inventario completo está en `SONIDOS-PARTE-C.md` y el score original en
  `modulos-parte-c/score-con-sonido.js`.
- **El clip de las dos cajas dura 9 s en una escena de 18**, así que se ve dos
  veces seguidas. No está verificado cómo se comporta eso al exportar.
- **La placa final dura 6 s**, bajada de 8 porque era placa muda entera.

## Lo que no se resolvió y no es de la Parte C

En `flexsim/DATOS_VIDEO.md` hay una contradicción entre la corrida validada
suelta y el Experimenter sobre el mostrador: 7,7 min y 131 personas contra
0,016 min y 4,8. El video usa solo el Experimenter, así que no afecta lo que se
ve, pero conviene revisar `TiemposServicio` fila 2, Scale 17,3 en
`comedor_unc_3.fsm` antes de cerrar el trabajo.
