# Ubicaciones 3D en el modelo nuevo de FlexSim

[TOC]

Reemplaza la tabla 4.4 y la tabla `Ubicaciones` de `GUIA_PERSONAS_3D.md`. Los valores de esa guía estaban medidos en el dibujo viejo (`comedor-v00.dae`). Estos están medidos en el modelo hecho en Blender (`3d/comedor-blender-liviano.dae`), con la Shape puesta como está en `comedor_unc_2.fsm`.

## 1. Cómo está puesta la escena

| Dato | Valor |
|---|---|
| Posición de la Shape | X = 8,24 · Y = −47,75 · Z = 0 |
| Tamaño | 16,52 × 95,50 × 6,80 m (escala 1) |
| Rotación | 0, 0, 0 |
| El edificio ocupa | X de 0 a 16,5 · Y de −95,5 a 0 |
| Altura del piso | **Z = 0,30** (el modelo tiene 0,3 m de cimiento bajo el piso) |
| Eje del pasillo central | X = 8,33 |

Regla de conversión desde Blender: **X + 8,33**, **Y − 24,15**, **Z + 0,30**.

> Si la Shape se mueve sin querer, se vuelve a escribir X = 8,24, Y = −47,75, Z = 0.

## 2. Qué hay en la escena

- **Cubículos de validación:** dos cajas blancas a los lados del pasillo central, con el frente hacia el sur. El pasillo entre ellos mide 3,25 m (X de 6,60 a 9,85) y los cubículos empiezan en Y = −12,75.
- **Pared de los pasos:** en Y = −10,1. Tiene 3 pasos con puertas, en X ≈ 2,2, 8,25 y 14,2. Los pasos van del salón a la zona del mostrador.
- **Mostrador:** al otro lado de la pared, con 10 cubetas, protector de vidrio y el puesto vegetariano en el extremo derecho.
- **Postas con cuerda:** dos líneas a lo largo del pasillo central, de Y = −35,4 a Y = −13,4 (posición del `.blend` al 08/11, después de que las corrieras hacia atrás).
- **Escritorios de caja:** uno en cada cubículo, pegado a la pared del pasillo, detrás de la ventanilla (sección 3.1).
- **Mesa de verificación:** se sacó del modelo.

## 3. Posiciones de los objetos

Todos con Z = 0,30. Los nombres son los que usa el código: no los cambies.

| Objeto | Tipo | X | Y | Origen del dato |
|---|---|---|---|---|
| `Puerta` | Location | 7,98 | −94,50 | Provisorio: extremo sur |
| `Salida` | Location | 10,98 | −94,50 | Provisorio |
| `Caja_Loc1` | Location | 6,72 | −12,41 | **Medido en FlexSim** (puesto de validación 1) |
| `Caja_Loc2` | Location | 9,80 | −12,50 | **Indicado por el grupo** (puesto 2, enfrente) |
| `Cajero1` | Staff | 5,33 | −12,41 | Dentro del cubículo izquierdo |
| `Cajero2` | Staff | 11,23 | −12,50 | Dentro del cubículo derecho |
| `Paso_Central` | Location | 8,25 | −10,10 | Punto de paso: evita atravesar la pared |
| `Mostrador_Loc1` | Location | 2,23 | −8,75 | Entre la pared y el riel |
| `Mostrador_Loc2` | Location | 5,33 | −8,75 | Idem |
| `Mostrador_Loc3` | Location | 8,23 | −8,75 | Idem |
| `Mostrador_Loc4` | Location | 11,23 | −8,75 | Idem |
| `Veg_Loc` | Location | 15,03 | −8,75 | Frente a la mesada vegetariana |
| `Previo_Loc0` | Location | 15,03 | −9,60 | Un paso antes del puesto vegetariano: el último tramo es recto hacia +Y, para llegar mirando al servidor |
| `Previo_Loc1` a `Previo_Loc4` | Location | 2,23 / 5,33 / 8,23 / 11,23 | −9,60 | Un paso antes de cada `Mostrador_Loc` (mismo X, Y = −9,60). Copiá y pegá el `Mostrador_Loc` y cambiá nombre y Y |
| `Servidor1` a `Servidor4` | Staff | 2,23 / 5,33 / 8,23 / 11,23 | −6,15 | Detrás de las cubetas |
| `Fila_Caja` | Waiting Line | ver sección 4 | | |
| `Fila_Servicio` | Waiting Line | ver sección 4 | | |

