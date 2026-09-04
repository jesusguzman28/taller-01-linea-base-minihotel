# Lista de Cotejo — Línea Base MiniHotel (variante Python)

**Unidad Didáctica:** Gestión de la Calidad del Software
**Programa de estudios:** Desarrollo de Sistemas de Información — Período IV — 2026-II
**Docente:** Ing. Pedro Jesús Guzmán Ramos
**Sesión de aprendizaje:** Auditoría de línea base
**Indicador de logro (C5.I1):** Identifica los aspectos básicos de la calidad del software para ser implementados en las organizaciones.
**Logro de la sesión:** El estudiante **elabora la línea base de calidad de un sistema clasificando sus hallazgos según ISO/IEC 25010.**
**Instrumento:** Lista de cotejo (verificación dicotómica Sí / No).

| Dato | |
|---|---|
| Fecha | ____/____/2026 |
| Estudiante / Célula | ______________________________________ |
| Integrantes | ______________________________________ |
| Sistema evaluado | MiniHotel v0.1 |

---

## Instrucciones

Marque **Sí** solo si el criterio se cumple **completamente y con evidencia**;
en caso contrario, marque **No**. Cada ítem vale **1 punto**. La verificación
se hace sobre los entregables E1–E5 de la actividad y la observación en aula.

---

## Dimensión 1 — Levantamiento del sistema (E1)

| # | Criterio | Sí | No | Evidencia |
|---|---|:--:|:--:|---|
| 1 | Ejecutó MiniHotel con `python main.py` / script sin errores. | | | E1 |
| 2 | Ejecutó el sistema y mostró el menú principal en funcionamiento. | | | E1 |
| 3 | La evidencia (captura) identifica equipo/entorno (SO y versión de Python). | | | E1 / ficha §0 |

## Dimensión 2 — Exploración del sistema (E2)

| # | Criterio | Sí | No | Evidencia |
|---|---|:--:|:--:|---|
| 4 | Ejecutó los 10 pasos del guion de exploración del README. | | | E2 |
| 5 | Cada paso de la bitácora indica: acción realizada, resultado esperado y resultado obtenido. | | | E2 |
| 6 | Adjuntó capturas de pantalla que respaldan lo observado. | | | E2 |
| 7 | Detectó el fallo de caída del programa al ingresar un dato no numérico en "noches". | | | E2 / ficha §3 |
| 8 | Detectó el cálculo incorrecto del descuento por porcentaje. | | | E2 / ficha §3 |

## Dimensión 3 — Uso correcto del modelo ISO/IEC 25010 (E3)

| # | Criterio | Sí | No | Evidencia |
|---|---|:--:|:--:|---|
| 9 | La ficha de diagnóstico registra al menos **8 hallazgos**. | | | E3 |
| 10 | Cada hallazgo tiene **todos** los campos obligatorios completos (ID, pasos, esperado/obtenido, característica, subcaracterística, severidad, evidencia, estado). | | | E3 §3 |
| 11 | Cada hallazgo está asignado a **una** de las 8 características ISO/IEC 25010. | | | E3 §5 |
| 12 | Las asignaciones de característica son **correctas** en al menos el 80 % de los hallazgos. | | | E3 §5 |
| 13 | Indicó la **subcaracterística** correspondiente en cada hallazgo. | | | E3 §5 |
| 14 | Cubrió con hallazgos **al menos 6 de las 8** características. | | | E3 §6 |
| 15 | Distinguió correctamente **calidad interna / externa / en uso** al menos en la sección de datos generales y en los hallazgos. | | | E3 §0, §5 |

## Dimensión 4 — Línea base y clasificación (E3, E4)

| # | Criterio | Sí | No | Evidencia |
|---|---|:--:|:--:|---|
| 16 | Completó el **resumen por característica** con calificación provisional (C/O/NC/NE). | | | E3 §5 |
| 17 | Completó la **tabla consolidada** de hallazgos por característica y severidad, con totales correctos. | | | E3 §6 / E4 |
| 18 | Identificó y **justificó con datos** cuál es la característica más comprometida. | | | E3 §6 / E5 |
| 19 | Registró los **aspectos no evaluados** y qué se necesitaría para evaluarlos. | | | E3 §7 |
| 20 | Redactó el **enunciado de la línea base** de forma objetiva (describe el estado, sin juicios de valor ni propuestas de solución). | | | E3 §8 / E5 |

## Dimensión 5 — Verificación en el código (obligatoria, no eliminatoria)

| Criterio (no puntúa en el vigesimal; se verifica como requisito de entrega) | Sí | No | Evidencia |
|---|:--:|:--:|---|
| Completó los 4 bloques de reconocimiento inicial del código (CR1–CR4). | | | E3 §1 |
| Completó los 8 bloques de verificación de causa en el código (PB1–PB8), con comando y resultado pegados en cada uno. | | | E3 §4 |

> Estos dos bloques ahora son **obligatorios para entregar** (con la sesión de 3 h ya hay tiempo suficiente), pero no suman puntos aparte: si faltan, la ficha se considera **incompleta** y no se puede calificar hasta completarlos.

---

## Actitud observada (registro cualitativo — no puntúa, orienta la retroalimentación)

| Aspecto | Observación |
|---|---|
| **Objetividad**: reporta lo observado con evidencia, sin exagerar ni minimizar los hallazgos | |
| Honestidad al declarar lo que no alcanzó a evaluar | |
| Trabajo colaborativo dentro de la célula | |

---

## Calificación

| | |
|---|---|
| Ítems marcados **Sí** | ______ / 20 |
| **Nota vigesimal = (Sí ÷ 20) × 20** | ______ / 20 |
| Condición | ☐ Aprobado (≥ 13)  ☐ Desaprobado (< 13) |

---

## Retroalimentación

**Logros:**
_____________________________________________________________________________

**A mejorar:**
_____________________________________________________________________________

<br>

______________________________  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ______________________________
Firma del docente &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Firma del estudiante / delegado de célula
