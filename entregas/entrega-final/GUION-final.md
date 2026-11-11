# Guion del video: entrega final del TPI

[TOC]

Duración objetivo: **12 a 13 minutos** (el máximo es 15). Los apartados siguen el orden que pide la consigna.

## Cómo leer este guion

- **🎥 Pantalla:** lo que se ve (captura de OBS, diapositiva o animación).
- **🗣️ Juan / Jonatan:** quién habla y qué dice, palabra por palabra.
- **Las frases en negrita dentro de la locución aparecen escritas en el video en el momento en que se dicen** (Claude Motion). El resto se dice sin texto en pantalla.
- Lo que está entre **[CORCHETES]** se completa cuando estén los resultados de FlexSim.

**Reparto de las voces:** cada orador se queda con bloques enteros, así cada uno graba sus partes de corrido y el cambio de voz marca el cambio de tema.

| Escena | Orador | Duración aprox. |
|---|---|---|
| 0 Apertura | Juan y Jonatan | 0:15 |
| 1 Organización | Juan | 0:45 |
| 2 Problemática | Juan | 0:45 |
| 3 Escenario base | Jonatan | 1:30 |
| 4 Render 3D | Jonatan | 0:30 |
| 5 Ejecución base | Jonatan | 1:15 |
| 6 Resultados base | Juan | 1:30 |
| 7 Alternativos | Juan y Jonatan, alternando | 3:00 |
| 8 Comparación | Jonatan | 1:15 |
| 9 Conclusión | Juan y cierre de Jonatan | 1:15 |

Queda en unos 6 minutos de locución para cada uno. A unas 130 palabras por minuto, el total ronda los **12 minutos**, y queda un minuto para pausas y transiciones.

**Reglas para las frases que aparecen en pantalla:**

- Son **2 o 3 por escena**, no más. Si todo aparece, nada se destaca.
- Aparecen **exactamente cuando se dicen**: en Claude Motion, la palabra arranca con la primera sílaba. Pueden salir palabra por palabra o la frase entera de una vez.
- Se quedan **2 o 3 segundos** después de dichas y se van antes de la siguiente.
- Los números importantes (minutos, porcentajes, personas) siempre van en pantalla: son lo que el profesor tiene que retener.
- La frase en pantalla puede ser **más corta** que la dicha. Si se dice «la espera media en la fila de caja es de 8 minutos», en pantalla alcanza con «Espera en caja: 8 min». En el guion, la negrita marca la parte que aparece.

> **Regla de la consigna:** no se nombra la organización. En la locución se dice siempre «un comedor universitario» o «el comedor». Antes de grabar, revisá que no se vea el nombre en el modelo de FlexSim (títulos, tablas, nombre del archivo en la barra de la ventana) ni en las diapositivas.

## Material grabado y de dónde salen los números

Las tomas están en [`flexsim/LISTA_DE_TOMAS.md`](../../flexsim/LISTA_DE_TOMAS.md), y las grabaciones, en `videos/una-caja.mkv` (escenario base) y `videos/dos-cajas.mkv` (E1).

> **Las grabaciones son una animación ilustrativa**, hecha con un replay de un escenario más exigente que el medido: la cola llega a 100 personas y la caja abre a las 12:01:54. **Ningún número que se diga en voz alta sale de la animación.** Los números de la locución salen del modelo medido ([`validacion_E0_Pico.md`](../../flexsim/validacion_E0_Pico.md)) y, para los escenarios alternativos, del Experimenter.
>
> Mientras se ve la animación, va un pie fijo y chico abajo: «Animación ilustrativa de un escenario más exigente que el medido».

| Escena | Tomas |
|---|---|
| 1 Organización | Toma 1 de `una-caja.mkv` (plano general, acelerada) |
| 2 Problemática | Final de la toma 1: la fila armada antes de abrir |
| 4 Render 3D | Toma 5 (una persona camino a la salida) y planos de la toma 1 |
| 5 Ejecución base | Tomas 2, 3 y 4 de `una-caja.mkv` |
| 7, E1 | Tomas 2 y 3 de `dos-cajas.mkv` y la fila de servicio llena (bloque 5 de la lista) |
| 7, E2 a E5 | Gráficos de barras y diagramas de caja del Experimenter |
| 4 Render 3D | Renders de `3d/video/artlist/` |
| 9 Conclusión | Toma 6 de las dos grabaciones, lado a lado |