Rotación Z de los cajeros: el `Cajero1` tiene que mirar hacia +X (hacia el pasillo) y el `Cajero2` hacia −X. Los `Servidor` miran hacia −Y (hacia los clientes). Se prueba con la rotación Z hasta que quede bien.

### 3.1 Escritorios de caja (para apoyar la PC)

Cada uno mide 0,60 × 2,20 m, con la tapa a 0,76 m del piso. En FlexSim la **tapa queda a Z = 1,06** (0,76 + 0,30 del cimiento). Para que la PC no quede en el aire, ponela con ese Z:

| Escritorio | X (m) | Y (m) | Z de la tapa | Sugerencia para la PC |
|---|---|---|---|---|
| Caja 1 (cubículo izquierdo) | 5,88 a 6,48 | −12,60 a −10,40 | 1,06 | X = 6,18 · Y = −12,0 · mirando hacia −X (hacia el cajero) |
| Caja 2 (cubículo derecho) | 9,97 a 10,57 | −12,60 a −10,40 | 1,06 | X = 10,27 · Y = −12,0 · mirando hacia +X |

Los cajeros quedan a unos 0,6 m del escritorio (`Cajero1` en X = 5,33 y `Cajero2` en X = 11,23), así que no hace falta moverlos.

## 4. Las dos filas

| Fila | Puntos (X, Y), del frente al fondo | *Gap Size* | *Single Entry Point* |
|---|---|---|---|
| `Fila_Caja` | (8,33 ; −13,8), (8,33 ; −80) | 0,6 m | Tildado |
| `Fila_Servicio` | (8,25 ; −10,6), (8,25 ; −13,0) | 0,6 m | Tildado |

Si el primer punto es el frente o el fondo es una de las preguntas del laboratorio (L3 de la guía). Si resulta al revés, se invierten los puntos.

**Capacidad.** `Fila_Caja` mide 66 m y entran unas 110 personas, contra las 66 del pico. `Fila_Servicio` mide 2,4 m y entran **unas 4 personas**. La guía suponía 38. Con una fila tan corta, `CapacidadFilaServicio` pasa a ser un valor bajo y **el bloqueo de la caja aparece mucho antes**. Es el supuesto S23 y cambia los resultados: hay que acordar con el referente cómo espera la gente entre la validación y el mostrador (si hace una fila ordenada o espera de pie frente a los tres pasos) antes de fijar el valor.

## 5. Tabla `Ubicaciones`

Una fila por persona del personal. `EstX` y `EstY` son el lugar de espera, fuera del edificio (a la izquierda, con X negativa), para cuando ese puesto no se usa en el escenario.

| Objeto | Rol | Numero | X | Y | Z | EstX | EstY |
|---|---|---|---|---|---|---|---|
| Cajero1 | Cajero | 1 | 5,33 | −12,41 | 0,30 | −4 | −12,41 |
| Cajero2 | Cajero | 2 | 11,23 | −12,50 | 0,30 | −4 | −12,50 |
| Servidor1 | Servidor | 1 | 2,23 | −6,15 | 0,30 | −4 | −6,15 |
| Servidor2 | Servidor | 2 | 5,33 | −6,15 | 0,30 | −4 | −6,15 |
| Servidor3 | Servidor | 3 | 8,23 | −6,15 | 0,30 | −4 | −6,15 |
| Servidor4 | Servidor | 4 | 11,23 | −6,15 | 0,30 | −4 | −6,15 |

Esta tabla es **provisoria**. Por la regla del proyecto, los valores no se editan a mano en FlexSim: cuando se confirmen con el referente hay que pasarlos a `generar_inputs_flexsim.py` y a `supuestos.json`.

## 6. Prueba de la fase 1

Poné primero `Puerta` y `Caja_Loc1`, y mirá que caigan donde corresponde:

- [ ] `Caja_Loc1` queda en el pasillo, pegado al cubículo izquierdo, donde marcaste con la cruz roja
- [ ] `Caja_Loc2` queda enfrente, pegado al cubículo derecho
- [ ] `Puerta` queda en el extremo sur del salón, lejos de los puestos
- [ ] Los cuatro `Mostrador_Loc` quedan del otro lado de la pared de los pasos, frente al riel
- [ ] Los `Servidor` quedan detrás de las cubetas

Si alguno cae en otro lado, avisame: lo más probable es que haya que invertir un signo en Y.
