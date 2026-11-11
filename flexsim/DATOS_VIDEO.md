# Datos para el video

[TOC]

Todos los números de los escenarios salen del **Experimenter de FlexSim**: 12 escenarios × 30 réplicas, un día de 11:40 a 16:00, intervalos de confianza del 95 % (`flexsim/experimenter/RESULTADOS.md`). Se muestra solo el **perfil pico**, que es el que pregunta la consigna.

Cada bloque de abajo es una placa del video. El texto entre comillas es para copiar tal cual.

## Antes de usarlos: una diferencia a resolver

La corrida que se validó (`validacion_E0_Pico.md`, una sola corrida) y el Experimenter **no dan lo mismo en el mostrador**:

| Medida, E0 pico | Corrida validada | Experimenter (30 réplicas) |
|---|---|---|
| Espera media en el mostrador | 7,7 min | 0,016 min (1 s) |
| Cola máxima en el mostrador | 131 personas | 4,8 personas |
| Utilización del servicio | 94 % | no se midió |

Con 3 personas sirviendo y 17,3 s por ración (S15), el mostrador atiende unas 104 raciones cada 10 minutos, menos de las que llegan en el pico. Lo esperable es lo de la corrida validada, con cola en el mostrador. El Experimenter parece haber corrido con un servicio más rápido. Conviene mirar en `comedor_unc_3.fsm` la tabla `TiemposServicio` (fila 2, *Scale* = 17,3) y el Delay `Servir raciones` antes de cerrar el video.

**Mientras tanto, no mezclar las dos fuentes en la misma placa.** Las placas de abajo usan solo el Experimenter, salvo la correlación con lo real, que es parte de la validación.

## Placa 1 · Resultados del escenario base

Título: "Resultados del escenario base"

Subtítulo: "E0 · 1 puesto de caja y 3 personas sirviendo · 30 réplicas"

| Tarjeta | Valor | Fuente |
|---|---|---|
| "Espera máxima en la caja" | **4,9 min** (± 0,2) | Experimenter |
| "Cola máxima en la caja" | **71 personas** (± 3) | Experimenter |
| "Tiempo total medio" | **68 s** (± 5 s) | Experimenter |
| "Cola máxima en el mostrador" | **5 personas** | Experimenter |
| "Utilización de la caja" | **63 %** (barra al 63 %) | Experimenter |
| "Correlación con lo real" | **0,95** | Validación: raciones por franja contra los registros |

Sacar de esta placa la "Espera en la cola previa 13 min", la "Espera en el mostrador 8 min" y la "Utilización del servicio 94 %". Salen de la corrida validada, no del Experimenter (ver arriba).

Pie opcional: "La cola se forma antes de abrir: a las 12:00 ya hay unas 65 personas esperando."

## Placa 2 · Cinco cambios sobre la base

Título: "Cinco cambios sobre la base"

Subtítulo: "En cada uno se modifica una sola cosa, así se sabe qué causa la diferencia."

Las definiciones están confirmadas contra la tabla `Escenarios`. Se puede **quitar** el pie "E4 y E5: definición a confirmar".

| Escenario | Texto | Resultado (reemplaza "Resultado pendiente") |
|---|---|---|
| E1 | "Dos puestos de caja todo el turno" | "Caja: espera máx. 4,9 → 2,4 min · Mostrador: cola 5 → 31" |
| E2 | "Dos puestos solo en el pico, de 12:00 a 13:30" | "Igual que E1: el pico es lo único que pesa" |
| E3 | "Validación por código QR: 60 % del tiempo del DNI" | "Caja: espera máx. 4,9 → 2,9 min · Mostrador: cola 5 → 23" |
| E4 | "Un puesto de caja y cuatro personas sirviendo" | "La caja no cambia (4,9 min): el cuello está en la caja" |
| E5 | "Dos puestos y cuatro personas sirviendo" | "Caja: espera máx. 4,9 → 2,4 min · Mostrador: cola 5 → 16" |

Versión corta, si el recuadro es chico:

| Escenario | Resultado corto |
|---|---|
| E1 | "La cola pasa al mostrador" |
| E2 | "Igual que E1" |
| E3 | "Mejora la caja, la cola pasa al mostrador" |
| E4 | "No cambia nada" |
| E5 | "Mejor tiempo total" |

## Placa 3 · Los seis escenarios, uno al lado del otro

Título: "Los seis escenarios, uno al lado del otro"

Subtítulo: "Tiempo total medio, con su intervalo de confianza del 95 %"

Barras en **segundos**:

| Escenario | Media | Intervalo 95 % |
|---|---|---|
| E0 base | 68 s | 63 a 74 s |
| E1 | 59 s | 54 a 63 s |
| E2 | 59 s | 55 a 64 s |
| E3 | 58 s | 53 a 62 s |
| E4 | 68 s | 62 a 73 s |
| E5 | **55 s** | 52 a 59 s |

```grafico
tipo: barras
titulo: Tiempo total medio, perfil pico
unidad: s

Escenario, Tiempo total
E0, 68
E1, 59
E2, 59
E3, 58
E4, 68
E5, 55
```

Pie (reemplaza "Cada barra se completa..."): "30 réplicas por escenario, con las mismas personas en todos. Las diferencias de E1, E2, E3 y E5 con la base son significativas."

Si se quiere una segunda barra por escenario, la que mejor cuenta la historia es la **cola máxima en el mostrador**:

```grafico
tipo: barras
titulo: Cola máxima en el mostrador, perfil pico
unidad: personas

Escenario, Cola máxima
E0, 5
E1, 31
E2, 31
E3, 23
E4, 3
E5, 16
```

## Placa 4 · La pregunta del principio

Pregunta (ya está en la placa): "¿Qué combinación de puestos de validación y personas en el servicio reduce el tiempo total en el pico, sin trasladar la cola al mostrador?"

Respuesta, en el recuadro:

"**Dos puestos de caja y cuatro personas sirviendo (E5).**"

"Es el menor tiempo total: 55 s contra 68 s de hoy (−13 s, −19 %)."

"Agregar solo un puesto (E1) corre la cola al mostrador: pasa de 5 a 31 personas. Sumar la cuarta persona en el servicio la baja a 16."

"Agregar solo gente en el servicio (E4) no cambia nada: el cuello de botella está en la caja."

Si entra una sola línea: "Dos puestos de caja y cuatro personas sirviendo: −19 % de tiempo total, y la mitad de cola en el mostrador que con solo dos puestos."

## Comparaciones para citar en la voz en off

Diferencias pareadas, perfil pico (escenario menos base), todas significativas:

| Comparación | Tiempo total | Espera máxima en la caja | Cola máxima en el mostrador |
|---|---|---|---|
| E1 contra E0 | −10 s | −2,5 min | +26 personas |
| E3 contra E0 | −11 s | −2,0 min | +18 personas |
| E4 contra E0 | −1 s | sin cambio | −2 personas |
| E5 contra E0 | −13 s | −2,5 min | +11 personas |
| E5 contra E1 | −4 s | sin cambio | −15 personas |

## Cómo se comparó (una placa o una frase)

"Usamos el Experimenter de FlexSim: 6 escenarios, 30 réplicas de un día cada uno, con los mismos números aleatorios en todos. Así cada escenario atiende exactamente a las mismas personas, y la diferencia se debe solo al cambio."