> **Regrabar (Juan):** los audios de las escenas 6, 7 y 9 (`juan_escena06`, `juan_escena07-a`, `-b`, `-c` y `juan_escena09`) se grabaron con resultados viejos, en los que el cuello de botella era el mostrador. Hay que volver a grabarlos con este guion. Las escenas 1 y 2 siguen valiendo.
>
> En el bloque 1 de la lista de tomas, cambiar «Comedor Universitario UNC» por «Un comedor universitario».

---

# Escena 0 · Apertura (0:00 – 0:15)

- **🎥 Pantalla:** placa con fondo liso y los apellidos del grupo. Sobre el final, fundido a una foto o al plano 3D del comedor.

**🗣️ Juan:** «Hola. Somos [NOMBRE 1]…»

**🗣️ Jonatan:** «…y [NOMBRE 2]. En este video presentamos nuestro trabajo integrador de Simulación: **la fila de un comedor universitario, simulada en FlexSim**.»

---

# Escena 1 · Presentación de la organización (0:15 – 1:00)

- **🎥 Pantalla:** foto del comedor (sin carteles ni logos) o el plano 3D en vista aérea.

**🗣️ Juan:**

«La organización es un **comedor universitario** que sirve almuerzos subsidiados a estudiantes, becarios y personal. El almuerzo **se reserva antes por internet**.

Al llegar, cada persona hace una fila, **valida su reserva presentando el DNI** y pasa a otra fila para **retirar la bandeja en el mostrador**.

Simulamos ese recorrido: desde que la persona llega a la fila hasta que retira la bandeja. Lo que pasa después, en el salón, queda fuera del estudio.»

---

# Escena 2 · Problemática y objetivo (1:00 – 1:45)

- **🎥 Pantalla:** captura de la cola previa a las 11:59 en FlexSim. Cuando se lee la pregunta, la imagen se oscurece y la pregunta queda sola en el centro.

**🗣️ Juan:**

«En el horario pico se forma una fila larga antes de que abra la atención: **entre 60 y 70 personas**. Hay dos puestos de validación, pero **habitualmente funciona uno solo**.

La pregunta que nos hicimos es esta: **¿qué combinación de puestos de validación y personas en el servicio reduce el tiempo total en el pico, sin trasladar la cola al mostrador?**

La trampa es que si agilizamos la validación, la cola puede simplemente **correrse al mostrador**. Por eso medimos el **tiempo total**, y no solo la espera en la caja.»

> La pregunta es la frase más larga que aparece en todo el video: que se arme palabra por palabra mientras Juan la lee y quede fija unos 4 segundos. Si el grupo reformula la pregunta (D05), cambiá la locución y el texto juntos.

---

# Escena 3 · Escenario base (1:45 – 3:15)

- **🎥 Pantalla:** el Process Flow de FlexSim (la versión final, captura del 08/11), con zoom a cada bloque a medida que se nombra: las dos fuentes de llegadas, la validación, la decisión del menú vegetariano y el servicio. Después, la tabla `Escenarios` con la fila de E0 resaltada.

**🗣️ Jonatan:**

«Este es el **escenario base**, la situación de partida contra la que comparamos todo.

La caja abre alrededor de las 12, pero la gente llega antes: suponemos que la fila **empieza a formarse a las 11:40**. Ese horario no lo medimos; lo elegimos porque con él el modelo reproduce la fila que se ve en el comedor. La caja casi nunca abre en punto, y esa demora sí sale de los registros.

Después de la apertura, las llegadas salen de los **registros reales de reservas**, por franjas de diez minutos y por tipo de cliente.

Hay **un solo puesto de validación**. Cada persona presenta un DNI por ración, y cada DNI lleva **unos cuatro segundos**, un tiempo que sacamos de los registros del puesto.

Después pasa a la fila del servicio, donde **tres personas sirven**, a **unos 17 segundos por ración**. Una de ellas atiende el menú vegetariano.

