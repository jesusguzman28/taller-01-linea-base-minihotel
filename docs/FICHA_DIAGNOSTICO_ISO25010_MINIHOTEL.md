# Ficha de Diagnóstico de Calidad — ISO/IEC 25010

## Línea base de MiniHotel (aplicación de escritorio, Python + Tkinter)

**Unidad Didáctica:** Gestión de la Calidad del Software
**Programa:** Desarrollo de Sistemas de Información — 2026-II — Período IV
**Docente:** Ing. Pedro Jesús Guzmán Ramos

---

## Cómo se llena esta ficha (léelo una vez)

Esta ficha se llena **completa dentro de este documento**. No hay carpeta aparte: la evidencia se **pega aquí mismo**.

| Símbolo | Qué haces |
|---|---|
| **▶️ Haz esto** | Sigues los pasos al pie de la letra, en orden. |
| **✍️ ESCRIBE AQUÍ** + líneas **amarillas** | Escribes **sobre las líneas amarillas** el texto o número **exacto** que salió en pantalla. |
| **❓ marca una con una X** + ☐ | Pones una `X` dentro de **un** cuadro: ☐ → X. |
| **📸 PEGA AQUÍ LA CAPTURA** | Tomas la captura (`Win + Shift + S`) y la **pegas dentro del recuadro** (`Ctrl + V`). |
| **💻 PEGA AQUÍ EL COMANDO** | Copias de la terminal el comando **y su resultado** y lo pegas en el recuadro. |
| **🏷️ Severidad** | Marcas una con una X. Abajo hay una *Sugerida* con el motivo. |

**Reglas:** (1) no corrijas nada, solo describe;  (2) sin captura, el hallazgo no cuenta;  (3) escribe lo que **viste**, no lo que supones.

**Escala de severidad:**  **Crítica** = dinero mal calculado / pérdida de datos / caída / brecha de seguridad · **Mayor** = función clave incorrecta o flujo común inusable · **Menor** = molesta pero se puede continuar · **Observación** = mejora deseable.

---

## Sección 0 · Datos generales  *(llénalo ANTES de empezar)*

Para los campos con comando: ábrelo en la terminal, en la carpeta del repositorio.

**Commit auditado** — comando: `git rev-parse --short HEAD`

[________________________________________]{.mark}

**Sistema operativo** — comando: `(Get-CimInstance Win32_OperatingSystem).Caption`

[__________________________________________________]{.mark}

**Versión de Python** — comando: `python --version`

[__________________________________________________]{.mark}

**Fecha (dd/mm/2026)** · **Código de célula** · **Integrantes** · **Responsable del reporte**

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}


**Tipo de calidad evaluada:** Externa (caja negra).

---

## Sección 1 · Primer vistazo al código (obligatorio, antes de arrancar el sistema)

Con más tiempo de sesión, empiezas **mirando el código por encima** antes de tocar la ventana. No necesitas entenderlo todo, solo ubicarte: qué archivos hay y qué hace cada uno. Los hallazgos de calidad vienen después, en la Sección 3; aquí solo te orientas.

**🧭 Mapa de archivos** — toda la aplicación vive en `src/minihotel/`:

| Archivo | Qué contiene (y nada más) |
|---|---|
| `main.py` | Punto de entrada: solo llama a `app.py` |
| `src/minihotel/habitacion.py` | La clase `Habitacion` (los datos de una habitación) |
| `src/minihotel/hotel.py` | Toda la lógica: reservar, cancelar, descuento, caja |
| `src/minihotel/reporte.py` | El reporte y la exportación a CSV |
| `src/minihotel/app.py` | La ventana y los botones (la interfaz) |

### 🔎 Cómo buscar dentro del código (léelo antes de CR1 — se usa en toda la ficha)

Nunca vas a leer un archivo completo de arriba a abajo: **buscas una palabra puntual** y miras solo alrededor. Dos formas, usa la que te sea más cómoda:

**Opción A — con el editor (Ctrl+F):**

1. Abre el archivo con **VS Code** o **Notepad++** (no hace falta instalar nada más pesado). Evita el Bloc de notas de Windows: no muestra número de línea, y lo vas a necesitar.
2. Con el archivo abierto, presiona **Ctrl+F**. Aparece un cuadro de búsqueda arriba o al costado.
3. Escribe **exactamente** la palabra que se te pide en cada bloque (por ejemplo `def cancelar`), tal cual, sin comillas.
4. Presiona **Enter**. El editor salta a la primera coincidencia y la resalta en amarillo/verde.
5. Mira el número de línea: en VS Code aparece abajo a la derecha ("Ln 131, Col 5"); en Notepad++ aparece en la columna gris de la izquierda. Ese número es el que escribes en "Ubicación exacta".

**Opción B — con el comando de la terminal (más rápido, y ya lo tienes):**

Los comandos `grep -n` / `Select-String` que se dan en cada bloque **ya imprimen el número de línea** al inicio de cada resultado. Por ejemplo, si el resultado dice:

```
131:    def cancelar(self, codigo):
```

el `131` de antes de los dos puntos **es el número de línea**. No necesitas abrir el editor para esto — solo para leer más contexto alrededor si te hace falta.

