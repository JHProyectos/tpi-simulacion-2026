# Eje 1. Introducción a la simulación

Hola. Este es el resumen hablado del eje uno: introducción a la simulación. Dura unos quince minutos. Para el parcial de mañana, la teoría que se toma es del eje cuatro al ocho, así que este eje no entra directamente. Pero es la base de todo lo demás, y varias ideas vuelven a aparecer en los ejes posteriores: el modelo, la validación, la verificación, el proceso de simulación. Escuchalo como repaso de fondo.

## Presentación de la cátedra

Rápido. La materia se llama Simulación, es de cuarto nivel de Ingeniería en Sistemas de Información, tres horas semanales y régimen anual. El docente titular es el ingeniero Sergio Andrés Revilla y la jefa de trabajos prácticos es la ingeniera Sofía Gaggi.

Los objetivos: comprender el proceso de simulación de sistemas, desde el modelado hasta su implementación; diseñar un proceso de simulación completo, trasladando el modelo a programas de computación; y formar al alumno para construir modelos informáticos sobre el comportamiento de sistemas, experimentar con ellos, analizar los resultados y desarrollar conclusiones para la toma de decisiones, con criterios estadísticos.

## Qué es un modelo

La definición: un modelo es la representación de un objeto, idea o sistema de forma diferente al original. El propósito es ayudarnos a entender, explicar o mejorar un sistema. Puede ser incluso una réplica exacta, aunque con otro material y otra escala.

Las funciones de un modelo son cinco. Una ayuda para el pensamiento. Una ayuda para la comunicación. Sirve para entrenamiento e instrucción. Es una herramienta de predicción. Y es una ayuda para la experimentación.

Y la clasificación, con cuatro ejes, cada uno con dos o tres categorías. Estático contra dinámico. Determinístico contra estocástico. Discreto contra continuo. Y por su forma: icónico o físico, analógico o simbólico. Estos cuatro ejes los vas a ver reaparecer. Por ejemplo, en el eje cinco los modelos son dinámicos, estocásticos y discretos; en el eje ocho son dinámicos, determinísticos y continuos.

## El arte del modelado

Es la habilidad para analizar un problema, resumir sus características esenciales, seleccionar y modificar las suposiciones básicas que caracterizan al sistema, y después enriquecer y elaborar el modelo hasta obtener una aproximación útil.

El proceso de enriquecer implica una interacción constante, una retroalimentación entre la situación del mundo real y el modelo. Mientras el modelo sea computacionalmente manejable, el analista puede seguir enriqueciéndolo, o sea complicando las suposiciones. Cuando se vuelve intratable, se recurre a la simplificación y a la abstracción.

Hay siete principios del modelado. Uno: dividir el problema del sistema en problemas más simples. Dos: establecer una definición clara de los objetivos. Tres: buscar analogías. Cuatro: considerar un ejemplo numérico específico del problema. Cinco: establecer algunos símbolos. Seis: escribir los datos obvios. Siete: si se obtiene un modelo manejable, enriquecerlo; de otra manera, simplificarlo.

Y hay una frase del apunte que vale la pena memorizar: nadie resuelve el problema, sino que cada quien resuelve el modelo del problema que ha construido.

Las formas de simplificar un modelo son cinco. Convertir variables en constantes. Eliminar o combinar variables. Suponer linealidad. Agregar suposiciones más potentes y restricciones. Y restringir los límites del sistema.

## Criterios para un buen modelo

Seis criterios. Fácil de entender por parte del usuario. Dirigido a metas u objetivos. Sensato, en cuanto a que no dé respuestas absurdas. Fácil de controlar y manipular por el usuario, o sea que sea sencillo comunicarse con el modelo. Completo, en lo referente a asuntos importantes. Y adaptable, con un procedimiento sencillo para modificarlo o actualizarlo.

Y una observación del apunte: no existe una justificación para preparar un modelo de simulación si no se usa o si no es utilizable para quien toma las decisiones.