Lo que pudimos sacar de los registros viene de ahí. Lo que no pudimos medir, como el tiempo de servicio o cuántas raciones retira cada persona, lo estimamos y lo declaramos como supuesto.»

> Los datos del escenario pueden ir apareciendo como una ficha en un costado: «Fila desde 11:40 (supuesto)», «1 puesto · 4 s por DNI», «3 sirviendo · 17 s por ración».

---

# Escena 4 · Renderizado 3D (3:15 – 3:45) · opcional

- **🎥 Pantalla:** los renders de `3d/video/artlist/` en orden: vista general, fila de caja, recorrido cenital y mostrador. Movimiento lento de cámara sobre cada imagen (Ken Burns). Si hay tiempo, cerrar con la toma 5 de FlexSim, una persona que sale con la bandeja.

**🗣️ Jonatan:** «Esta es la representación tridimensional del comedor. Por este pasillo se forma la **fila de caja**, acá están los **puestos de validación**, y por acá la gente avanza hacia el **mostrador**.»

> Las palabras en negrita funcionan como etiquetas que aparecen sobre cada sector cuando se nombran. Pie chico: «Renders mejorados con IA». Si el video se pasa de tiempo, esta escena es la primera que se recorta.

---

# Escena 5 · Ejecución del escenario base (3:45 – 5:00)

- **🎥 Pantalla:** `una-caja.mkv`, con el pie fijo «Animación ilustrativa de un escenario más exigente que el medido». Dos momentos:
  1. La fila armada antes de abrir y la apertura (toma 2).
  2. Plano general alejándose mientras la fila de caja baja (toma 3).
- **No usar** las tomas del mostrador con la fila de servicio llena: en el escenario base medido la fila del servicio no pasa de 5 personas.

**🗣️ Jonatan:**

«Corremos el escenario base en el día pico. Antes de que abra la caja ya hay **unas 70 personas** esperando.

Abre la caja y la fila empieza a bajar, pero tarda: con un solo puesto, en el pico llega gente casi tan rápido como se la atiende. Después del mostrador, en cambio, no se junta casi nadie: la fila del servicio **no pasa de cinco personas**.

En el escenario base, **el cuello de botella es la caja**.»

> «El cuello de botella es la caja» es la frase para resaltar: texto grande y una pausa de un segundo antes de decirla. Ningún número sale de la animación: salen del Experimenter.

---

# Escena 6 · Resultados del escenario base (5:00 – 6:30)

- **🎥 Pantalla:** el Experimenter con las 30 réplicas en verde (captura del 11/11, 06:26). Después, la tabla de E0 del informe, y al final el gráfico de raciones por franja, real contra modelo.

**🗣️ Juan:**

«Para tener resultados confiables, corrimos **30 réplicas** de cada escenario: 30 días simulados, cada uno con llegadas distintas.

En el día pico, quien llega antes de la apertura espera **unos 13 minutos**. Una vez abierta la caja, la espera más larga es de **casi 5 minutos**. La caja está ocupada el **63 %** del tiempo.

En el mostrador, la cola máxima es de **5 personas**, y la espera media, de **un segundo**.

Para validar el modelo, comparamos las raciones validadas cada diez minutos con los registros reales: la curva coincide, con una **correlación de 0,95**, y el total del día difiere en **menos de un 2 %**. La cola antes de la apertura y su espera también caen en lo que se observa en el comedor: **entre 60 y 70 personas** y **entre 10 y 15 minutos**.»

> En pantalla: «Cola previa: 13 min», «Espera máx. en caja: 4,9 min», «Caja: 63 %», «Mostrador: cola máx. 5», «Correlación: 0,95».

---

# Escena 7 · Escenarios alternativos (6:30 – 9:30)

Cada escenario dura unos 30 segundos y sigue la misma estructura: el nombre arriba a la izquierda, el diagrama de caja del Experimenter o una barra, y dos números. Los oradores **se alternan por escenario**.

