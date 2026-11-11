# Resultados del Experimenter

[TOC]

Generado con `analisis/procesar_experimenter.py` a partir de `flexsim/experimenter/ReporteCompleto.html`. Son 12 escenarios por 30 réplicas, simulación terminante de un día (11:40 a 16:00, calentamiento 0). Los intervalos son de confianza al 95 % con la t de Student. Las réplicas por escenario comparten los mismos números aleatorios (las personas del día son idénticas entre escenarios del mismo perfil), por eso las comparaciones son **pareadas**.

## Perfil pico

Media de las réplicas, con el semiancho del intervalo de confianza al 95 % (±).

| Escenario | Tiempo total medio en el sistema (min) | Espera máxima en la caja desde la apertura (min) | Espera media en la fila de servicio (min) | Tiempo con la caja bloqueada (min) | Utilización de la caja (%) | Cola máxima en la caja (personas) | Cola máxima en el servicio (personas) |
|---|---|---|---|---|---|---|---|
| E0 | 1,14 ± 0,09 | 4,89 ± 0,23 | 0,016 ± 0,001 | 0,00 ± 0,00 | 62,5 ± 0,8 | 70,6 ± 2,5 | 4,8 ± 0,5 |
| E1 | 0,98 ± 0,07 | 2,42 ± 0,11 | 0,086 ± 0,014 | 0,00 ± 0,00 | 31,2 ± 0,4 | 70,5 ± 2,5 | 30,8 ± 1,9 |
| E2 | 0,99 ± 0,07 | 2,42 ± 0,11 | 0,084 ± 0,014 | 0,00 ± 0,00 | 31,2 ± 0,4 | 70,5 ± 2,5 | 30,8 ± 1,9 |
| E3 | 0,96 ± 0,07 | 2,93 ± 0,14 | 0,069 ± 0,012 | 0,00 ± 0,00 | 37,5 ± 0,5 | 70,6 ± 2,5 | 22,7 ± 2,2 |
| E4 | 1,13 ± 0,09 | 4,89 ± 0,23 | 0,004 ± 0,001 | 0,00 ± 0,00 | 62,5 ± 0,8 | 70,6 ± 2,5 | 3,1 ± 0,2 |
| E5 | 0,92 ± 0,06 | 2,42 ± 0,11 | 0,027 ± 0,004 | 0,00 ± 0,00 | 31,2 ± 0,4 | 70,5 ± 2,5 | 16,2 ± 1,7 |

### Comparaciones pareadas, perfil pico

Diferencia media (escenario menos base) con su intervalo. **Significativa** si el intervalo no incluye el cero.

| Comparación | Medida | Diferencia media | Intervalo 95 % | ¿Significativa? |
|---|---|---|---|---|
| E1 contra E0: segundo puesto todo el turno | Tiempo total medio en el sistema (min) | -0,16 | [-0,20; -0,13] | sí |
| E1 contra E0: segundo puesto todo el turno | Espera máxima en la caja desde la apertura (min) | -2,47 | [-2,58; -2,35] | sí |
| E1 contra E0: segundo puesto todo el turno | Espera media en la fila de servicio (min) | 0,069 | [0,056; 0,083] | sí |
| E1 contra E0: segundo puesto todo el turno | Cola máxima en el servicio (personas) | 26,0 | [24,1; 27,9] | sí |
| E2 contra E0: segundo puesto de 12:00 a 13:30 | Tiempo total medio en el sistema (min) | -0,15 | [-0,18; -0,12] | sí |
| E2 contra E0: segundo puesto de 12:00 a 13:30 | Espera máxima en la caja desde la apertura (min) | -2,47 | [-2,58; -2,35] | sí |
| E2 contra E0: segundo puesto de 12:00 a 13:30 | Espera media en la fila de servicio (min) | 0,068 | [0,055; 0,082] | sí |
| E2 contra E0: segundo puesto de 12:00 a 13:30 | Cola máxima en el servicio (personas) | 26,0 | [24,1; 27,9] | sí |
| E3 contra E0: validación por QR | Tiempo total medio en el sistema (min) | -0,18 | [-0,21; -0,14] | sí |
| E3 contra E0: validación por QR | Espera máxima en la caja desde la apertura (min) | -1,96 | [-2,05; -1,87] | sí |
| E3 contra E0: validación por QR | Espera media en la fila de servicio (min) | 0,053 | [0,041; 0,064] | sí |
| E3 contra E0: validación por QR | Cola máxima en el servicio (personas) | 17,9 | [15,7; 20,1] | sí |
| E4 contra E0: 4.ª persona sirviendo | Tiempo total medio en el sistema (min) | -0,01 | [-0,01; -0,01] | sí |
| E4 contra E0: 4.ª persona sirviendo | Espera máxima en la caja desde la apertura (min) | 0,00 | [0,00; 0,00] | no |
| E4 contra E0: 4.ª persona sirviendo | Espera media en la fila de servicio (min) | -0,012 | [-0,013; -0,011] | sí |
| E4 contra E0: 4.ª persona sirviendo | Cola máxima en el servicio (personas) | -1,7 | [-2,2; -1,2] | sí |
| E5 contra E0: segundo puesto y 4.ª persona | Tiempo total medio en el sistema (min) | -0,22 | [-0,27; -0,18] | sí |
| E5 contra E0: segundo puesto y 4.ª persona | Espera máxima en la caja desde la apertura (min) | -2,47 | [-2,58; -2,35] | sí |
| E5 contra E0: segundo puesto y 4.ª persona | Espera media en la fila de servicio (min) | 0,011 | [0,007; 0,015] | sí |
| E5 contra E0: segundo puesto y 4.ª persona | Cola máxima en el servicio (personas) | 11,3 | [9,7; 12,9] | sí |
| E5 contra E1: sumar la 4.ª persona al segundo puesto | Tiempo total medio en el sistema (min) | -0,06 | [-0,07; -0,05] | sí |
| E5 contra E1: sumar la 4.ª persona al segundo puesto | Espera máxima en la caja desde la apertura (min) | 0,00 | [0,00; 0,00] | no |
| E5 contra E1: sumar la 4.ª persona al segundo puesto | Espera media en la fila de servicio (min) | -0,059 | [-0,069; -0,049] | sí |
| E5 contra E1: sumar la 4.ª persona al segundo puesto | Cola máxima en el servicio (personas) | -14,6 | [-15,7; -13,6] | sí |

