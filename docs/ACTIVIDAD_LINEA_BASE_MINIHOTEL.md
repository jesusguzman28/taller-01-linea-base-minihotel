# Actividad — Auditoría de línea base con ISO/IEC 25010 (variante MiniHotel / Python)

> **Indicador de logro (C5.I1):** Identifica los aspectos básicos de la calidad
> del software para ser implementados en las organizaciones.
> **Logro de la sesión:** *"Al finalizar la sesión, el estudiante elabora la
> línea base de calidad de un sistema clasificando sus hallazgos según ISO 25010."*
> **Instrumento de evaluación:** Lista de cotejo (`LISTA_COTEJO_MINIHOTEL.md`).
> **Contenido:** modelo ISO/IEC 25010, calidad interna/externa, línea base de diagnóstico.

---

## 1. Contexto (ABP de la unidad)

La unidad se desarrolla con **Aprendizaje Basado en Proyectos**: durante el
semestre auditarás un sistema de información real y decidirás, con evidencia,
si está en condiciones de ser liberado a producción.

**Hoy es el punto de partida.** Recibes **MiniHotel**, un sistema de reservas
de hotel que "ya funciona", y tienes que levantar su **línea base de
calidad**: describir objetivamente su estado actual según un modelo estándar
(ISO/IEC 25010), sin corregir nada todavía.

- **Modalidad:** células de 2–3 estudiantes.
- **Duración:** 1 sesión (3 h).
- **Sistema:** MiniHotel (Python + Tkinter, aplicación de escritorio). Ver `README.md` para levantarlo.

---

## 2. Marco conceptual (lo mínimo que debes manejar)

### 2.1. Calidad interna, externa y en uso

| Tipo | Qué mira | Cómo se observa hoy |
|---|---|---|
| **Interna** | Propiedades del código y diseño (estructura, complejidad) | **Primer vistazo guiado al código** *(Sección 1, obligatorio)* y **verificación de causa** *(Sección 4, obligatorio)*; el análisis de código a fondo con métricas y herramientas estáticas sigue siendo de semanas posteriores |
| **Externa** | Comportamiento del sistema en ejecución (fallos, tiempos, errores) | **Usando el sistema** *(Secciones 2–3, lo central de hoy)* |
| **En uso** | Resultado para el usuario real (eficacia, satisfacción, riesgo) | Pruebas con usuarios / operación *(más adelante)* |

En esta sesión trabajas sobre todo la **calidad externa**, pero con la
sesión de 3 h ahora sí alcanza para tocar la **calidad interna** dos veces:
antes de arrancar (orientación) y después de explorar (confirmación).

> **Obligatorio (código):** la ficha de diagnóstico trae dos bloques de
> código, ya no opcionales:
> - **Sección 1 — Primer vistazo al código (CR1–CR4):** antes de arrancar la
>   app, un recorrido guiado por los 5 archivos de `src/minihotel/` (cuántos
>   archivos y líneas hay, dónde está el punto de entrada, cuántos métodos
>   tiene cada archivo, y ubicar los comentarios `Defecto sembrado`/`BUG` que
>   el propio código trae). Solo orientación, todavía no hay veredicto.
> - **Sección 4 — Verificación en el código (PB1–PB8):** después de explorar
>   la ventana, confirmas en el código la causa real de los hallazgos más
>   importantes (descuento, sobreventa, "cancelar" que no libera, arqueo de
>   caja, ruta fija, reporte lento, moneda inconsistente).
>
> Ambos bloques indican **exactamente** qué archivo abrir y qué palabra
> buscar (pensado para quien lee código por primera vez); si te faltan, la
> ficha se considera incompleta (ver `LISTA_COTEJO_MINIHOTEL.md`, Dimensión 5).

### 2.2. Modelo de calidad del producto ISO/IEC 25010

8 características (modelo 2011, el que usaremos). Cada una tiene
subcaracterísticas; te basta con reconocer la característica principal.

