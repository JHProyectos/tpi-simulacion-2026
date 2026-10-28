# Eje 6. Análisis de datos e implantación

Vamos con el eje seis, análisis de datos e implantación. Este repaso dura unos treinta minutos.

Lo primero: de este eje entra solo la teoría, casi toda en multiple choice, con alguna posible pregunta de desarrollo.

¿Y qué sacó el profe? Todas las fórmulas de cálculo, las distribuciones una por una, las pruebas de Kolmogorov-Smirnov y chi cuadrado con sus dos ejemplos, y todo lo de FlexSim. Eso no lo estudies: se evalúan los conceptos.

Si te llevás cuatro ideas, que sean estas.

La primera: el promedio solo no alcanza, y la distribución de entrada se elige combinando histograma, medidas descriptivas y prueba de bondad de ajuste.

La segunda: no rechazar una hipótesis no demuestra nada.

La tercera: una corrida es un futuro posible, no la respuesta. Por eso hay réplicas, intervalos de confianza y, en sistemas no terminantes, warm-up.

Y la cuarta: verificar, validar e implantar son cosas distintas, y la implantación va por etapas, con piloto.

## Datos de entrada

Antes de arrancar, el mapa del eje: primero, datos de entrada; después, planeación táctica; después, validación y análisis; y por último, implantación.

La primera etapa tiene su propio recorrido, que el apunte llama flujo general: del sistema real se recolectan los datos, se preparan, se analizan con medidas y gráficos, se comparan con distribuciones candidatas y, al final, se decide cuál usar. Abajo lo tenés dibujado.

![Recorrido del eje seis](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/material/img/eje6-recorrido.svg)

*Figura 1. Arriba, las cuatro etapas del eje. Abajo, el flujo de los datos de entrada, del sistema real a la decisión.*

### Qué medir y cómo preparar los datos

Un modelo bien armado da resultados poco confiables si los datos de entrada están mal medidos. Es como una receta perfecta con ingredientes vencidos.

El ejemplo del apunte: la atención media es de cinco minutos, y alguien carga todas las atenciones como cinco minutos fijos. ¿Qué perdió? La variabilidad, que es justamente lo que genera las colas.

Dos sistemas con el mismo promedio se comportan muy distinto si uno varía poco y el otro mucho. Pensá en un río de un metro de profundidad promedio: igual te ahogás si en el medio tiene tres.

Así se ven dos cajas con la misma atención media de cinco minutos. La A casi siempre tarda entre cuatro y seis; la B va de uno a nueve. Con la B, cada tanto se juntan varias atenciones largas, y ahí se arma la cola.

![Dos cajas con la misma media](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/37acd8b34578a4dc1e22ead737868dc209b3150c/material/img/eje6-dos-cajas.svg)

*Figura 2. Misma media, distinta dispersión: cuanto más ancha la curva, más atenciones largas y más cola.*

¿Qué se mide? Las variables aleatorias que cambian la congestión: tiempos entre llegadas, de servicio, cantidades, y tiempos de falla y reparación.

Y la muestra tiene que ser representativa: distintos momentos, días y condiciones, no diez casos cómodos. Un restaurante no se evalúa yendo solo un martes a la tarde.

Preparar es, primero, unificar unidades. Después, sacar duplicados, revisar valores imposibles, como tiempos negativos, y ordenar. Y por último, separar por tipo cuando corresponda: en una mesa de ayuda, pedidos rápidos y lentos mezclados dan una distribución sin sentido. Es como promediar una bici con un auto.

Mirá cómo queda la distribución de esa mesa de ayuda con los dos tipos juntos: dos jorobas, una por tipo. La media cae en el valle del medio, justo donde casi no hay pedidos. Ninguna distribución conocida describe eso; separados, cada tipo tiene la suya.

![Curva bimodal](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/37acd8b34578a4dc1e22ead737868dc209b3150c/material/img/eje6-bimodal.svg)

*Figura 3. Dos tipos mezclados: dos modas, y una media en la zona donde casi no hay pedidos.*

Un outlier es un dato muy alejado del resto, y no siempre se elimina. Puede ser un error de carga o un caso real, como el cliente que tardó muchísimo por un problema con el pago.

Con los faltantes, igual: si son pocos, se descartan; si son muchos, se vuelve a medir.