## Perfil bajo

Media de las réplicas, con el semiancho del intervalo de confianza al 95 % (±).

| Escenario | Tiempo total medio en el sistema (min) | Espera máxima en la caja desde la apertura (min) | Espera media en la fila de servicio (min) | Tiempo con la caja bloqueada (min) | Utilización de la caja (%) | Cola máxima en la caja (personas) | Cola máxima en el servicio (personas) |
|---|---|---|---|---|---|---|---|
| E0 | 0,98 ± 0,08 | 2,54 ± 0,19 | 0,005 ± 0,001 | 0,00 ± 0,00 | 28,1 ± 0,5 | 36,5 ± 2,8 | 3,2 ± 0,4 |
| E1 | 0,93 ± 0,08 | 1,25 ± 0,10 | 0,035 ± 0,008 | 0,00 ± 0,00 | 14,0 ± 0,2 | 36,5 ± 2,8 | 16,1 ± 1,9 |
| E2 | 0,93 ± 0,08 | 1,25 ± 0,10 | 0,035 ± 0,008 | 0,00 ± 0,00 | 14,0 ± 0,2 | 36,5 ± 2,8 | 16,1 ± 1,9 |
| E3 | 0,91 ± 0,08 | 1,52 ± 0,12 | 0,027 ± 0,006 | 0,00 ± 0,00 | 16,8 ± 0,3 | 36,5 ± 2,8 | 11,9 ± 1,6 |
| E4 | 0,97 ± 0,08 | 2,54 ± 0,19 | 0,002 ± 0,001 | 0,00 ± 0,00 | 28,1 ± 0,5 | 36,5 ± 2,8 | 2,2 ± 0,3 |
| E5 | 0,91 ± 0,07 | 1,25 ± 0,10 | 0,014 ± 0,004 | 0,00 ± 0,00 | 14,0 ± 0,2 | 36,5 ± 2,8 | 9,2 ± 1,4 |

### Comparaciones pareadas, perfil bajo

Diferencia media (escenario menos base) con su intervalo. **Significativa** si el intervalo no incluye el cero.