**Para la "Ubicación exacta del error":** escribe `archivo.py:número` (por ejemplo `hotel.py:131`), usando cualquiera de las dos opciones de arriba.

---

### CR1 · Cuenta archivos y líneas del proyecto

**Comando(s) a usar:**

```
(Get-ChildItem -Recurse -Filter *.py src).Count                                  (PowerShell)
(Get-ChildItem -Recurse -Filter *.py src | Get-Content | Measure-Object -Line).Lines   (PowerShell)
find src -name "*.py" | wc -l ; find src -name "*.py" | xargs wc -l               (Git Bash)
```

+--------------------------------------------------------------------------+
| 💻 PEGA AQUÍ EL COMANDO Y SU RESULTADO (CR1)                              |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+

**✍️ ¿Cuántos archivos `.py` tiene el proyecto? ¿Cuántas líneas en total (aprox.)?** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

---

### CR2 · Encuentra el punto de entrada

**▶️ Haz esto:** abre `main.py` en la raíz del repositorio (tiene menos de 10 líneas).

**✍️ ¿A qué función, de qué archivo, termina llamando `main.py`?** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

---

### CR3 · Cuenta cuántos métodos tiene cada archivo

**Comando(s) a usar** (repite cambiando el nombre del archivo: `hotel.py`, `app.py`, `reporte.py`):

```
Select-String -Path src\minihotel\hotel.py -Pattern "def " | Measure-Object   (PowerShell)
grep -c "def " src/minihotel/hotel.py                                          (Git Bash)
```

+--------------------------------------------------------------------------+
| 💻 PEGA AQUÍ EL COMANDO Y SU RESULTADO (CR3, los 3 archivos)              |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+

**✍️ ¿Cuántos métodos tiene `hotel.py` // `app.py` // `reporte.py`? ¿Cuál tiene más?** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

---

### CR4 · Ubica los comentarios que el propio código trae

El código marca sus propios defectos sembrados con la etiqueta `Defecto sembrado` o `BUG`, para que se puedan encontrar rápido.

**Comando(s) a usar:**

```
Select-String -Path src\minihotel\*.py -Pattern "Defecto sembrado|BUG"   (PowerShell)
grep -rn "Defecto sembrado\|BUG" src/minihotel/*.py                       (Git Bash)
```

+--------------------------------------------------------------------------+
| 💻 PEGA AQUÍ EL COMANDO Y SU RESULTADO (CR4)                              |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+

**✍️ Copia UN comentario "Defecto sembrado" o "BUG" que hayas visto (no hace falta entenderlo todavía, solo ubicarlo).** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

---

## Sección 2 · Arranque del sistema

**▶️ Haz esto:**

1. Abre una terminal en la carpeta del repositorio.
2. Ejecuta `.\scripts\run.ps1` (Windows) o `bash scripts/run.sh` (Linux/Mac/Git Bash).
3. Espera a que aparezca la ventana **MiniHotel v0.1 (escritorio)**.

**❓ Marca con una X:**

☐ Arrancó sin errores

☐ Se abrió la ventana con la botonera `1) …` a `0) Salir`

☐ El panel dice `=== MiniHotel v0.1 ===` y `Cargadas 5 habitaciones | Caja S/. 0.00`

☐ Se creó el archivo `datos/reservas.txt`

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE EL ARRANQUE                                    |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


---

## Sección 3 · Pruebas y hallazgos

Haz los bloques **en orden**. Al final debes tener **al menos 8** bloques con "SÍ" en "¿Hay defecto?" y todos sus campos llenos.

---


### P1 · Formato del catálogo de habitaciones

**Característica ISO/IEC 25010:** Usabilidad  ·  **Subcaracterística:** reconocibilidad

**📘 Por qué se revisa (esto es lo que aprendes):** la *reconocibilidad* mide si el usuario entiende la información de un vistazo. Un catálogo desalineado o con la moneda escrita distinto en cada pantalla obliga a esfuerzo extra y provoca errores de lectura de precios.

**▶️ Haz esto, exactamente:**

1. Clic en el botón `1) Ver habitaciones`.
2. Observa las columnas COD / TIPO / PRECIO/NOCHE / ESTADO.

**✅ Si estuviera BIEN, verías:** columnas alineadas, precios con 2 decimales (`80.00`) y el mismo símbolo de moneda en todas las pantallas.

**✍️ ¿Cómo se ve realmente? (¿alineado?, ¿decimales?, ¿moneda?)** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P1                                             |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Menor** — molesta al leer pero no impide reservar.*


---

### P2 · Cálculo del descuento por porcentaje

**Característica ISO/IEC 25010:** Adecuación funcional  ·  **Subcaracterística:** corrección

**📘 Por qué se revisa (esto es lo que aprendes):** la *corrección* exige que los cálculos den el resultado exacto. Un descuento del 10 % debe **multiplicar** el precio por 0.90, no restarle 10. Si está mal, todas las tarifas rebajadas salen mal.

**▶️ Haz esto, exactamente:**

1. Clic en `3) Aplicar descuento (consulta)`.
2. En «Codigo de habitacion» escribe: `H101`
3. En «% de descuento» escribe: `10`
4. Acepta.