¿Cómo ves los atípicos? Con el boxplot. La caja tiene el cincuenta por ciento central, entre el primer y el tercer cuartil, y la línea de adentro es la mediana. Lo que queda afuera de los bigotes son posibles outliers.

![Boxplot de tiempos de atención](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/37acd8b34578a4dc1e22ead737868dc209b3150c/material/img/eje6-boxplot.svg)

*Figura 4. Un boxplot de tiempos de atención. La mediana está más cerca de Q1 que de Q3 y el bigote derecho es más largo: la cola va a la derecha. Los dos puntos sueltos, como el cliente con problemas en el pago, se revisan antes de decidir si se borran.*

Los bigotes llegan hasta el último dato que no se aleja más de 1,5 veces el ancho de la caja:

$$IQR = Q_3 - Q_1 \qquad \text{outlier si } x < Q_1 - 1{,}5\,IQR \ \text{ o } \ x > Q_3 + 1{,}5\,IQR$$

Acá: $IQR = 5{,}3 - 2{,}9 = 2{,}4$, y el límite de arriba es $5{,}3 + 3{,}6 = 8{,}9$. Por eso 10,5 y 13 quedan afuera.

**Lo importante.** La dispersión y la forma importan tanto como el promedio. Y limpiar no es borrar lo que molesta.

**Ojo, trampa.** "Con el tiempo medio alcanza" es falso, y el apunte lo lista como error frecuente.

Marca otros tres. El primero, confundir instantes con duraciones: las diez y cinco es un instante; siete minutos, una duración. El segundo, cargar tiempos absolutos, como la hora de cada llegada, cuando se necesitan tiempos entre eventos. Y el tercero, elegir una distribución por costumbre.

Y "los outliers siempre se eliminan" también es falso.

## Estadística descriptiva

Las medidas descriptivas orientan el ajuste.

La media es el promedio, y la afectan los extremos. La mediana es el dato central, y es más robusta frente a outliers. Si a una sala entra un millonario, el sueldo promedio se dispara, pero la persona del medio casi no cambia.

Con números: cinco personas cobran 500, 600, 700, 800 y 900 mil pesos. Media y mediana, 700. Entra alguien que cobra 50 millones. La media salta a casi 8,9 millones, un sueldo que no cobra nadie de la sala; la mediana apenas se mueve, de 700 a 750.

```grafico
tipo: barras
titulo: Sueldos antes y después de que entre el millonario
unidad: miles de $

Sala, Media, Mediana
5 personas, 700, 700
Con el millonario, 8917, 750
```

Por eso, si media y mediana se parecen, la distribución suele ser simétrica.

La moda es el valor más repetido, y puede no existir o haber más de una. En el histograma, es la barra más alta. La mesa de ayuda de más arriba tiene dos: una por cada joroba.

La varianza y el desvío miden cuánto se alejan los datos de la media, y el desvío está en la unidad del dato. El coeficiente de variación compara dispersión entre procesos.

$$\bar{x} = \frac{\sum x_i}{n} \qquad s^2 = \frac{\sum (x_i - \bar{x})^2}{n - 1} \qquad s = \sqrt{s^2} \qquad CV = \frac{s}{\bar{x}}$$

Ejemplo del apunte: cuatro, cinco, cinco, seis y ocho. La media queda un poco por encima de la mediana. ¿Por qué? Porque el ocho la empuja.

```grafico
tipo: barras
titulo: Datos del apunte: 4, 5, 5, 6 y 8
unidad: veces

Valor, Frecuencia
4, 1
5, 2
6, 1
7, 0
8, 1
```

| Medida | Cuenta | Valor |
|---|---|---|
| Media | (4 + 5 + 5 + 6 + 8) / 5 | 5,6 |
| Mediana | el tercero de cinco, ordenados | 5 |
| Moda | el que más se repite | 5 |
| Varianza | (2,56 + 0,36 + 0,36 + 0,16 + 5,76) / 4 | 2,3 |
| Desvío | $\sqrt{2{,}3}$ | 1,52 |
| CV | 1,52 / 5,6 | 0,27 |

Moda y mediana quedan en 5; la media, sola, se corre hacia el 8. Ese orden es la marca de una distribución con cola a la derecha.

Y es justo la forma típica de los tiempos de atención: la mayoría son cortos y unos pocos se estiran mucho.