| Comparación | Medida | Diferencia media | Intervalo 95 % | ¿Significativa? |
|---|---|---|---|---|
| E1 contra E0: segundo puesto todo el turno | Tiempo total medio en el sistema (min) | -0,05 | [-0,05; -0,04] | sí |
| E1 contra E0: segundo puesto todo el turno | Espera máxima en la caja desde la apertura (min) | -1,29 | [-1,39; -1,20] | sí |
| E1 contra E0: segundo puesto todo el turno | Espera media en la fila de servicio (min) | 0,030 | [0,023; 0,038] | sí |
| E1 contra E0: segundo puesto todo el turno | Cola máxima en el servicio (personas) | 12,9 | [11,1; 14,7] | sí |
| E2 contra E0: segundo puesto de 12:00 a 13:30 | Tiempo total medio en el sistema (min) | -0,04 | [-0,05; -0,04] | sí |
| E2 contra E0: segundo puesto de 12:00 a 13:30 | Espera máxima en la caja desde la apertura (min) | -1,29 | [-1,39; -1,20] | sí |
| E2 contra E0: segundo puesto de 12:00 a 13:30 | Espera media en la fila de servicio (min) | 0,030 | [0,023; 0,037] | sí |
| E2 contra E0: segundo puesto de 12:00 a 13:30 | Cola máxima en el servicio (personas) | 12,9 | [11,2; 14,7] | sí |
| E3 contra E0: validación por QR | Tiempo total medio en el sistema (min) | -0,07 | [-0,07; -0,06] | sí |
| E3 contra E0: validación por QR | Espera máxima en la caja desde la apertura (min) | -1,02 | [-1,10; -0,94] | sí |
| E3 contra E0: validación por QR | Espera media en la fila de servicio (min) | 0,022 | [0,016; 0,027] | sí |
| E3 contra E0: validación por QR | Cola máxima en el servicio (personas) | 8,7 | [7,2; 10,1] | sí |
| E4 contra E0: 4.ª persona sirviendo | Tiempo total medio en el sistema (min) | -0,00 | [-0,00; -0,00] | sí |
| E4 contra E0: 4.ª persona sirviendo | Espera máxima en la caja desde la apertura (min) | 0,00 | [0,00; 0,00] | no |
| E4 contra E0: 4.ª persona sirviendo | Espera media en la fila de servicio (min) | -0,003 | [-0,004; -0,002] | sí |
| E4 contra E0: 4.ª persona sirviendo | Cola máxima en el servicio (personas) | -1,0 | [-1,3; -0,7] | sí |
| E5 contra E0: segundo puesto y 4.ª persona | Tiempo total medio en el sistema (min) | -0,07 | [-0,08; -0,06] | sí |
| E5 contra E0: segundo puesto y 4.ª persona | Espera máxima en la caja desde la apertura (min) | -1,29 | [-1,39; -1,20] | sí |
| E5 contra E0: segundo puesto y 4.ª persona | Espera media en la fila de servicio (min) | 0,009 | [0,006; 0,012] | sí |
| E5 contra E0: segundo puesto y 4.ª persona | Cola máxima en el servicio (personas) | 6,0 | [4,8; 7,1] | sí |
| E5 contra E1: sumar la 4.ª persona al segundo puesto | Tiempo total medio en el sistema (min) | -0,02 | [-0,03; -0,02] | sí |
| E5 contra E1: sumar la 4.ª persona al segundo puesto | Espera máxima en la caja desde la apertura (min) | 0,00 | [0,00; 0,00] | no |
| E5 contra E1: sumar la 4.ª persona al segundo puesto | Espera media en la fila de servicio (min) | -0,022 | [-0,026; -0,017] | sí |
| E5 contra E1: sumar la 4.ª persona al segundo puesto | Cola máxima en el servicio (personas) | -6,9 | [-7,8; -6,1] | sí |

### Espera máxima en la caja (min), perfil pico

```grafico
tipo: barras
titulo: Espera máxima en la caja (min), perfil pico
unidad: min

Escenario, Media
E0, 4.886
E1, 2.416
E2, 2.417
E3, 2.927
E4, 4.886
E5, 2.416
```

### Cola máxima en el servicio (personas), perfil pico

```grafico
tipo: barras
titulo: Cola máxima en el servicio (personas), perfil pico
unidad: personas

Escenario, Media
E0, 4.833
E1, 30.800
E2, 30.833
E3, 22.733
E4, 3.133
E5, 16.167
```

### Tiempo total medio (min), perfil pico

```grafico
tipo: barras
titulo: Tiempo total medio (min), perfil pico
unidad: min

Escenario, Media
E0, 1.141
E1, 0.978
E2, 0.991
E3, 0.964
E4, 1.129
E5, 0.919
```

## Réplicas necesarias

Semiancho relativo del intervalo (semiancho dividido por la media) con las 30 réplicas. Si es menor que 5 % la precisión alcanza; si es mayor, hay que subir las réplicas con $n \approx (t\,s/h)^2$.

| Medida | Peor semiancho relativo (pico) | Escenario |
|---|---|---|
| Tiempo total medio en el sistema | 8,3 % | E4 |
| Espera máxima en la caja desde la apertura | 4,7 % | E2 |
| Espera media en la fila de servicio | 17,2 % | E3 |
| Tiempo con la caja bloqueada | 0,0 % |  |
| Utilización de la caja | 1,3 % | E3 |
| Cola máxima en la caja | 3,6 % | E0 |
| Cola máxima en el servicio | 10,3 % | E5 |