| # | Característica | Pregunta guía | Subcaracterísticas |
|---|---|---|---|
| 1 | **Adecuación funcional** | ¿Hace lo que debe, completo y correcto? | Completitud, corrección, pertinencia |
| 2 | **Eficiencia de desempeño** | ¿Responde rápido y usa bien los recursos? | Comportamiento temporal, uso de recursos, capacidad |
| 3 | **Compatibilidad** | ¿Coexiste e intercambia datos con otros sistemas? | Coexistencia, interoperabilidad |
| 4 | **Usabilidad** | ¿Es fácil de entender, aprender y operar? ¿Protege del error? | Reconocibilidad, aprendizaje, operabilidad, protección ante errores, estética, accesibilidad |
| 5 | **Fiabilidad** | ¿Se mantiene funcionando y se recupera de fallos? | Madurez, disponibilidad, tolerancia a fallos, recuperabilidad |
| 6 | **Seguridad** | ¿Protege la información y controla el acceso? | Confidencialidad, integridad, no repudio, responsabilidad, autenticidad |
| 7 | **Mantenibilidad** | ¿Es fácil de analizar, modificar y probar? | Modularidad, reusabilidad, analizabilidad, modificabilidad, testeabilidad |
| 8 | **Portabilidad** | ¿Se adapta, instala y reemplaza en otros entornos? | Adaptabilidad, instalabilidad, reemplazabilidad |

> *Nota:* la revisión **ISO/IEC 25010:2023** añade **Seguridad funcional
> (Safety)** como 9.ª característica y reorganiza algunas subcaracterísticas.
> Para este taller usamos el modelo de 8; menciónalo en tu informe si quieres
> punto extra de rigor.

---

## 3. Entregables

| # | Entregable | Formato |
|---|---|---|
| E1 | Evidencia de que **el sistema levanta**: captura del menú de MiniHotel en ejecución | PNG / PDF |
| E2 | **Bitácora de exploración**: los 10 pasos del guion del README con lo observado y capturas | MD / PDF |
| E3 | **Ficha de diagnóstico ISO/IEC 25010 completa** (`FICHA_DIAGNOSTICO_ISO25010_MINIHOTEL.md`), con ≥ 8 hallazgos, uno por cada característica al menos intentado | MD / hoja de cálculo |
| E4 | **Tabla resumen de línea base**: hallazgos clasificados por característica + severidad + estado "abierto" | En el informe |
| E5 | **Informe de línea base** (máx. 2 páginas): interpretación, característica más débil, y respuesta a las preguntas del punto 6 | PDF |

---

## 4. Procedimiento

1. **Levantar** MiniHotel (README §2). Captura → E1.
2. **Explorar** con el guion del README §3. Llena la bitácora → E2.
   - Regla de oro: **objetividad**. Anota lo que *observaste*, no lo que
     *supones*. Cada hallazgo lleva evidencia reproducible (qué tecleaste).
3. Para **cada hallazgo**, completa una fila de la **ficha de diagnóstico**:
   - ID, descripción, **cómo reproducirlo**, resultado esperado vs. obtenido,
     **característica ISO/IEC 25010**, subcaracterística, **severidad**,
     evidencia (captura).
4. **Clasificar**: agrupa los hallazgos por característica. Cuenta cuántos
   caen en cada una → esa es tu **línea base** (E4).
5. **Interpretar** (E5): ¿cuál es la característica más comprometida? ¿el
   sistema, tal como está, podría operar en un hotel real? ¿qué NO pudiste
   evaluar hoy y por qué?

### Escala de severidad (úsala en la ficha)

| Severidad | Criterio |
|---|---|
| **Crítica** | Pérdida de datos, dinero mal calculado, caída total, o brecha de seguridad. |
| **Mayor** | Funcionalidad clave da resultado incorrecto o el sistema se vuelve inusable en un flujo común. |
| **Menor** | Molesta o confunde, pero hay forma de continuar. |
| **Observación** | Mejora deseable; no impide operar. |

---

## 5. Pistas de dónde mirar (sin resolverlo por ti)

Con el guion de exploración deberías poder ubicar hallazgos en **al menos 6**
de las 8 características. Si te faltan, revisa:

- ¿Qué pasa con el **descuento** y con el **arqueo de caja**? → una característica.
- ¿Qué pasa al escribir una **letra** en "noches"? ¿Y al **cerrar** el programa? → otra.
- ¿Te pidió **clave** para ver la caja o cancelar una reserva? ¿Dónde está la clave? → otra.
- ¿Cuánto **tardó** el reporte? → otra.
- Abre el **CSV exportado** en Excel. ¿A qué carpeta fue? → dos características.
- Mira los **mensajes de error** y las **confirmaciones** → otra.
- Mira la **estructura del proyecto** (`src/`): ¿está bien repartido el código? → otra.