![Moda, mediana y media](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/37acd8b34578a4dc1e22ead737868dc209b3150c/material/img/eje6-moda-mediana-media.svg)

*Figura 5. Los mismos tiempos de atención del boxplot, como curva. De izquierda a derecha: moda, mediana y media.*

El pico de la curva es la moda: 3,2 minutos, la duración más frecuente. La mediana deja la mitad de las atenciones a cada lado: 3,9. Y la media, empujada por las atenciones largas de la cola, 4,3. En una distribución con cola a la derecha el orden suele ser ese: moda, después mediana, después media. Si fuera simétrica, las tres coincidirían en el centro.

El histograma da la primera hipótesis de forma. Y la frase del apunte es: el gráfico dice parece, la prueba dice qué tan bien ajusta.

**Lo importante.** Media contra mediana te da una pista de la simetría.

**Ojo, trampa.** La moda puede no ser única. Y si te dicen que la media es más robusta que la mediana frente a outliers, es al revés.

## Bondad de ajuste

### Qué es y cómo se lee

Bondad de ajuste es medir qué tan cerca están los datos reales de una distribución propuesta.

¿Te suena? En el eje dos se probaba si el generador daba números uniformes. Acá, si los datos reales se pueden representar con una distribución candidata.

Dos frases del apunte para tener a mano.

La primera: la prueba no elige por sí sola. Primero se mira el histograma y se entiende el proceso; después, la prueba respalda o cuestiona.

La segunda: un valor p mayor que cero coma cero cinco significa que no hay evidencia suficiente para rechazar la distribución, no que quedó demostrada como la única verdadera. Es como un juicio: no culpable no quiere decir inocente, sino que no alcanzaron las pruebas.

Además, la mejor distribución no es la más compleja, sino la que ajusta y tiene sentido para el fenómeno.

**Lo importante.** No rechazar no es demostrar.

**Ojo, trampa.** Cualquier opción que diga que la prueba "demuestra" o "confirma" la distribución es falsa. Lo correcto es "no se rechaza" o "los datos son compatibles".

### La limitación de las pruebas

Las tablas estándar de las pruebas de bondad de ajuste suponen que la distribución está completamente especificada de antemano.

¿Qué pasa en simulación? Los parámetros se estiman con los mismos datos que después se prueban, y entonces la prueba tiende a aceptar de más. Es como corregir tu examen usando tus propias respuestas como plantilla: te va a ir mejor de lo que merecés.

Por eso no conviene apoyarse solo en ella. Se combinan tres miradas: histograma, medidas descriptivas y bondad de ajuste.

**Lo importante.** La prueba sola no decide: cuando histograma, medidas descriptivas y bondad de ajuste coinciden, la decisión suele ser sólida.

**Ojo, trampa.** La opción tramposa dice que estimar los parámetros con la muestra vuelve la prueba más exigente. Es al revés: acepta de más.

**Si te toca de desarrollo.** Primero, definí bondad de ajuste y para qué sirve. Después aclará que la prueba no elige por sí sola: antes se mira el histograma y se entiende el proceso. Sumá la limitación de los parámetros estimados y las tres miradas. Y cerrá con que no rechazar no demuestra.

## Planeación táctica

La planeación táctica define tres cosas: cuánto simular, desde cuándo medir y cuántas réplicas correr. Y tiene una frase de cabecera: una corrida es un futuro posible, no la respuesta.

### Variabilidad y réplicas

¿Corriste dos veces el mismo modelo y te dio distinto? Es normal: las entradas son aleatorias. No es un error del software. El error es mirar una sola corrida y creerla definitiva, como tirar un dado una vez, que salga cuatro, y concluir que el dado da cuatro.

Con varias réplicas calculás tres cosas. Primero, la media de las réplicas, que es el resultado estimado. Después, el desvío entre réplicas, que dice cuánto cambia una corrida de otra. Y por último, el error estándar, que mide la incertidumbre de esa media.

¿Qué es una réplica? Una ejecución completa e independiente: reinicia el estado y las estadísticas, y usa aleatorios independientes.

¿Y cortar una corrida larga en trozos? No es lo mismo, porque los trozos pueden estar correlacionados. Pensá en una autopista medida hora por hora: si a las ocho hay embotellamiento, a las nueve todavía queda cola.