- **🎥 Pantalla:** para E1, las tomas 2 y 3 de `dos-cajas.mkv` con el mismo encuadre que en la escena 5, y después la fila de servicio llena (bloque 5 de la lista de tomas): acá sí corresponde. Para E2 a E5, los gráficos de barras de la sección 11 del informe (espera máxima en caja y cola máxima en servicio), con el escenario de turno resaltado.

**🗣️ Juan:** «Ahora probamos cinco cambios sobre el escenario base. En cada uno **cambiamos una sola cosa**, así sabemos qué causa la diferencia.»

**🗣️ Jonatan (E1):** «**Escenario 1: dos puestos de caja todo el turno.** La espera más larga en la caja baja a la mitad, **de 5 a 2,4 minutos**. Pero miren el mostrador: la cola pasa de 5 a **31 personas**. **La cola no desapareció: se mudó al mostrador.**»

**🗣️ Juan (E2):** «**Escenario 2: el segundo puesto solo en el pico**, de 12 a 13:30. Da **exactamente lo mismo que el escenario 1**. Después de las 13:30 alcanza con un solo puesto.»

**🗣️ Jonatan (E3):** «**Escenario 3: validación con código QR**, que tarda un 60 % de lo que tarda el DNI. Mejora la caja, pero menos que un segundo puesto: **2,9 minutos**. Y también corre cola al mostrador: **23 personas**.»

**🗣️ Juan (E4):** «**Escenario 4: un solo puesto y cuatro personas sirviendo.** **No cambia casi nada**: el mostrador ya alcanzaba, el problema estaba en la caja.»

**🗣️ Jonatan (E5):** «**Escenario 5: dos puestos y cuatro personas sirviendo.** La caja mejora igual que en el escenario 1, **2,4 minutos**, y la cola del mostrador queda en **16 personas**, la mitad que en el escenario 1. **Es el que logra el menor tiempo total.**»

> «La cola no desapareció: se mudó al mostrador» es la idea central del video: texto grande y pausa antes.

---

# Escena 8 · Comparación de resultados (9:30 – 10:45)

- **🎥 Pantalla:** dos gráficos de barras lado a lado con los seis escenarios: a la izquierda, la espera máxima en la caja; a la derecha, la cola máxima en el servicio. E0 en gris oscuro, E5 en el color de acento y el resto en gris claro. Después, la tabla de abajo.

**🗣️ Jonatan:**

«Pongamos todo junto. A la izquierda, la caja: **todo lo que agrega capacidad en la caja la mejora**, y reforzar solo el mostrador no le hace nada. A la derecha, el mostrador: **todo lo que mejora la caja le manda gente**.

La única combinación que mejora la caja y contiene el mostrador es la del **escenario 5**. Como las 30 réplicas de cada escenario usan las mismas llegadas, comparamos réplica por réplica, y todas estas diferencias son **estadísticamente significativas**.

En promedio, el tiempo total baja **unos 13 segundos por persona**. Parece poco, pero el promedio incluye a la mayoría, que llega cuando no hay fila. **La mejora la siente quien llega en el pico**: su espera se reduce a la mitad.»

Tabla (día pico, media de 30 réplicas; la misma está en el informe):

| Escenario | Espera máx. en caja (min) | Cola máx. caja | Cola máx. servicio | Tiempo total medio (min) | Utilización de la caja (%) |
|---|---|---|---|---|---|
| E0 base | 4,9 | 71 | 5 | 1,14 | 63 |
| E1 2 puestos | 2,4 | 71 | 31 | 0,98 | 31 |
| E2 2 puestos hasta 13:30 | 2,4 | 71 | 31 | 0,99 | 31 |
| E3 QR | 2,9 | 71 | 23 | 0,96 | 38 |
| E4 4 sirviendo | 4,9 | 71 | 3 | 1,13 | 63 |
| E5 2 puestos y 4 sirviendo | **2,4** | 71 | **16** | **0,92** | 31 |

---

# Escena 9 · Conclusión (10:45 – 12:10)

- **🎥 Pantalla:** vuelve la pregunta de la escena 2, achicada arriba; la respuesta se escribe debajo mientras Juan la dice. Para el cierre de Jonatan, la toma 6 de las dos grabaciones lado a lado. Las horas de salida de la animación no se dicen ni se escriben.

**🗣️ Juan:**