---

## 6. Preguntas del informe (E5)

1. ¿Por qué se dice que MiniHotel "funciona" y aun así tiene mala calidad?
   Relaciónalo con calidad **externa** vs. **en uso**.
2. De las 8 características, ¿cuál es la **más débil** de MiniHotel según tu
   línea base? Justifícalo con el número de hallazgos y su severidad.
3. Elige **un** hallazgo **crítico** y explica qué incidente real podría
   provocar en un hotel (dinero, sobreventa de habitaciones, huéspedes).
4. ¿Qué característica **no pudiste diagnosticar bien** con solo usar el
   sistema? ¿Qué necesitarías (herramienta, dato, acceso) para evaluarla?
5. ¿Para qué le sirve a un equipo tener esta **línea base** documentada antes
   de empezar a mejorar el sistema?

---

## 7. Criterios de evaluación

La sesión se evalúa con la **lista de cotejo** (`LISTA_COTEJO_MINIHOTEL.md`):
20 ítems verificables (Sí / No), agrupados en *Levantamiento del sistema*,
*Exploración*, *Uso correcto del modelo ISO/IEC 25010*, *Línea base y
clasificación*, y *Objetividad del reporte*.

Conversión: **Nota = (ítems "Sí" ÷ 20) × 20**. Mínima aprobatoria de la UD: **13**.

---

## Anexo — Clave de referencia (uso del docente)

Hallazgos sembrados en MiniHotel y su clasificación esperada:

| Hallazgo observable | Característica ISO/IEC 25010 | Sev. |
|---|---|---|
| El descuento del 10 % resta S/ 10 al precio en vez de multiplicar (H101 → S/ 70 en vez de S/ 72) | Adecuación funcional (corrección) | Crítica |
| "Cancelar reserva" deja la habitación en estado "Ocupada" | Adecuación funcional (corrección) | Mayor |
| Deja reservar una habitación que ya está "Ocupada" (sobreventa / doble reserva) | Adecuación funcional / Fiabilidad | Mayor |
| El arqueo de caja no refleja los descuentos aplicados (a caja entra el precio sin descuento) | Adecuación funcional (corrección) | Mayor |
| Escribir una letra en **Cantidad de noches** aborta la operación con stack trace en la consola, sin mensaje al usuario | Fiabilidad (tolerancia a fallos) | Mayor |
| "Ver caja" y "Cancelar reserva" no piden autenticación | Seguridad (control de acceso) | Mayor |
| Clave de administrador embebida en el código ("hotel123"), y además nunca se usa | Seguridad (confidencialidad) | Crítica |
| Acepta descuentos y precios negativos | Seguridad (integridad) / Func. | Mayor |
| El reporte "habitación más reservada" tarda ~1.5 s (pausa + O(n²)) y congela la ventana | Eficiencia de desempeño (comportamiento temporal) | Mayor |
| Mensajes de error crípticos ("E01"), sin ayuda | Usabilidad (protección ante errores / operabilidad) | Mayor |
| "Cancelar reserva" no pide confirmación | Usabilidad (protección ante errores) | Menor |
| Catálogo de habitaciones desalineado, símbolo de moneda inconsistente ("S/" vs "S/.") | Usabilidad (reconocibilidad) | Menor |
| Exporta siempre a `C:\temp\reservas.csv` (ruta fija de Windows) | Portabilidad (adaptabilidad) | Mayor |
| Fecha del CSV fija al formato por defecto del sistema | Portabilidad (adaptabilidad) | Menor |
| CSV con separadores mezclados (","/";"), sin comillas | Compatibilidad (interoperabilidad) | Mayor |
| Todo el código de interfaz y flujo en `app.py`; búsqueda de habitación por código duplicada 3× en `hotel.py` | Mantenibilidad (modularidad / modificabilidad) | Mayor |

Cobertura esperada: 8/8 características con al menos un hallazgo.
Distribución típica de la línea base: Adecuación funcional 4, Fiabilidad 2,
Seguridad 3, Usabilidad 3, Portabilidad 2, Compatibilidad 1, Eficiencia 1,
Mantenibilidad 1.

> **Nota:** el guardado/recarga de datos (`datos/reservas.txt`) **sí
> funciona correctamente**: es el único punto conforme; los demás defectos
> siguen sembrados.