**Lo importante.** Un resultado se informa con varias réplicas independientes, no con una corrida.

**Ojo, trampa.** Tres frases que caen seguido.

La primera: con más réplicas baja el error estándar, no la variabilidad del sistema. Más fotos del mar te dicen mejor cómo son las olas, pero el mar no se calma.

La segunda: "si dos corridas dan distinto, el modelo tiene un error" es falso.

Y la tercera: una corrida larga en trozos no equivale a réplicas.

### Sistemas terminantes, no terminantes y warm-up

El terminante, como un supermercado de ocho a veintiuna, se vacía o se reinicia cada jornada. Es como un partido de fútbol: cada uno arranca de cero y tiene final. La pregunta es cómo fue ese día.

El no terminante, como un hospital de veinticuatro horas o un servidor web, no tiene final natural. La pregunta es cómo funciona a largo plazo.

Si un sistema que normalmente tiene cola arranca vacío, los primeros minutos parecen tranquilos y se subestima la espera. Es el sesgo de inicialización.

¿La solución? El warm-up: el período inicial en que el modelo corre normalmente, pero no se mide. Como un horno: funciona desde que lo prendés, pero no anotás la temperatura hasta que se estabiliza.

Ejemplo: un hospital simulado treinta días, con dos de warm-up, se mide del día tres al treinta.

¿Cómo se elige? Se grafican corridas piloto, promediadas o con media móvil, y se toma el punto donde termina la tendencia de arranque. Abajo lo tenés dibujado.

![Curva de warm-up](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/material/img/eje6-warmup.svg)

*Figura 6. Un sistema no terminante que arranca vacío. Al principio la cola parece más chica que la real: ese tramo es el warm-up y no se mide. Las estadísticas se toman en la zona estable.*

**Lo importante.** El warm-up es para sistemas no terminantes, y elimina el sesgo de arrancar vacío.

**Ojo, trampa.** Durante el warm-up el modelo funciona; solo se descartan las estadísticas.

En el supermercado simulado desde su apertura real, el apunte dice que no hace falta warm-up: ahí arrancar vacío es lo real.

Y warm-up y réplicas resuelven cosas distintas: el sesgo de arranque y la variabilidad entre corridas.

### Cuántas réplicas

No hay un número mágico: depende de la variabilidad y de la precisión que necesitás.

Con las réplicas se arma un intervalo de confianza para la media, por ejemplo del noventa y cinco por ciento. En la práctica, el software calcula el intervalo y su semiancho, que es cuánto se abre hacia cada lado. El apunte recomienda un error relativo de hasta un quince por ciento, aproximadamente.

El procedimiento: primero, fijás la precisión. Después, corrés un piloto de al menos diez réplicas y mirás el semiancho. Si supera lo aceptable, recalculás la cantidad de réplicas y volvés a correr. Y si ya cumple, documentás el resultado.

**Lo importante.** La cantidad de réplicas sale de la precisión que necesitás: piloto, semiancho y ajuste.

**Ojo, trampa.** "Siempre alcanza con diez réplicas" es falso. Diez es el mínimo del piloto; después, la cantidad se ajusta según la precisión.

**Si te toca de desarrollo.** Arrancá con que una corrida es un futuro posible. Definí réplica y por qué no sirve partir una corrida larga. Contá para qué sirve el intervalo de confianza. Explicá el piloto y cómo se ajusta la cantidad de réplicas hasta la precisión buscada. Y por último, sumá el warm-up.

### Números aleatorios comunes

Reducir varianza es comparar con más claridad sin multiplicar réplicas. No mejora el sistema real ni los resultados: mejora la forma de experimentar.

Con números aleatorios comunes, la réplica uno de las dos alternativas corre con la misma demanda aleatoria, la réplica dos con otra demanda común, y así. Comparás par por par, y la demanda del día no tapa el efecto de agregar una caja.

Es como probar dos zapatillas con el mismo corredor, circuito y clima. Al otro día cambia el clima, pero otra vez es igual para las dos. Así la diferencia es de la zapatilla, no del viento.

El apunte nombra también las variables antitéticas, que usan secuencias opuestas, y las de control, que aprovechan una medida conocida y correlacionada.

**Lo importante.** Sirve para comparar alternativas bajo las mismas condiciones aleatorias.