**✅ Si estuviera BIEN, verías:** `Precio con descuento: S/. 72.00`  (10 % de 80.00 = 8.00; 80.00 − 8.00 = 72.00).

**✍️ ¿Qué texto exacto mostró la app?** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P2                                             |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Crítica** — la tarifa cobrada puede salir mal en cada reserva con descuento; el hotel pierde o gana dinero indebido.*


---

### P3 · Cobro de una reserva con descuento

**Característica ISO/IEC 25010:** Adecuación funcional  ·  **Subcaracterística:** corrección

**📘 Por qué se revisa (esto es lo que aprendes):** el mismo cálculo del descuento se usa al **reservar**. Aquí compruebas si el error de P2 también afecta el dinero que entra a caja.

**▶️ Haz esto, exactamente:**

1. Clic en `2) Reservar`.
2. «Codigo»: `H101`  ·  «Cantidad de noches»: `2`  ·  «% de descuento»: `10`
3. Acepta y lee la línea `Reserva OK. …`.

**✅ Si estuviera BIEN, verías:** un total de `S/. 144.00`  (2 × 72.00).

**✍️ ¿Qué monto cobró? (copia la línea `Reserva OK …` completa)** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P3                                             |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Crítica** — dinero mal calculado en la operación central del sistema.*


---

### P4 · "Ver caja" sin pedir clave

**Característica ISO/IEC 25010:** Seguridad  ·  **Subcaracterística:** control de acceso

**📘 Por qué se revisa (esto es lo que aprendes):** el *control de acceso* exige que las operaciones sensibles pidan autenticación. El total de caja es información del negocio: cualquiera que pase por la recepción no debería verlo.

**▶️ Haz esto, exactamente:** (hazlo justo después de P3, sin reservar nada más)

1. Clic en `5) Ver caja`.
2. Observa si aparece un cuadro pidiendo contraseña **antes** de mostrar el total.

**✅ Si estuviera BIEN, verías:** un diálogo que pide la clave de administrador antes de mostrar nada.

**✍️ ¿Qué pasó? (¿pidió clave?, ¿mostró el total directo?)** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P4                                             |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Mayor** — expone información del negocio sin ninguna barrera.*


---

### P5 · El arqueo de caja no cuadra

**Característica ISO/IEC 25010:** Adecuación funcional  ·  **Subcaracterística:** corrección

**📘 Por qué se revisa (esto es lo que aprendes):** el total de caja debe ser exactamente la suma de lo cobrado a los huéspedes. Si no cuadra, no se puede confiar en el cierre del día.

**▶️ Haz esto, exactamente:**

1. Calcula a mano lo que te cobró la app en P3: **S/ 140.00** (el total que mostró "Reserva OK").
2. Anota el total que te mostró `5) Ver caja` en P4.
3. Compara los dos números.

**✅ Si estuviera BIEN, verías:** el total de "Ver caja" = **S/ 140.00** (lo mismo que te cobró en la reserva).

**✍️ Total que muestra "Ver caja"  //  Total que te cobró la reserva (P3)** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P5                                             |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Mayor** — el cierre de caja diario queda descuadrado.*


---

### P6 · Reservar una habitación que ya está ocupada (sobreventa)

**Característica ISO/IEC 25010:** Fiabilidad  ·  **Subcaracterística:** madurez

**📘 Por qué se revisa (esto es lo que aprendes):** la *madurez* mide si el sistema se protege de estados imposibles. Dos huéspedes distintos ocupando la misma habitación la misma noche no existe en la vida real: significa que dejó reservar algo que ya no estaba disponible.

**▶️ Haz esto, exactamente:**

1. Clic en `2) Reservar`  ·  «Codigo»: `H101` (la que reservaste en P3, ya está "Ocupada")  ·  «Cantidad de noches»: `1`  ·  «% de descuento»: *(vacío)*
2. Acepta.
3. Clic en `1) Ver habitaciones` y busca la fila de `H101`.

**✅ Si estuviera BIEN, verías:** un aviso tipo "habitación no disponible"; la reserva **no** se registra.

**✍️ ¿Qué pasó al reservar? ¿Cuántas veces aparece "reservada" H101 si repites la acción?** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P6                                             |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Mayor** — corrompe la disponibilidad real y puede llevar a que dos huéspedes lleguen a la misma habitación.*


---

### P7 · "Cancelar reserva" sin confirmación

**Característica ISO/IEC 25010:** Usabilidad  ·  **Subcaracterística:** protección ante errores

**📘 Por qué se revisa (esto es lo que aprendes):** la *protección ante errores* exige confirmar las acciones destructivas. Cancelar sin preguntar hace fácil anular la reserva equivocada.

**▶️ Haz esto, exactamente:**

1. Clic en `4) Cancelar reserva`  ·  «Codigo a cancelar»: `H101`
2. Observa si aparece un "¿Está seguro?" **antes** de ejecutar.

**✅ Si estuviera BIEN, verías:** un diálogo de confirmación Sí / No.

**✍️ ¿Qué pasó? (¿preguntó algo o canceló directo?)** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P7                                             |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Menor** — hay riesgo, pero el daño es acotado y recuperable.*


---

### P8 · "Cancelar reserva" no libera la habitación

**Característica ISO/IEC 25010:** Adecuación funcional  ·  **Subcaracterística:** corrección

