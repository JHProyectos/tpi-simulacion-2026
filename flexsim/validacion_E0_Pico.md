# Validación del modelo: E0_Pico

[TOC]

Corrida exportada en `salidas.xlsx`: 1369 personas, 1522 raciones, apertura a t = 1314 s. Generado con `analisis/validar_modelo.py`.

## 1. Verificación interna

| Chequeo | Resultado | Estado |
|---|---|---|
| Los tiempos de cada persona van en orden (llegada ≤ inicio caja ≤ fin caja ≤ fila servicio ≤ inicio servicio ≤ salida) | todas las personas | OK |
| Personas del día (esperadas 1381, tolerancia ±109: 3 desvíos de un Poisson) | 1369 | OK |
| Raciones del día (esperadas 1546, tolerancia ±5 %) | 1522 | OK |
| Salida_Franjas coincide con las raciones que se calculan desde Salida_Personas | coinciden | OK |
| ColaCajaMax de Salida_Dia coincide con la calculada desde Salida_Personas | tabla 66, personas 66 | OK |
| Al final de la corrida no queda nadie en la fila de caja ni en la de servicio | EnFilaCaja 0, EnFilaServicio 0 | OK |
| Todos salen antes de las 16:00 (t = 15600) | última salida a t = 10714 s | OK |

## 2. Contra los datos reales

| Chequeo | Resultado | Estado |
|---|---|---|
| Curva de raciones por franja: correlación con la real (mínimo 0.9) | 0.946 | OK |
| Error relativo medio por franja, sin la última (máximo 15%) | 10.0% | OK |
| Total de raciones contra el real (±5%) | -1.5% | OK |
| Franjas fuera del rango de los días reales (máximo 2 de 16) | 0 | OK |
| Cola máxima en la caja (S10: 60 a 70 personas; aceptable 55 a 75) | 66 | OK |
| Espera media de la cola previa (S10: 10 a 15 min) | 13.0 min | OK |

Curva de raciones validadas por franja de 10 minutos desde las 12:00:

```grafico
tipo: lineas
titulo: Raciones por franja, Pico (E0_Pico)
unidad: raciones

Franja, Registros reales, Modelo
12:00, 103.5, 100.0
12:10, 134.9, 109.0
12:20, 124.8, 132.0
12:30, 119.3, 126.0
12:40, 117.8, 115.0
12:50, 104.6, 98.0
13:00, 119.3, 118.0
13:10, 126.9, 136.0
13:20, 119.8, 123.0
13:30, 99.0, 94.0
13:40, 75.4, 94.0
13:50, 75.5, 68.0
14:00, 72.4, 87.0
14:10, 81.7, 70.0
14:20, 62.4, 49.0
14:30, 8.4, 3.0
```

| Franja | Real (media) | Modelo | Mín real | Máx real |
|---|---|---|---|---|
| 12:00 | 103.4 | 100.0 | 61 | 139 |
| 12:10 | 134.9 | 109.0 | 100 | 168 |
| 12:20 | 124.8 | 132.0 | 104 | 161 |
| 12:30 | 119.3 | 126.0 | 97 | 144 |
| 12:40 | 117.8 | 115.0 | 83 | 148 |
| 12:50 | 104.6 | 98.0 | 80 | 121 |
| 13:00 | 119.3 | 118.0 | 90 | 138 |
| 13:10 | 126.9 | 136.0 | 111 | 146 |
| 13:20 | 119.8 | 123.0 | 89 | 145 |
| 13:30 | 99.0 | 94.0 | 59 | 132 |
| 13:40 | 75.4 | 94.0 | 54 | 104 |
| 13:50 | 75.6 | 68.0 | 31 | 104 |
| 14:00 | 72.4 | 87.0 | 57 | 98 |
| 14:10 | 81.7 | 70.0 | 56 | 100 |
| 14:20 | 62.4 | 49.0 | 38 | 115 |
| 14:30 | 8.4 | 3.0 | 2 | 46 |

La primera franja da menos que la real porque la caja abre con demora (S25). El último valor corresponde a las 14:30, con muy pocas llegadas.

## 3. Contra la réplica independiente (30 réplicas)

Una corrida de FlexSim es una sola muestra: se acepta si queda a menos de 2 desvíos estándar de la media de la réplica. Con 12 indicadores, es esperable que alguno salga apenas del rango por azar.

| Indicador | FlexSim | Réplica (media) | Desvío | z | Estado |
|---|---|---|---|---|---|
| Personas | 1369 | 1372.1 | 31.6 | -0.1 | OK |
| Raciones | 1522 | 1537.3 | 36.9 | -0.4 | OK |
| EsperaCaja_min | 0.8 | 0.9 | 0.2 | -0.6 | OK |
| EsperaColaPrevia_min | 13.0 | 14.3 | 2.4 | -0.5 | OK |
| EsperaCajaDesdeApertura_min | 0.2 | 0.3 | 0.1 | -0.6 | OK |
| EsperaCajaDesdeAperturaMax_min | 4.7 | 4.9 | 0.6 | -0.4 | OK |
| ColaCajaMax | 66 | 70.9 | 6.5 | -0.7 | OK |
| EsperaServicio_min | 7.7 | 9.9 | 2.9 | -0.8 | OK |
| EsperaServicioMax_min | 86.3 | 17.2 | 3.6 | 19.3 | REVISAR |
| ColaServicioMax | 131 | 157.5 | 34.5 | -0.8 | OK |
| UtilCaja_pct | 62.6 | 61.9 | 1.8 | 0.4 | OK |
| UtilServicio_pct | 93.6 | 94.7 | 2.6 | -0.5 | OK |

## 4. Ley de Little

| Cálculo | Valor |
|---|---|
| L = Σ espera / T, desde Salida_Personas | 3.96 personas |
| L = N · W / T | 3.96 personas |

Las dos primeras filas son el mismo cálculo y no prueban nada por sí solas: lo que valida es contrastarlas con el contenido medio que mide FlexSim en `Esperar en la fila` (opción `--little`).

## 5. Resumen

1 chequeo(s) para revisar.