**Ojo, trampa.** No es usar la misma secuencia en todas las réplicas: cada réplica tiene su demanda, y lo que se comparte es entre alternativas. Y no la confundas con las antitéticas, que usan secuencias opuestas.

## Validación y análisis

### Verificación, validación y credibilidad

Un modelo es válido, para un objetivo concreto, cuando hay evidencia suficiente de que representa al sistema con una precisión útil para decidir.

Ahora, el trío. Para ordenarlo, pensá el modelo como un mapa.

Verificación pregunta si construimos el modelo como lo describimos: si la regla FIFO y los horarios de las cajas están bien programados. Es revisar que el mapa esté dibujado según tus anotaciones. Lo viste en el eje cuatro.

Validación pregunta si el modelo representa razonablemente al sistema real para este objetivo: si la espera y la utilización simuladas se parecen a las observadas. Es salir a la calle y ver si el mapa coincide con el barrio.

Credibilidad pregunta si los usuarios confían en el estudio y lo entienden: si el encargado reconoce las reglas y acepta las conclusiones. Es que quien va a usar el mapa le crea.

La implantación es otra cosa: no compara, lleva la alternativa elegida al sistema real. Abajo tenés las cuatro dibujadas.

![Verificar, validar, credibilidad e implantar](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/material/img/eje6-verificar-validar.svg)

*Figura 7. Verificar mira lo que describiste; validar, el sistema real; credibilidad, a los usuarios. Implantar lleva la alternativa elegida al sistema real.*

¿Cuándo se valida? A medida que se construye, no al final. Primero, definís el objetivo y documentás supuestos. Después, revisás el modelo conceptual con quienes conocen el proceso y probás componentes por separado. Y por último, comparás con datos reales y registrás limitaciones.

Y ojo: un modelo puede ser válido para estimar la espera y no para diseñar la distribución física del local. La validez está ligada al propósito, como el mapa del subte: sirve para saber dónde bajarte, no para medir cuánto caminás.

Los métodos se combinan. Los subjetivos usan conocimiento experto: recorrido con expertos, revisión de la animación y juicio de coherencia, como preguntarse si al duplicar la demanda la cola debería crecer.

Los objetivos usan datos: comparar media, percentiles y throughput, o sea, clientes atendidos por hora, con la realidad; intervalos, pruebas de hipótesis, balances y trazas.

**Lo importante.** Verificar mira hacia adentro, contra lo que describiste. Validar mira hacia afuera, contra el sistema real. Credibilidad mira a los usuarios. Y primero se verifica, después se valida.

**Ojo, trampa.** Es el trío que más cae: lógica bien programada es verificación; parecido con la realidad, validación; confianza del usuario, credibilidad.

Son falsas "un modelo válido sirve para cualquier decisión" y "se valida al final". Y el apunte lo dice textual: los métodos subjetivos no son menos serios.

**Si te toca de desarrollo.** Primero, definí los tres conceptos con su pregunta y un ejemplo. Después aclará que la validez depende del objetivo. Listá los pasos, remarcando que se valida durante la construcción. Y cerrá con los métodos subjetivos y objetivos.

### Pruebas de hipótesis sobre los resultados

Sirven para decidir si una diferencia entre escenarios es azar de las réplicas o es consistente.

Ejemplo: hipótesis nula, dos y tres cajas tienen la misma espera media; alternativa, con tres es menor. Si el intervalo de la diferencia queda por encima de cero, hay evidencia a favor de tres cajas.

¿Y el valor p? Uno chico indica que los datos son poco compatibles con la hipótesis nula. Pero no dice que sea falsa con un porcentaje exacto, ni mide la importancia práctica. Ahorrar cero coma cero tres minutos puede ser detectable e irrelevante, como un descuento de un peso en una heladera.

**Lo importante.** No rechazar no es demostrar igualdad, y significativo no es lo mismo que importante.

**Ojo, trampa.** El error que el apunte marca como frecuente: leer "no se rechaza la hipótesis nula" como "los escenarios son iguales". Otra vez el juicio: no culpable no es inocente. Solo significa que no hubo evidencia suficiente; tal vez faltan réplicas.

### Estructura interna y pruebas de campo

La estructura interna se revisa por dentro, con cuatro pruebas.

La primera, la traza: seguís a un cliente desde que llega hasta que sale.