## Formas de estudiar un sistema

Ante un sistema real hay distintas maneras de estudiarlo. Se puede experimentar con el sistema real, o experimentar con un modelo del sistema. Y si se usa un modelo, puede ser físico o matemático; y si es matemático, se puede resolver con una solución analítica, cuando es posible, o con simulación. La simulación es el camino que se elige cuando el modelo matemático no se puede resolver analíticamente, o cuando resolverlo es mucho más difícil que simularlo.

### Desventajas de la experimentación directa

Esto es una trampa para el parcial, y lo anotaste en tus apuntes de clase: las desventajas de la experimentación directa no son las desventajas de la simulación. Es una pregunta que se presta a confusión. Así que escuchá bien las cinco, que son las de experimentar directamente sobre el sistema real.

Una: puede interrumpir las operaciones de la compañía. Dos: si la gente es parte integral del sistema, puede afectar los resultados; el hecho de que se observe a la gente puede modificar su comportamiento. Tres: mantener las mismas condiciones operativas en cada repetición o corrida del experimento puede ser muy difícil. Cuatro: obtener el mismo tamaño de muestra puede requerir más tiempo y ser más costoso. Cinco: quizás no sea posible explorar muchos tipos de alternativas en la experimentación del mundo real.

Y las de la simulación son otras, que vemos más abajo. No las mezcles.

## El concepto de simulación

La simulación es una herramienta fundamental para analizar, entender y mejorar sistemas complejos. Se basa en construir un modelo computacional que imita el funcionamiento de un sistema real o hipotético a lo largo del tiempo, permitiendo experimentar con diferentes condiciones sin intervenir directamente en la realidad.

### Las tres definiciones formales

Tu anotación dice: ver bien las definiciones de Shannon, Banks y Averill, que es Averill Law. Así que van las tres, con la idea central de cada una.

La de Robert Shannon, de mil novecientos setenta y cinco: la simulación de sistemas es el proceso de diseñar un modelo computarizado de un sistema real y realizar experimentos con él para entender el comportamiento del sistema o evaluar varias estrategias para su operación. Fijate en las palabras clave: diseñar un modelo computarizado, y realizar experimentos con él. Dos propósitos: entender el comportamiento y evaluar estrategias.

La de Banks y colaboradores, de dos mil nueve: la simulación representa la operación de algún proceso o sistema del mundo real a través del tiempo, ya sea realizada manualmente o por medio de una computadora. Involucra la generación de una historia artificial de un sistema y su observación para obtener inferencias relacionadas con las características operativas del sistema real. Palabras clave: a través del tiempo; manualmente o por computadora; historia artificial; inferencias sobre el sistema real. Es la única de las tres que dice explícitamente que se puede hacer a mano. Y es la que habla de historia artificial.

La de Averill Law, de dos mil catorce, de su libro Simulation Modeling and Analysis, quinta edición: la simulación es la imitación del funcionamiento de un proceso o sistema del mundo real a lo largo del tiempo. Implica el desarrollo de un modelo que represente las características clave o comportamientos del sistema o proceso físico o abstracto seleccionado. El modelo representa el sistema en sí, mientras que la simulación representa su funcionamiento en el tiempo. Palabras clave: imitación; a lo largo del tiempo; y la distinción final, el modelo representa el sistema, la simulación representa su funcionamiento en el tiempo.

Un truco para distinguirlas: Shannon es el que habla de experimentos con un modelo computarizado; Banks es el de la historia artificial; Law es el de modelo contra simulación.

### Propósitos de la simulación

La simulación se usa como una metodología aplicada y experimental para cuatro cosas. Describir el comportamiento de sistemas reales o hipotéticos. Postular teorías o hipótesis que expliquen ese comportamiento. Predecir el impacto de cambios en las condiciones de operación o en la estructura del sistema. Y evaluar decisiones sin incurrir en los costos o riesgos que tendría implementarlas directamente.

