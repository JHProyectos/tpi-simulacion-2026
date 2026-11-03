# Uso de IA en el TPI: qué se hizo, con qué scripts y cómo se verificó

[TOC]

Documento para la declaración de IA de la entrega (sección 12). Cuenta qué parte del trabajo hizo la IA (Claude, de Anthropic, usado a través de Claude Code), qué hizo el grupo, qué scripts existen y cómo se comprobó que lo producido por la IA es correcto. Vale lo mismo para los datos: **ningún dato generado por IA está mezclado con los reales sin marcar**.

## 1. Reparto del trabajo

| Tarea | Quién |
|---|---|
| Relevamiento en el comedor, observaciones de campo y estimaciones del referente (S01, S05, S06, S10, S15, S20, S22) | Grupo |
| Decisiones de alcance y del problema (D01 a D06) | Grupo |
| Armado del modelo en FlexSim, corridas y exportación de resultados | Grupo |
| Dibujo del comedor en SketchUp y escena 3D | Grupo |
| Procesamiento de los registros reales (`data/real/`), tiempos de validación y tasas de llegada | IA, con scripts que el grupo puede correr de nuevo |
| Datos sintéticos (ausentismo, cancelaciones, retiro múltiple, QR, menú vegetariano) | IA, cada uno con su supuesto y su base escritos |
| Registro de supuestos (`supuestos/`), tablas de entrada de FlexSim y guías paso a paso | IA, revisado por el grupo |
| Réplica del modelo en Python y script de validación | IA |
| Razonamiento sobre los resultados (por ejemplo, por qué el mostrador no alcanzaba) | IA propone, el grupo decide |

La IA **no tiene acceso a FlexSim**: no corre el modelo. Las corridas las hace el grupo y la IA analiza lo que se exporta (`flexsim/salidas.xlsx`).

## 2. Scripts de Python

Todos están en `analisis/` y se corren desde la raíz del proyecto. Requieren Python 3 con `pandas`, `numpy` y `openpyxl`.

| Script | Qué hace | Entra | Sale |
|---|---|---|---|
| `tiempo_validacion.py` | Estima el tiempo de validación por DNI a partir de los intervalos entre check-ins en las franjas saturadas (S07) | `data/real/` | `data/procesado/intervalos_saturados.csv` |
| `generar_datos.py` | Completa el dataset con las filas sintéticas de ausentismo y cancelaciones (S11, S12), sin tocar las reales | `data/real/`, `supuestos/supuestos.json` | `data/generado/`, `data/final/reservas_completo.csv` |
| `organizar_por_tipo.py` | Organiza el dataset por tipo de cliente y arma la página `web/index.html` | `data/final/` | `reporte/datos.json`, `web/index.html` |
| `render_supuestos.py` | Genera `SUPUESTOS.md` a partir de `supuestos.json` (la fuente única) | `supuestos/supuestos.json` | `supuestos/SUPUESTOS.md` |
| `generar_inputs_flexsim.py` | Genera las tablas que se importan a FlexSim: llegadas por franja, cola previa, mezcla de tipos, tiempos, escenarios | datos y supuestos | `flexsim/inputs.xlsx` |
| `referencia_modelo.py` | **Réplica independiente del modelo** en Python con las mismas tablas. Da el orden de magnitud de cada escenario | `flexsim/inputs.xlsx` | tablas en pantalla |
| `validar_modelo.py` | Valida una corrida de FlexSim de tres maneras (sección 5) | `flexsim/salidas.xlsx` | `flexsim/validacion_<escenario>.md` |

Regla de trabajo: **los valores no se editan a mano en las tablas**. Se cambian en `supuestos.json`, se corre `render_supuestos.py` y `generar_inputs_flexsim.py`, y se reimporta. Así la tabla de FlexSim, el supuesto escrito y la réplica siempre dicen lo mismo.

## 3. Datos generados con IA

La cátedra permite datos generados con IA si se declara la fuente y la base de cada valor. En `supuestos/supuestos.json` cada supuesto tiene `origen` (registro, referente, derivado de registros o generado), `base`, `estado` y rango de sensibilidad. Los generados son:

| Supuesto | Valor | Estado |
|---|---|---|
| S09 | Cola formada antes de la apertura (65 en el pico, 30 en el bajo) | Aceptado, a calibrar |
| S11 | Ausentismo | Propuesto |
| S12 | Cancelaciones definitivas | Propuesto |
| S21 | Retiro de más de una ración por persona (1,25 y 1,05 raciones por persona) | Propuesto |
| S24 | Validación con QR: 60 % del tiempo actual | Propuesto |
| S27 | 12 % pide menú vegetariano | Propuesto |

El **tiempo de servicio (S15)** es una estimación del referente que el grupo ajustó el 14/10 de 15–30 s a **15–20 s** (mediana 17,3 s, sigma 0,09). Sigue como «propuesto» hasta que se cronometre solo el servir.

Los datos reales (`data/real/`) están **sin modificar**. Las filas sintéticas del dataset final llevan `origen_fila = generado_ia`.

## 4. Cómo se verifica lo que hace la IA