La segunda, el balance: las entradas tienen que ser iguales a las salidas más las que siguen adentro, como el arqueo de caja al cierre. Detecta entidades duplicadas o perdidas.

La tercera, el caso extremo: cero llegadas o capacidad infinita.

Y la cuarta, la sensibilidad lógica: aumentás la demanda o reducís recursos, y mirás que el resultado vaya en la dirección esperada.

Las pruebas de campo comparan indicadores reales y simulados en condiciones equivalentes. Una semana de promociones contra un día simulado sin promociones es comparar peras con manzanas.

No hace falta que cada cifra coincida, sino que la diferencia sea aceptable para decidir. En el ejemplo del apunte, el percentil noventa y cinco de la espera da doce minutos en el campo y ocho coma siete en el modelo. ¿Conclusión? El modelo probablemente no representa bien los picos.

Calibrar es ajustar parámetros inciertos dentro de rangos defendibles, documentando cada cambio. No es mover valores hasta que el gráfico quede lindo.

**Lo importante.** Un promedio razonable puede esconder errores, dentro del modelo o en los picos.

**Ojo, trampa.** Hay tres.

La primera: el apunte llama a la estructura interna validación en el índice y verificación en el título. Así que aprendete qué detecta cada prueba.

La segunda: no confundas la sensibilidad lógica, que mira la dirección del resultado, con el análisis de sensibilidad, que mira si cambia la conclusión.

Y la tercera: calibrar no es ocultar un problema.

### Análisis de sensibilidad

La pregunta es: si este supuesto cambia dentro de un rango razonable, ¿cambia mi conclusión?

Sirve para saber dónde invertir esfuerzo de medición y qué recomendaciones son robustas. Se prueban factores inciertos con valores bajo, base y alto, con réplicas por escenario.

El gráfico típico es el diagrama tornado: cada factor es una barra que muestra cuánto cambia la espera respecto del caso base. Las barras más largas son los supuestos más influyentes; en el ejemplo, el tiempo de atención y la tasa de arribos, que conviene medir mejor. Un factor de poco impacto se puede modelar más simple. Abajo tenés uno dibujado.