## El ejemplo de la tienda de regalos

El apunte tiene un ejemplo muy simple. Un sistema de una sola cola, la caja registradora de una pequeña tienda de regalos. El tiempo entre llegadas de clientes está uniformemente distribuido entre uno y diez minutos. El tiempo de atención, uniforme entre uno y seis minutos. Interesa el tiempo promedio que un cliente permanece en el sistema y el porcentaje de tiempo que el cajero está desocupado.

Para simular, hace falta generar una experiencia artificial. Se piden prestadas diez fichas de póker y un dado: las fichas numeradas del uno al diez, en un sombrero; sacar una ficha da el tiempo entre llegadas, y tirar el dado da el tiempo de servicio. Repitiendo, se genera una serie de llegadas y tiempos de servicio. El problema se vuelve un problema contable: una tabla con veinte clientes.

La moraleja del ejemplo: se usaron dos dispositivos para generar números aleatorios, las fichas y el dado, para producir un experimento artificial con un sistema. Y con una advertencia: para tener significación estadística haría falta una muestra mucho más grande, y se ignoraron las condiciones de inicio, que son el tema del período de calentamiento del eje seis.

## Condiciones favorables para aplicar simulación

Seis. Uno: no existe una adecuada formulación matemática del problema. Dos: existen métodos analíticos pero son tan complejos y difíciles que la simulación brinda un método más simple. Tres: las soluciones analíticas existen y son posibles, pero están más allá de la habilidad matemática del personal disponible. Cuatro: se desea observar el trayecto histórico, simulando el proceso sobre un período. Cinco: la simulación puede ser la única posibilidad. Seis: se requiere acelerar el tiempo en sistemas o procesos que demandan mucho tiempo para realizarse.

## Ventajas de la simulación

Ocho ventajas. Evaluación sin riesgo: se puede experimentar con escenarios y estrategias sin afectar el sistema real. Análisis de sistemas complejos, difíciles de analizar con métodos analíticos tradicionales. Optimización de procesos: ayuda a identificar cuellos de botella y áreas de mejora. Prueba de nuevas políticas antes de implementarlas. Visualización y comunicación: da una visualización clara del comportamiento y facilita comunicar resultados. Flexibilidad: sirve para modelar muchos tipos de sistemas y escenarios. Reducción de costos: evita cambios costosos en el sistema real hasta haberlos probado virtualmente. Y capacitación y formación: permite entrenar al personal en situaciones difíciles o peligrosas de replicar.

## Desventajas de la simulación

Ocho desventajas, que no tenés que confundir con las de la experimentación directa. Costo y tiempo de desarrollo, sobre todo con mucho detalle. Complejidad en la construcción del modelo: requiere conocimientos especializados. Limitaciones de los datos: la precisión depende de la calidad y disponibilidad de los datos. Dificultad en la validación. Suposiciones simplificadas, que pueden afectar la precisión y validez. Requiere recursos computacionales: hardware potente y software especializado. Resultados dependientes del modelo: son tan buenos como el modelo, y uno mal diseñado puede llevar a decisiones incorrectas. Y falta de comprensión por parte de los interesados: los resultados y métodos pueden ser difíciles de entender para quienes no están familiarizados.

Un truco para recordarlas: hay tres que tienen que ver con el modelo, que son complejidad, suposiciones y dependencia del modelo; dos con los datos y la validación; y tres con costo, recursos y comprensión.

## Uso de la simulación

Cuatro usos generales. Para definir un sistema o proceso. Como herramienta de análisis y toma de decisiones. Como asesoramiento para evaluar o sintetizar soluciones. Y como predictor para planear futuros desarrollos.

Y áreas de aplicación: sistemas de computadoras, para evaluar hardware o requisitos de software; telecomunicaciones; transporte y energía, como autopistas, metros y puertos; aplicaciones militares y navales; economía; fabricación, con políticas de planificación e inventarios; personal en empresas de servicios, como bancos, comida rápida y correo; distribución y logística; y salud, con salas de urgencias y de operaciones, y planes de emergencia.