**📘 Por qué se revisa (esto es lo que aprendes):** si un botón se llama "Cancelar", debe liberar la habitación. Dejarla en estado "Ocupada" confunde a recepción y ensucia los reportes de disponibilidad.

**▶️ Haz esto, exactamente:**

1. Justo después de P7, clic en `1) Ver habitaciones`.
2. Busca `H101` en la lista.

**✅ Si estuviera BIEN, verías:** `H101` en estado **"Libre"**.

**✍️ ¿En qué estado quedó `H101`?** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P8                                             |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Mayor** — el botón no hace lo que dice; la disponibilidad queda inconsistente.*


---

### P9 · "Cancelar reserva" sin clave

**Característica ISO/IEC 25010:** Seguridad  ·  **Subcaracterística:** control de acceso

**📘 Por qué se revisa (esto es lo que aprendes):** cancelar una reserva es una operación sensible: debería exigir clave de administrador.

**▶️ Haz esto, exactamente:**

1. Recuerda P7: ¿te pidió contraseña en algún momento antes de cancelar?

**✅ Si estuviera BIEN, verías:** un diálogo pidiendo la clave de administrador antes de permitir la cancelación.

**✍️ ¿Pidió clave o no?** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P9                                             |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Mayor** — cualquiera puede alterar la disponibilidad del hotel.*


---

### P10 · El reporte "habitación más reservada" congela la app

**Característica ISO/IEC 25010:** Eficiencia de desempeño  ·  **Subcaracterística:** comportamiento temporal

**📘 Por qué se revisa (esto es lo que aprendes):** el *comportamiento temporal* mide tiempos de respuesta. Si una consulta bloquea toda la ventana, recepción no puede atender mientras tanto.

**▶️ Haz esto, exactamente:**

1. Clic en `6) Reporte: habitacion mas reservada`.
2. Mientras "calcula", intenta mover la ventana o pulsar otro botón.
3. Cuenta aproximadamente los segundos hasta que responde.

**✅ Si estuviera BIEN, verías:** respuesta casi inmediata y la ventana sigue reaccionando.

**✍️ Tiempo aprox. (s)  //  ¿respondía la ventana?  //  resultado devuelto** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P10                                            |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Mayor** — bloquea la recepción; con más habitaciones, empeora.*


---

### P11 · La exportación usa una ruta fija de Windows

**Característica ISO/IEC 25010:** Portabilidad  ·  **Subcaracterística:** adaptabilidad