«Volvamos a la pregunta. **Con dos puestos de validación en el pico y cuatro personas sirviendo.**

Abrir el segundo puesto, solo, no alcanza: la cola **se pasa al mostrador**. Reforzar solo el mostrador tampoco, porque el problema estaba en la caja. Hay que hacer **las dos cosas juntas**.

Nuestra recomendación es abrir el segundo puesto **de 12 a 13:30** y sumar una persona al mostrador en ese horario.»

**🗣️ Jonatan:**

«Dos aclaraciones para cerrar. Ningún escenario cambia la espera de quienes llegan antes de la apertura: eso depende de **a qué hora llega la gente** y de que la caja abra puntual. Y el tiempo de servicio por ración no lo pudimos cronometrar: es un supuesto, y el siguiente paso sería **medirlo en el comedor**. Gracias por mirar.»

- **Cierre (12:10 – 12:20):** placa final con los apellidos y «Simulación · 2026». Sin música fuerte.

---

# Tips para grabar y editar

## Antes de grabar

- **Grabá la voz primero y la pantalla después.** Con la locución ya grabada sabés cuánto tiene que durar cada fragmento de FlexSim, y no te trabás leyendo mientras manejás el mouse.
- **Leé el guion en voz alta una vez cronometrando.** Si pasa de 12 minutos sin pausas, recortá frases antes de grabar, no en la edición.
- **Escribí como hablás.** Frases cortas, una idea por frase. Si una oración necesita una coma en el medio para respirar, partila en dos.
- **Dos voces, dos lugares:** si cada orador graba en su casa, usen el mismo tipo de micrófono y la misma distancia, y procesen las dos voces con los mismos ajustes en Audify para que no suene como dos videos pegados. Cada uno graba solo sus bloques de la tabla de reparto.
- **Dejá todos los resultados listos antes de grabar la pantalla:** el Dashboard armado y los gráficos exportados. No hay que buscar nada en vivo.

## Configuración de OBS

- **Resolución y cuadros:** 1920 × 1080 a 30 fps alcanzan. FlexSim no necesita 60 fps.
- **Formato:** grabá en **MKV** (si se corta, no perdés el archivo) y convertilo a MP4 desde *Archivo → Remux*.
- **Calidad:** en *Salida*, modo simple, calidad «Alta» o «Indistinguible». Encoder por hardware (NVENC o QuickSync) si tenés, para que FlexSim no se trabe mientras graba.
- **Una escena de OBS por tipo de toma:** pantalla completa de FlexSim, solo el Process Flow, solo la vista 3D. Así cambiás sin mover ventanas.
- **Escala de pantalla:** si trabajás con la escala de Windows al 125 % o 150 %, bajala al 100 % para grabar o agrandá las fuentes de FlexSim. El texto chico de los Process Flow no se lee en un video.
- **Grabá la pantalla sin audio** (o con el micrófono silenciado) si la voz va aparte. Evita ecos y clics de teclado.

## Al grabar FlexSim

- **Limpiá la pantalla:** cerrá las notificaciones (modo «No molestar» de Windows), el chat y las pestañas del navegador. Que no aparezcan el nombre de la organización, tu mail del trabajo ni rutas de OneDrive con el nombre de la empresa.
- **Mové el mouse despacio** y dejalo quieto cuando no señalás nada. Un cursor que da vueltas distrae.
- **Usá la velocidad de simulación a tu favor:** corré rápido las partes aburridas y bajá la velocidad en los momentos clave (apertura de las 12:00, pico de la cola). En la edición podés acelerar más.
- **Grabá tomas largas y de sobra.** Es más fácil recortar que volver a abrir FlexSim, configurar el escenario y repetir.
- **Fijá la semilla** del generador para la corrida que grabes, así la corrida del video coincide con los números que mostrás.
- **Hacé zoom en la edición, no en FlexSim:** grabá la vista amplia y acercá en Claude Motion a la zona que importa. Queda más prolijo que acercar en vivo.

## Locución