## El proceso de simulación: doce etapas

Este es el esquema del proceso completo, y es el hilo conductor de la materia. Son doce etapas.

Uno. Definición del problema: identificar y definir claramente el problema, con objetivos y alcance.

Dos. Formulación del modelo conceptual: una representación abstracta del sistema, con los componentes y relaciones esenciales. Por ejemplo, un diagrama de flujo del proceso.

Tres. Recopilación y análisis de datos: tiempos de operación, tasas de llegada.

Cuatro. Desarrollo del modelo de simulación: traducir el modelo conceptual a un modelo computarizado, con software de simulación.

Cinco. Verificación del modelo: asegurarse de que el modelo se implementó correctamente y funciona según lo previsto; que no tenga errores de programación.

Seis. Validación del modelo: comparar el modelo con el sistema real para asegurarse de que es una representación precisa, creíble y útil para el propósito. Por ejemplo, comparar los resultados de la simulación con datos históricos.

Siete. Diseño de experimentos: planificar qué variables se modificarán y cómo se medirán los resultados.

Ocho. Ejecución de experimentos: correr el modelo bajo diferentes condiciones y recolectar resultados.

Nueve. Análisis de resultados: sacar conclusiones y recomendaciones según los objetivos.

Diez. Documentación y reporte: documentar metodología, diseño, experimentos y resultados.

Once. Implementación de resultados: usar las recomendaciones para tomar decisiones y cambiar el sistema real.

Doce. Revisión y mantenimiento del modelo: actualizarlo para reflejar cambios en el sistema real.

La diferencia entre cinco y seis es una pregunta clásica. Verificación: ¿construimos bien el modelo? Es chequear que el programa hace lo que queremos. Validación: ¿construimos el modelo correcto? Es chequear que representa al sistema real. Verificación mira el programa; validación mira la realidad.

## Algunos conceptos importantes

Una cita atribuida a Einstein que aparece en el apunte: la formulación adecuada del problema es aún más esencial que su solución.

Una situación se vuelve un problema cuando el efecto de la operación del sistema no proporciona los resultados deseados.

Se desea construir un modelo del sistema real que no simplifique demasiado y que no contenga demasiados detalles.

Sobre la recopilación de datos: el uso de datos obtenidos en determinado año no necesariamente indicará algo sobre el comportamiento futuro del sistema.

Y sobre la validación: es imposible probar que cualquier simulador es un modelo correcto o verdadero del sistema real. Por eso nos importa la utilidad operativa del modelo y no la verdad de su estructura. Esta idea la vas a escuchar de nuevo en los ejes seis y ocho: un modelo no es verdadero o falso, es más o menos adecuado para responder una pregunta.

## Para cerrar: lo que más puede caer

Primero, las tres definiciones formales con su autor y su palabra clave: Shannon, experimentos con un modelo computarizado; Banks, historia artificial a través del tiempo, a mano o con computadora; Law, el modelo representa el sistema y la simulación representa su funcionamiento en el tiempo.

Segundo, la trampa de tus apuntes: desventajas de la experimentación directa no son desventajas de la simulación. Las de la experimentación directa son cinco: interrumpe operaciones, la gente cambia su comportamiento al ser observada, difícil mantener las mismas condiciones, difícil igualar el tamaño de muestra, y difícil explorar muchas alternativas.

Tercero, los cuatro propósitos: describir, postular teorías, predecir el impacto de cambios, evaluar decisiones sin costos ni riesgos.

Cuarto, las doce etapas del proceso, y la diferencia entre verificación y validación.

Quinto, que nadie resuelve el problema sino el modelo del problema, y que de un modelo importa su utilidad operativa y no la verdad de su estructura.

Eso es todo del eje uno.