**📘 Por qué se revisa (esto es lo que aprendes):** la *adaptabilidad* mide si el sistema funciona en distintos entornos. Escribir siempre en `C:\temp\` falla en Linux/Mac y en cualquier PC sin esa carpeta o sin permisos.

**▶️ Haz esto, exactamente:**

1. Clic en `7) Exportar CSV`.
2. Lee la línea del panel: anota la **ruta exacta** a la que dice que exportó.

**✅ Si estuviera BIEN, verías:** un diálogo "Guardar como…" que te deja elegir la carpeta.

**✍️ ¿Qué ruta exacta mostró?** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P11                                            |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Mayor** — en un entorno sin `C:\temp` la función simplemente no sirve.*


---

### P12 · El CSV exportado abre mal en Excel

**Característica ISO/IEC 25010:** Compatibilidad  ·  **Subcaracterística:** interoperabilidad

**📘 Por qué se revisa (esto es lo que aprendes):** un CSV existe para que **otro** programa lo lea. Si la cabecera usa `,` y las filas usan `;`, Excel no lo separa en columnas.

**▶️ Haz esto, exactamente:**

1. Mira el archivo con el comando de abajo.
2. Compara el separador de la **cabecera** (1.ª línea) con el de las **filas**.
3. Ábrelo también en Excel o LibreOffice Calc.

**✅ Si estuviera BIEN, verías:** un único separador en todo el archivo y columnas limpias en Excel.

**Comando(s) a usar** (cópialos en la terminal, en la raíz del repo):

```
type C:\temp\reservas.csv        (PowerShell)
cat  /c/temp/reservas.csv        (Git Bash)
```

+--------------------------------------------------------------------------+
| 💻 PEGA AQUÍ EL COMANDO Y SU RESULTADO (P12)                              |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**✍️ Separador de la cabecera  //  separador de las filas  //  ¿abrió en columnas en Excel?** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P12                                            |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Mayor** — el archivo de intercambio no es utilizable sin arreglarlo a mano.*


---

### P13 · Moneda y fecha fijas al idioma del sistema

**Característica ISO/IEC 25010:** Portabilidad  ·  **Subcaracterística:** adaptabilidad

**📘 Por qué se revisa (esto es lo que aprendes):** si el símbolo de moneda y el formato de fecha están "quemados" en el código, el sistema no se puede usar en otra región sin tocar el programa.

**▶️ Haz esto, exactamente:**

1. Mira el símbolo de moneda en `1) Ver habitaciones` y en una reserva (¿siempre igual, `S/` o `S/. `?).
2. Mira el formato de fecha en el CSV exportado (última línea, `Generado;…`).

**✅ Si estuviera BIEN, verías:** moneda y fecha configurables, o al menos tomadas de la configuración regional, y **consistentes** entre pantallas.

**✍️ Símbolo(s) de moneda que aparecen  //  formato de fecha del CSV** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P13                                            |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Menor** — limita el reúso, pero no bloquea la operación local.*


---

### P14 · Persistencia de los datos  (ESTE DEBE FUNCIONAR)

**Característica ISO/IEC 25010:** Fiabilidad  ·  **Subcaracterística:** recuperabilidad

**📘 Por qué se revisa (esto es lo que aprendes):** la *recuperabilidad* mide si el sistema conserva la información tras cerrarse. Aquí compruebas que MiniHotel **sí** guarda.

**▶️ Haz esto, exactamente:**

1. Clic en `8) Guardar`.
2. Cierra la ventana por completo.
3. Vuelve a levantar la app (`.\scripts\run.ps1`).
4. Clic en `5) Ver caja` y `1) Ver habitaciones`: ¿siguen tu caja y los estados de habitación como los dejaste?

**✅ Si estuviera BIEN, verías:** la caja y los estados de habitación **conservan** los valores de antes de cerrar.

**Comando(s) a usar** (cópialos en la terminal, en la raíz del repo):

```
type datos\reservas.txt        (PowerShell)
cat  datos/reservas.txt        (Git Bash)
```

+--------------------------------------------------------------------------+
| 💻 PEGA AQUÍ EL COMANDO Y SU RESULTADO (P14)                              |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**✍️ Caja al reabrir  //  estado de `H101` al reabrir  //  ¿se conservó todo?** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Funciona bien? (si SÍ, es CONFORME y NO es hallazgo)** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P14                                            |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **—** — si marcaste "NO", clasifícalo como recuperabilidad y elige la severidad.*


---

### P15 · Un dato no numérico rompe la operación

**Característica ISO/IEC 25010:** Fiabilidad  ·  **Subcaracterística:** tolerancia a fallos

**📘 Por qué se revisa (esto es lo que aprendes):** teclear una letra por error es de lo más común. El sistema debería avisar "eso no es un número", no fallar por dentro sin decir nada.

**▶️ Haz esto, exactamente:**

1. Asegúrate de haber arrancado la app **desde la terminal** (para ver la consola).
2. Clic en `2) Reservar`  ·  «Codigo»: `H102`  ·  «Cantidad de noches»: escribe una letra: `x`
3. Acepta. Mira **la ventana** y luego **la consola** (la terminal).

**✅ Si estuviera BIEN, verías:** un mensaje tipo "La cantidad de noches debe ser un número entero" y la app estable, sin nada raro en la consola.

**Comando(s) a usar** (cópialos en la terminal, en la raíz del repo):

```
(no hay comando: copia a mano las primeras líneas del error que aparece en la consola)
```

+--------------------------------------------------------------------------+
| 💻 PEGA AQUÍ EL COMANDO Y SU RESULTADO (P15)                              |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**✍️ Qué mostró la ventana  //  primera línea del error en la consola** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P15                                            |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Mayor** — un error de tecleo normal deja la operación a medias sin avisar al usuario.*


---

### P16 · Acepta descuentos / precios negativos

**Característica ISO/IEC 25010:** Seguridad  ·  **Subcaracterística:** integridad

**📘 Por qué se revisa (esto es lo que aprendes):** la *integridad* exige rechazar datos que dejan el sistema en un estado inválido. Un descuento mayor que el precio (o negativo) produce importes negativos.

**▶️ Haz esto, exactamente:**

1. Clic en `3) Aplicar descuento (consulta)`  ·  «Codigo»: `H101`  ·  «% de descuento»: `150`
2. Acepta y observa el resultado.

**✅ Si estuviera BIEN, verías:** un rechazo o un aviso; nunca un precio negativo.

**✍️ ¿Qué valor devolvió?** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P16                                            |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Mayor** — permite estados de datos imposibles (importe < 0).*


---

### P17 · La clave de administrador está escrita en el código

**Característica ISO/IEC 25010:** Seguridad  ·  **Subcaracterística:** confidencialidad

**📘 Por qué se revisa (esto es lo que aprendes):** nunca se guardan contraseñas en texto plano, y menos en el código fuente: cualquiera con acceso al repositorio la ve, y no se puede cambiar sin volver a distribuir el programa. Peor aún si, como viste en P4 y P9, **nunca se usa**.

**▶️ Haz esto, exactamente:**

1. Ejecuta en la terminal **uno** de los comandos de abajo.
2. Mira si aparece una contraseña literal.

**✅ Si estuviera BIEN, verías:** ninguna contraseña en el código (estaría cifrada o fuera del repositorio).

**Comando(s) a usar** (cópialos en la terminal, en la raíz del repo):

```
Select-String -Path src\minihotel\*.py -Pattern "hotel123|ADMIN_PASS"   (PowerShell)
grep -rn -E "hotel123|ADMIN_PASS" src/minihotel/                        (Git Bash)
```

+--------------------------------------------------------------------------+
| 💻 PEGA AQUÍ EL COMANDO Y SU RESULTADO (P17)                              |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**✍️ Archivo y línea donde aparece  //  clave encontrada** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P17                                            |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Crítica** — credencial expuesta en texto plano; no rotable sin volver a distribuir el programa.*


---

### P18 · Toda la interfaz y el flujo en un solo archivo (God class)

**Característica ISO/IEC 25010:** Mantenibilidad  ·  **Subcaracterística:** modularidad

**📘 Por qué se revisa (esto es lo que aprendes):** la *modularidad* mide si las responsabilidades están separadas. Cuando la ventana, el flujo de cada botón y las llamadas de negocio viven en un solo archivo enorme, cualquier cambio es arriesgado y difícil de probar.

**▶️ Haz esto, exactamente:**

1. Cuenta las líneas y los métodos `on_...` de `app.py` con los comandos de abajo.

**✅ Si estuviera BIEN, verías:** la interfaz separada del flujo de negocio, en clases o módulos distintos y más pequeños.

**Comando(s) a usar** (cópialos en la terminal, en la raíz del repo):

```
(Get-Content src\minihotel\app.py).Count                                    (PowerShell)
Select-String src\minihotel\app.py -Pattern "def on_" | Measure-Object        (PowerShell)
wc -l src/minihotel/app.py ; grep -c "def on_" src/minihotel/app.py           (Git Bash)
```

+--------------------------------------------------------------------------+
| 💻 PEGA AQUÍ EL COMANDO Y SU RESULTADO (P18)                              |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**✍️ Líneas de `app.py`  //  número de métodos `on_...` que manejan UI + flujo juntos** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P18                                            |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Mayor** — dificulta todo cambio futuro y las pruebas.*


---

### P19 · La misma búsqueda de habitación está copiada varias veces

**Característica ISO/IEC 25010:** Mantenibilidad  ·  **Subcaracterística:** modificabilidad

**📘 Por qué se revisa (esto es lo que aprendes):** la *modificabilidad* baja cuando el mismo código está duplicado: si hay que corregir la búsqueda, hay que acordarse de arreglarla en todos los sitios.

**▶️ Haz esto, exactamente:**

1. Ejecuta **uno** de los comandos de abajo.
2. Cuenta cuántas veces aparece el mismo bucle `for hab in self.habitaciones:`.

**✅ Si estuviera BIEN, verías:** una sola función de búsqueda reutilizada por todos los métodos.

**Comando(s) a usar** (cópialos en la terminal, en la raíz del repo):

```
Select-String -Path src\minihotel\hotel.py -Pattern "for hab in self.habitaciones"   (PowerShell)
grep -n "for hab in self.habitaciones" src/minihotel/hotel.py                        (Git Bash)
```

+--------------------------------------------------------------------------+
| 💻 PEGA AQUÍ EL COMANDO Y SU RESULTADO (P19)                              |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**✍️ Número de veces que se repite  //  en qué métodos** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P19                                            |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Mayor** — un mismo defecto habría que corregirlo en varios lugares a la vez.*


---

### P20 · Mensajes de error en clave

**Característica ISO/IEC 25010:** Usabilidad  ·  **Subcaracterística:** operabilidad

**📘 Por qué se revisa (esto es lo que aprendes):** la *operabilidad* exige que los mensajes digan qué pasó y qué hacer. Códigos como `E01` no significan nada para quien atiende recepción.

**▶️ Haz esto, exactamente:**

1. Clic en `2) Reservar`  ·  «Codigo»: `ZZZZ` (no existe)  ·  «Cantidad de noches»: `1`  ·  descuento vacío.
2. Anota el mensaje que aparece.

**✅ Si estuviera BIEN, verías:** "No existe una habitación con el código ZZZZ".

**✍️ Mensajes / códigos exactos que viste (`E01`, …)** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**❓ ¿Hay defecto?** (marca una con una X):  ☐ SÍ   ☐ NO

+--------------------------------------------------------------------------+
| 📸 PEGA AQUÍ LA CAPTURA DE P20                                            |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+


**🏷️ Severidad** (marca una con una X):  ☐ Crítica  ☐ Mayor  ☐ Menor  ☐ Observación

*Sugerida: **Mayor** — el usuario no sabe qué salió mal ni cómo seguir.*


---

## Sección 4 · Verificación en el código (obligatorio) — confirma tus hallazgos

Hasta aquí diagnosticaste **usando la ventana** (calidad externa). Estos 8 bloques cierran el círculo: vas al **código fuente** (el mismo que ya recorriste en la Sección 1) y confirmas que la causa de lo que viste está realmente ahí (calidad interna). No corrijas nada, solo cita la línea.

En cada bloque de abajo se te dice **exactamente qué archivo abrir y qué palabra buscar**. Usa la guía de búsqueda de la Sección 1 (Ctrl+F en el editor, o el número de línea que ya imprime el comando de terminal). No necesitas releer el archivo completo: busca solo esa palabra y mira las 3-4 líneas alrededor.

---

### PB1 · Por qué falla el descuento (causa de P2/P3)

**▶️ Haz esto:** abre `src/minihotel/hotel.py` y busca el método `_precio_con_descuento`.

**Comando(s) a usar:**

```
Select-String -Path src\minihotel\hotel.py -Pattern "def _precio_con_descuento" -Context 0,4   (PowerShell)
grep -n -A4 "def _precio_con_descuento" src/minihotel/hotel.py                                  (Git Bash)
```

+--------------------------------------------------------------------------+
| 💻 PEGA AQUÍ EL COMANDO Y SU RESULTADO (PB1)                              |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+

**🔎 ¿Qué está mal? (explícalo en tus palabras, 1 línea)**

[__________________________________________________________________]{.mark}

**📍 Ubicación exacta del error — archivo : línea (usa el número que te dio el comando)**

[__________________________________________________________________]{.mark}

**✍️ ¿Qué operación usa (resta o multiplicación)? Copia la línea exacta.** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

---

### PB2 · Por qué permite la sobreventa (causa de P6)

**▶️ Haz esto:** abre `src/minihotel/hotel.py`, método `reservar()`. Busca si existe alguna línea que compruebe `h.estado` (por ejemplo `if h.estado == "Ocupada"`) **antes** de marcar la habitación como ocupada.

**Comando(s) a usar:**

```
Select-String -Path src\minihotel\hotel.py -Pattern "estado ==" | Measure-Object   (PowerShell)
grep -c "estado ==" src/minihotel/hotel.py                                          (Git Bash)
```

+--------------------------------------------------------------------------+
| 💻 PEGA AQUÍ EL COMANDO Y SU RESULTADO (PB2)                              |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+

**🔎 ¿Qué está mal? (explícalo en tus palabras, 1 línea)**

[__________________________________________________________________]{.mark}

**📍 Ubicación exacta del error — archivo : línea (usa el número que te dio el comando)**

[__________________________________________________________________]{.mark}

**✍️ ¿Cuántas veces se valida `estado` antes de reservar? (si sale 0, esa es la causa de la sobreventa)** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

---

### PB3 · Por qué "cancelar" no libera la habitación (causa de P8)

**▶️ Haz esto:** abre `src/minihotel/hotel.py` y busca la palabra `def cancelar`. Lee las 12 líneas de ese método completo (es corto).

**Comando(s) a usar:**

```
Select-String -Path src\minihotel\hotel.py -Pattern "def cancelar" -Context 0,11   (PowerShell)
grep -n -A11 "def cancelar" src/minihotel/hotel.py                                  (Git Bash)
```

+--------------------------------------------------------------------------+
| 💻 PEGA AQUÍ EL COMANDO Y SU RESULTADO (PB3)                              |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+

**🔎 ¿Qué está mal? (explícalo en tus palabras, 1 línea)**

[__________________________________________________________________]{.mark}

**📍 Ubicación exacta del error — archivo : línea (usa el número que te dio el comando)**

[__________________________________________________________________]{.mark}

**✍️ Dentro de ese método, ¿hay alguna línea que ponga `h.estado = "Libre"`? (sí / no)** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

---

### PB4 · Por qué el arqueo de caja no cuadra (causa de P5)

**▶️ Haz esto:** abre `src/minihotel/hotel.py` y busca la palabra `self.caja`. Fíjate en qué variable usa esa línea: `h.precio_noche` (precio de lista) o la variable con descuento ya calculada un poco más arriba.

**Comando(s) a usar:**

```
Select-String -Path src\minihotel\hotel.py -Pattern "self.caja \+="   (PowerShell)
grep -n "self.caja +=" src/minihotel/hotel.py                          (Git Bash)
```

+--------------------------------------------------------------------------+
| 💻 PEGA AQUÍ EL COMANDO Y SU RESULTADO (PB4)                              |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+

**🔎 ¿Qué está mal? (explícalo en tus palabras, 1 línea)**

[__________________________________________________________________]{.mark}

**📍 Ubicación exacta del error — archivo : línea (usa el número que te dio el comando)**

[__________________________________________________________________]{.mark}

**✍️ Copia la línea exacta. ¿Usa el precio CON o SIN descuento?** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

---

### PB5 · Por qué la exportación falla fuera de Windows (causa de P11)

**▶️ Haz esto:** abre `src/minihotel/reporte.py` y busca la palabra `ruta = `.

**Comando(s) a usar:**

```
Select-String -Path src\minihotel\reporte.py -Pattern "ruta = "   (PowerShell)
grep -n "ruta = " src/minihotel/reporte.py                         (Git Bash)
```

+--------------------------------------------------------------------------+
| 💻 PEGA AQUÍ EL COMANDO Y SU RESULTADO (PB5)                              |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+

**🔎 ¿Qué está mal? (explícalo en tus palabras, 1 línea)**

[__________________________________________________________________]{.mark}

**📍 Ubicación exacta del error — archivo : línea (usa el número que te dio el comando)**

[__________________________________________________________________]{.mark}

**✍️ Copia la ruta exacta que encontraste escrita en el código.** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

---

### PB6 · Por qué el reporte se congela (causa de P10)

**▶️ Haz esto:** abre `src/minihotel/reporte.py` y busca la palabra `sleep`.

**Comando(s) a usar:**

```
Select-String -Path src\minihotel\reporte.py -Pattern "sleep"   (PowerShell)
grep -n "sleep" src/minihotel/reporte.py                          (Git Bash)
```

+--------------------------------------------------------------------------+
| 💻 PEGA AQUÍ EL COMANDO Y SU RESULTADO (PB6)                              |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+

**🔎 ¿Qué está mal? (explícalo en tus palabras, 1 línea)**

[__________________________________________________________________]{.mark}

**📍 Ubicación exacta del error — archivo : línea (usa el número que te dio el comando)**

[__________________________________________________________________]{.mark}

**✍️ ¿Cuántos segundos espera esa línea a propósito?** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

---

### PB7 · Por qué la moneda se ve distinta según la pantalla (causa de P1/P13)

**▶️ Haz esto:** busca la palabra `S/` en **todos** los archivos de `src/minihotel/` y compara cómo está escrita en cada resultado (¿siempre igual, o unas veces con punto y otras sin punto?).

**Comando(s) a usar:**

```
Select-String -Path src\minihotel\*.py -Pattern "S/"   (PowerShell)
grep -rn "S/" src/minihotel/*.py                         (Git Bash)
```

+--------------------------------------------------------------------------+
| 💻 PEGA AQUÍ EL COMANDO Y SU RESULTADO (PB7)                              |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+

**🔎 ¿Qué está mal? (explícalo en tus palabras, 1 línea)**

[__________________________________________________________________]{.mark}

**📍 Ubicaciones exactas — archivo : línea de CADA forma distinta que encontraste**

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

**✍️ ¿Cuántas formas distintas de escribir la moneda encontraste, y en qué archivos?** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

---

### PB8 · Cuántos defectos están marcados en el código (cierre)

Todos los defectos sembrados están comentados en el código con la etiqueta `Defecto sembrado` o `BUG`, para que el docente los ubique rápido.

**Comando(s) a usar:**

```
Select-String -Path src\minihotel\*.py -Pattern "Defecto sembrado|BUG" | Measure-Object   (PowerShell)
grep -rc "Defecto sembrado\|BUG" src/minihotel/ | awk -F: '{s+=$2} END{print s}'           (Git Bash)
```

+--------------------------------------------------------------------------+
| 💻 PEGA AQUÍ EL COMANDO Y SU RESULTADO (PB8)                              |
+==========================================================================+
| \                                                                        |
| \                                                                        |
| \                                                                        |
| \                                                                        |
+--------------------------------------------------------------------------+

**✍️ ¿Cuántos defectos cuenta el código mismo? ¿Coincide con lo que tú encontraste usando la ventana?** *(escribe sobre las líneas amarillas)*

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

---

## Sección 5 · Resumen por característica

Cuenta tus bloques con "SÍ" en "¿Hay defecto?".  **C** = 0 hallazgos · **O** = solo Menores/Obs. · **NC** = al menos 1 Mayor o Crítica · **NE** = no se pudo probar.
Escribe los valores sobre las líneas amarillas, en el mismo orden de las filas.

| # | Característica | Bloques |
|---|---|---|
| 1 | Adecuación funcional | P2, P3, P5, P8 |
| 2 | Eficiencia de desempeño | P10 |
| 3 | Compatibilidad | P12 |
| 4 | Usabilidad | P1, P7, P20 |
| 5 | Fiabilidad | P6, P15  (P14 = conforme, no suma) |
| 6 | Seguridad | P4, P9, P16, P17 |
| 7 | Mantenibilidad | P18, P19 |
| 8 | Portabilidad | P11, P13 |

**✍️ Para cada fila 1–8 — Nº de hallazgos // severidad más alta // C / O / NC / NE // comentario de 1 línea:**


[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}


---

## Sección 6 · Línea base consolidada

**✍️ Total de hallazgos** (bloques con "SÍ"): [______]{.mark}

**✍️ Por severidad — Críticos // Mayores // Menores // Observaciones:**

[__________________________________________________]{.mark}

**✍️ Característica más comprometida y por qué (usa números, no adjetivos):**

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

---

## Sección 7 · Aspectos que NO se pudieron evaluar hoy

*(llénalo solo si algún bloque no lo pudiste hacer)*

**✍️ Característica // por qué no se pudo // qué haría falta:**

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

---

## Sección 8 · Dictamen de línea base

**✍️ Características No conformes: ____ de 8   //   No evaluadas: ____ de 8   //   Característica más débil:**

[__________________________________________________________________]{.mark}

**✍️ Enunciado de la línea base** (2–3 líneas; describe el estado, con el commit; **sin** proponer soluciones ni opiniones):

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

[__________________________________________________________________]{.mark}

---

## Sección 9 · Antes de entregar (marca todo con una X)

☐ Sección 0 completa (commit, SO, Python).

☐ Sección 1 (primer vistazo al código) con los 4 bloques CR1–CR4 completos.

☐ Sección 2 (arranque) con sus casillas y la captura pegada.

☐ Todos los bloques P1–P20 con: pregunta marcada + líneas amarillas escritas + captura pegada (y comando pegado donde se pide).

☐ Al menos **8** bloques con "SÍ" en "¿Hay defecto?".

☐ Al menos **6 de 8** características con algún hallazgo.

☐ Sección 4 (verificación en el código) con los 8 bloques PB1–PB8 completos.

☐ Sección 5 (resumen) completa.

☐ Sección 6 con el total y la característica más comprometida justificada.

☐ Sección 8 con el enunciado objetivo, sin soluciones.

---

## Sección 10 · Firmas

<br><br>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_              \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Responsable del reporte (célula)              Docente