- **Micrófono:** cualquier auricular con micrófono anda mejor que el de la notebook. A un puño de distancia de la boca, un poco al costado para que no pegue el aire de la «p».
- **Ambiente:** una habitación con ropa, cortinas o un placard abierto absorbe el eco. Evitá cocinas y paredes desnudas.
- **Grabá 10 segundos de silencio** al principio de cada sesión. Es la muestra que usa la reducción de ruido.
- **Si te equivocás, no cortes:** hacé una pausa de dos segundos y repetí la frase entera desde el principio. En la edición se ve clarito dónde cortar.
- **Grabá por escena,** un archivo por bloque de cada orador (por ejemplo `Juan-escena2.wav`). Si una escena sale mal, rehacés solo esa. En la escena 7, cada orador graba sus escenarios por separado.
- **Sonreí al hablar.** Se escucha. Y hablá un poco más lento de lo que te parece natural.
- **Mismo lugar y mismo micrófono para todo,** así las escenas suenan iguales.

## Corrección de voz con Audify

Orden recomendado (cada paso funciona mejor sobre el anterior):

1. **Reducción de ruido**, con la muestra de silencio. Suave: si te pasás, la voz suena metálica o «bajo el agua».
2. **Recorte de muletillas y silencios largos.** Revisá a mano lo que corta automáticamente: a veces se lleva el principio de una palabra.
3. **De-esser** para las eses. También suave: con demasiado, suena a ceceo.
4. **Normalización** a un volumen parejo para todas las escenas (si da la opción, alrededor de -16 LUFS, el estándar de video en internet).

Hacé todo esto **antes** de llevar la voz a la edición, así sincronizás las letras sobre el audio final.

## Edición en Claude Motion

- **La voz manda:** armá primero la pista de la locución completa y después acomodá el video de FlexSim debajo.
- **Frases que aparecen al decirlas:** sincronizalas sobre la forma de onda de la voz ya procesada, con la primera sílaba. Máximo 6 a 8 palabras en pantalla a la vez; si la frase dicha es larga, mostrá solo la parte en negrita del guion.
- **Que cada frase dure** lo suficiente para leerla dos veces (unos 2 a 3 segundos después de dicha) y que salga antes de que aparezca la siguiente.
- **Una sola tipografía y dos colores:** uno neutro para todo y uno de acento para lo que hay que mirar (el escenario mejor, el número clave). Usá el mismo color de acento en todo el video.
- **Transiciones:** cortes directos o fundidos cortos. Nada de efectos de giro o barrido.
- **Música:** opcional, instrumental y muy baja debajo de la voz (unos 20 a 25 dB menos). Si hay duda, sin música. Usá música libre de derechos.
- **Subtítulos:** suman si el profesor ve el video sin audio o acelerado. Si Claude Motion los genera desde la locución, revisalos.

## Antes de entregar

- **Mirá el video completo de una vez,** sin pausas, como lo vería el profesor. Anotá dónde te aburrís: eso se recorta.
- **Chequeá el tiempo:** 12 a 13 minutos. Nunca más de 15.
- **Buscá el nombre de la organización** en todo el video, cuadro por cuadro en las capturas de FlexSim.
- **Escuchá con auriculares y con parlantes:** detecta ruidos y volúmenes que con uno solo no se notan.
- **Exportá en MP4 (H.264), 1080p.** Probá que el archivo se abra en otra computadora antes de subirlo al campus, y fijate el límite de tamaño del campus: si lo pasa, subilo a Drive y entregá el enlace.

---

# Checklist de grabación

- [ ] Pregunta de estudio cerrada (D05) y placa de la escena 2 actualizada
- [x] Resultados de E0 a E5 con réplicas y la tabla de la escena 8 completa
- [ ] Juan: regrabar las escenas 6, 7 y 9
- [ ] Gráficos exportados: colas en el tiempo, tiempo total, utilización y comparación
- [ ] Nombre de la organización fuera del modelo y de las capturas
- [ ] Locución grabada por escena y procesada en Audify
- [ ] Tomas de FlexSim grabadas en OBS (escenas 3, 4, 5, 6 y 7)
- [ ] Edición, textos y subtítulos en Claude Motion
- [ ] Revisión completa, duración entre 12 y 13 minutos
- [ ] MP4 exportado y probado en otra computadora