1. **Réplica independiente.** `referencia_modelo.py` reimplementa la lógica del modelo con otra herramienta. Si FlexSim y la réplica dan lo mismo, es difícil que ambos tengan el mismo error de armado.
2. **Tres niveles de validación** con `validar_modelo.py`:
   - *Verificación interna:* los tiempos de cada persona van en orden, las tablas de salida coinciden entre sí, la cola termina vacía.
   - *Contra la realidad:* la curva de raciones por franja contra los registros, y la cola y la espera contra lo que observó el referente (S10).
   - *Contra la réplica:* una corrida de FlexSim tiene que caer dentro de lo que dan 30 réplicas de Python (z entre −2 y 2).
3. **Umbrales declarados.** Los límites de aceptación están como constantes al principio del script. Son una propuesta del grupo: se pueden ajustar, pero hay que declararlos en el informe.
4. **Todo es reproducible.** Mismos datos y misma semilla dan los mismos resultados.

## 5. Resultado de la validación del 14/10 (E0_Pico, 17,3 s por ración)

Corrida de FlexSim exportada a `flexsim/salidas.xlsx`: 1.369 personas y 1.522 raciones. Informe completo en [`flexsim/validacion_E0_Pico.md`](flexsim/validacion_E0_Pico.md).

| Nivel | Resultado |
|---|---|
| Verificación interna | 7 de 7 chequeos en orden |
| Contra la realidad | 6 de 6: correlación de la curva 0,946; error medio por franja 10,0 %; total de raciones −1,5 %; cola máxima en la caja 66 (objetivo 60 a 70); espera de la cola previa 13,0 min (objetivo 10 a 15) |
| Contra la réplica | 11 de 12 dentro del rango |

| Indicador | FlexSim | Réplica (media de 30) |
|---|---|---|
| Cola máxima en la caja | 66 | 70,9 |
| Cola máxima en el mostrador | 131 | 157,5 |
| Espera media en el mostrador | 7,7 min | 9,9 min |
| Uso del servicio | 93,6 % | 94,7 % |

### Hallazgo: los vegetarianos esperan mucho más

El único chequeo que no pasó es la **espera máxima en el mostrador: 86 min en FlexSim contra 17 min en la réplica**. Mirando `Salida_Personas`:

| Menú | Personas | Espera media en el mostrador | Espera máxima |
|---|---|---|---|
| No vegetariano | 1.223 | 3,1 min | 6,7 min |
| Vegetariano | 147 | **45,0 min** | **86,3 min** |

**Causa probable:** en el modelo, quien pide menú vegetariano toma primero `PuestoVeg` y *después* hace fila para conseguir una de las 3 personas (`ServicioComida`). Mientras espera a esa persona, que puede demorar varios minutos en el pico, **retiene `PuestoVeg`** y los demás vegetarianos no pueden ni empezar. La réplica reserva las dos cosas a la vez, y por eso no tiene el problema. Es un defecto del armado, no un resultado del comedor.

**Corrección propuesta:** invertir el orden. Todos toman primero `Esperar Servidor`; después un Decide `¿Es vegetariano?` manda a los vegetarianos a `Esperar puesto vegetariano` antes de `Empieza el servicio`. `Acquire Resource` de FlexSim no admite pedir dos recursos en una sola actividad, así que no se pueden reservar a la vez; con este orden el único riesgo es que un vegetariano retenga un servidor mientras espera a `PuestoVeg`, y como los vegetarianos son el 12 % y el puesto se usa alrededor de un tercio del tiempo, ese tiempo es corto. Ya no hay riesgo de que se trabe, porque nadie toma los dos recursos en el orden contrario. **No está probada en FlexSim todavía.**

Esto no cambia las conclusiones sobre las colas de la caja (66 contra 70,9 de la réplica), pero **hay que corregirlo antes de correr E0 a E5 para el informe**, porque afecta el tiempo total de los vegetarianos.

## 6. Cómo reproducir

```bash
python analisis/render_supuestos.py
python analisis/generar_inputs_flexsim.py
python analisis/referencia_modelo.py 30
python analisis/validar_modelo.py --escenario E0_Pico
```

## 7. Límites

- La réplica es una verificación, no una validación: usa la misma lógica y las mismas tablas, así que confirma el armado, no que el modelo represente al comedor.
- Los datos generados (S09, S11, S12, S21, S24, S27) y el tiempo de servicio (S15) son supuestos. Los resultados dependen de ellos y hay que presentarlos con el análisis de sensibilidad.
- La validación contra la realidad se apoya en los registros de validaciones (por franja) y en la estimación del referente (cola de 60 a 70 y espera de 10 a 15 minutos). No hay mediciones del servicio ni de la caminata hasta el mostrador.

## 8. Texto sugerido para la sección 12 de la entrega

> Se usó Claude (Anthropic), a través de Claude Code, como apoyo en: el procesamiento de los registros reales del comedor, la generación de los datos sintéticos declarados en el registro de supuestos (S09, S11, S12, S21, S24 y S27), la redacción del registro de supuestos y de las guías de armado, y la programación de los scripts de Python de `analisis/`: tablas de entrada, réplica del modelo y validación. Cada dato generado tiene su base escrita y está marcado como tal, y los datos reales no se modificaron. La IA no corrió el modelo: las corridas en FlexSim y las decisiones de alcance las hizo el grupo. Los resultados de FlexSim se verificaron contra una réplica independiente en Python y contra los registros reales; los criterios de aceptación y los defectos encontrados están en `flexsim/validacion_E0_Pico.md` y en `AYUDA_IA.md`.