![Diagrama tornado](https://raw.githubusercontent.com/JHProyectos/tpi-simulacion-2026/main/material/img/eje6-tornado.svg)

*Figura 8. Un diagrama tornado. Cada barra muestra cuánto cambia la espera respecto del caso base; las más largas son los supuestos más influyentes.*

**Lo importante.** El tornado te dice qué supuestos pesan más y dónde conviene medir mejor.

**Ojo, trampa.** Barra más larga, factor más influyente; no al revés. Y no se hace con una corrida por escenario.

**Si te toca de desarrollo.** Primero, planteá la pregunta central. Después explicá para qué sirve. Contá los pasos, con valores bajo, base y alto y réplicas. Y por último, describí el tornado con el ejemplo de atención y arribos.

## Implantación

### De resultado a decisión

"El escenario B es mejor" no alcanza. Una recomendación útil dice cuatro cosas: qué cambiar, cuánto se espera mejorar, qué cuesta y con qué incertidumbre.

Ejemplo: tres cajas bajan la espera media de cinco coma cuatro a tres coma nueve minutos. Entonces, se abre una tercera caja de dieciocho a veintiuna.

¿Y si la utilización baja? No significa personal ocioso: la capacidad extra es la que evita los picos.

Ahora, la significancia práctica. Bajar cero coma un minuto puede ser real y no justificar contratar a alguien. En cambio, evitar esperas de más de quince minutos en hora pico puede valer mucho, aunque el promedio cambie poco.

**Lo importante.** La mejora tiene que importar para el objetivo real, no solo ser detectable.

**Ojo, trampa.** Significancia estadística no es significancia práctica.

### Plan, piloto y seguimiento

La implantación va por etapas, sobre todo si afecta personas, turnos o costos.

El plan tiene seis partes: objetivo, alcance, responsable, recursos, riesgos y criterio de éxito. En el ejemplo, el criterio es que el percentil noventa y cinco de la espera no pase de diez minutos.

Después, el piloto: una prueba limitada antes de extender la mejora. ¿Reemplaza a la simulación? No, la complementa: la simulación explora alternativas sin riesgo, y el piloto verifica la elegida en el contexto real. Como la prueba de manejo: después de comparar autos en los papeles, manejás el elegido por un recorrido corto.

El piloto lleva, primero, alcance acotado. Después, una línea de base medida antes del cambio, y las condiciones especiales registradas. Y por último, la decisión de detener, corregir o escalar, definida de antemano. Es poner el arco antes de patear, no dibujarlo donde cayó la pelota.

Y no se comparan solo promedios: si en el piloto hubo menos demanda, la mejora parece mayor de lo que es.

Después viene el seguimiento, hasta uno a tres meses más tarde. Y ante cambios relevantes hay que revalidar el modelo, como se actualiza un mapa cuando abren calles nuevas.

Al comunicar, no se oculta la incertidumbre, no se presenta la animación como prueba suficiente y no se prometen resultados exactos. Y se documenta todo.

**Lo importante.** Piloto acotado, con línea de base y criterio fijado antes, y seguimiento después.

**Ojo, trampa.** "El piloto reemplaza a la simulación" es falso. El criterio de éxito se define antes, no después de ver los resultados. Y un modelo validado una vez no queda validado para siempre.

**Si te toca de desarrollo.** Primero, explicá cómo se traduce un resultado en recomendación, con significancia práctica. Después nombrá los componentes del plan. Desarrollá el piloto con línea de base y criterio previo. Y cerrá con seguimiento, comunicación y documentación.

## Preguntas tipo multiple choice

En cada una: las opciones, la correcta, por qué, y dónde está la trampa.

Pregunta uno. Dos cajas tienen la misma atención media, pero en una los tiempos varían mucho más que en la otra. ¿Qué esperás al simularlas?

Primera: que se comporten igual, porque el promedio es el mismo. Segunda: que se comporten distinto, porque la dispersión y la forma también afectan las colas y las esperas. Tercera: que la más variable tenga menos cola. Cuarta: que la diferencia sea un error del modelo.

La correcta es la segunda, porque la variabilidad es lo que genera las colas. ¿La trampa? La primera: creer que el promedio alcanza es un error frecuente que marca el apunte.

Pregunta dos. Medís las atenciones de una caja y aparece un cliente que tardó muchísimo por un problema con el pago. ¿Qué hacés con ese dato?

Primera: lo eliminás siempre, porque es un outlier. Segunda: lo revisás, porque puede ser un error de carga o un caso real que conviene conservar. Tercera: lo reemplazás por la media. Cuarta: descartás toda la muestra.

La correcta es la segunda: un outlier no siempre se elimina, y este caso forma parte del proceso. ¿La trampa? La primera, porque limpiar no es borrar lo que molesta.

Pregunta tres. Una prueba de bondad de ajuste da un valor p de cero coma treinta.

Primera: los datos siguen esa distribución. Segunda: no hay evidencia suficiente para rechazarla. Tercera: se rechaza. Cuarta: quedó demostrada.

La correcta es la segunda. ¿La trampa? La primera, que convierte no rechazar en demostrar.

Pregunta cuatro. ¿Qué pasa si los parámetros se estiman con la misma muestra que se prueba?

Primera: la prueba se vuelve más exigente. Segunda: tiende a aceptar de más. Tercera: no cambia nada. Cuarta: no se puede usar.

La correcta es la segunda. ¿La trampa? La primera, que dice justo lo contrario.

Pregunta cinco. ¿Qué es una réplica?

Primera: cada trozo de una corrida larga. Segunda: una ejecución completa e independiente, que reinicia el estado y las estadísticas y usa aleatorios independientes. Tercera: volver a correr el modelo con la misma secuencia de aleatorios. Cuarta: el período inicial que no se mide.

La correcta es la segunda, porque cada réplica tiene que representar un futuro posible, independiente de los demás. ¿La trampa? La primera: los trozos de una corrida larga pueden estar correlacionados, así que no equivalen a réplicas.

Pregunta seis. ¿En qué caso hace falta warm-up?

Primera: un supermercado simulado desde su apertura real. Segunda: un hospital de veinticuatro horas. Tercera: todos los modelos. Cuarta: ninguno, porque las réplicas lo corrigen.

La correcta es el hospital, que es no terminante. ¿La trampa? "Todos los modelos": el supermercado que de verdad arranca vacío no lo necesita.

Pregunta siete. ¿De qué depende la cantidad de réplicas que hay que correr?

Primera: siempre alcanza con diez. Segunda: de cuánto varían los resultados y de cuánta precisión necesitás para decidir. Tercera: solo de la duración de cada corrida. Cuarta: del warm-up elegido.

La correcta es la segunda, porque no hay un número mágico universal. ¿La trampa? La primera: diez es el mínimo del piloto, y después la cantidad se ajusta según el semiancho obtenido.

Pregunta ocho. ¿Qué es la técnica de números aleatorios comunes?

Primera: la misma secuencia en todas las réplicas de un escenario. Segunda: la misma demanda aleatoria en cada réplica de las alternativas, comparando par por par. Tercera: secuencias opuestas. Cuarta: una forma de mejorar el sistema real.

La correcta es la segunda. La tercera son las antitéticas. ¿Y la más tramposa? La primera.

Pregunta nueve. Revisás que la regla FIFO esté bien programada. ¿Qué estás haciendo?

Las opciones: validación, verificación, credibilidad o calibración.

La correcta es verificación. ¿La trampa? Validación, que compara con el sistema real.

Pregunta diez. Comparás dos y tres cajas y no se rechaza la hipótesis nula.

Primera: los escenarios son iguales. Segunda: no hubo evidencia suficiente para detectar una diferencia. Tercera: conviene dejar dos cajas. Cuarta: el modelo no es válido.

La correcta es la segunda. ¿La trampa? La primera, que es el error frecuente que marca el apunte.

Pregunta once. En un diagrama tornado, ¿qué indica la barra más larga?

Primera: el factor menos influyente. Segunda: el supuesto que más cambia el resultado. Tercera: la variabilidad entre réplicas. Cuarta: el mejor escenario.

La correcta es la segunda. ¿La trampa? "El mejor escenario": el tornado ordena supuestos.

Pregunta doce. El modelo se parece a la realidad en la espera media, pero da bastante menos en el percentil noventa y cinco.

Primera: es válido porque la media coincide. Segunda: probablemente no representa bien los picos. Tercera: hay que mover parámetros hasta que coincida. Cuarta: no importa.

La correcta es la segunda. ¿La trampa? La tercera: calibrar no es forzar.

Pregunta trece. ¿Qué afirmación sobre el piloto es correcta?

Primera: reemplaza a la simulación. Segunda: el criterio de éxito se define al terminar. Tercera: es una prueba limitada, con línea de base y criterio previo. Cuarta: alcanza con comparar promedios.

La correcta es la tercera. ¿Y el distractor más tramposo? La cuarta: con menos demanda, la mejora parece mayor.

## Lo que puede entrar en desarrollo

Tema uno: cómo se elige la distribución de un dato de entrada. Por qué el promedio no alcanza. Cómo se prepara la muestra, con outliers que no siempre se eliminan. Medidas descriptivas e histograma. Prueba de bondad de ajuste, con sus límites. Y la decisión: la que ajusta y tiene sentido para el fenómeno.

Tema dos: planeación táctica. Una corrida es un futuro posible. Terminantes y no terminantes, sesgo de inicialización y warm-up. Réplicas independientes, intervalo de confianza y cómo se decide cuántas réplicas correr. Y números aleatorios comunes para comparar alternativas.

Tema tres: validación. Verificación, validación y credibilidad, con la validez ligada al propósito. Validar durante la construcción. Métodos subjetivos y objetivos. Y pruebas de campo y análisis de sensibilidad.

Tema cuatro: implantación. Recomendación con significancia práctica. Plan con sus seis componentes. Piloto con línea de base y criterio previo. Y seguimiento y comunicación honesta de la incertidumbre.

## Lo mínimo que te tenés que llevar

El promedio solo no alcanza: la dispersión y la forma generan las colas.

La prueba de bondad de ajuste no elige sola: se combinan histograma, medidas descriptivas y prueba. Y con parámetros estimados con la misma muestra, la prueba acepta de más.

No rechazar no es demostrar, ni en el ajuste ni al comparar escenarios. Y significativo no es lo mismo que importante.

Una corrida es un futuro posible: réplicas independientes, tantas como pida la precisión que necesitás. Y warm-up, solo en no terminantes.

Verificar es construir el modelo como se describió; validar, que represente al sistema para ese objetivo; credibilidad, que los usuarios confíen. Y la implantación va por etapas, con piloto.
