# Taller 01 (variante Python) — Auditoría de Línea Base (ISO/IEC 25010)

**Unidad Didáctica:** Gestión de la Calidad del Software · **Semana 1**
**Programa:** Desarrollo de Sistemas de Información — IESTP Sarasara
**Docente:** Ing. Pedro Jesús Guzmán Ramos
**Lenguaje:** Python 3 + Tkinter (aplicación de **escritorio**, sin frameworks ni build tools)

Sistema de ejemplo: **MiniHotel**, un sistema de reservas de un hotel pequeño
(ventana Tkinter) con **base de datos interna** en un archivo local
(`datos/reservas.txt`). El sistema **funciona**, pero arrastra **defectos de
calidad sembrados a propósito** que tocan varias características de la
**ISO/IEC 25010** — los mismos tipos de defecto que el Taller 01 original
(MiniPOS en Java), pero en otro lenguaje y otro dominio, para practicar el
mismo diagnóstico con un sistema distinto.

Tu trabajo en esta sesión **no es corregir nada**, sino:

1. **Levantar** (instalar y ejecutar) el sistema.
2. **Usarlo** siguiendo un guion de exploración.
3. **Diagnosticar** su calidad con la **ficha de diagnóstico ISO/IEC 25010** y
   dejar registrada la **línea base**: qué encontraste, con qué evidencia y en
   qué característica lo clasificas.

> **Línea base** = la "foto" del estado de calidad del sistema **hoy**, antes
> de intervenirlo. Todas las mejoras de las siguientes semanas se miden contra
> esta foto.

---

## 1. Requisitos

- **Python 3.10 o superior**, con Tkinter incluido (viene por defecto en la
  instalación oficial de Python en Windows/Mac; en Linux puede requerir el
  paquete `python3-tk`). Comprueba:
  ```bash
  python --version
  python -c "import tkinter; print('tkinter ok')"
  ```
- Git (para clonar el repositorio).
- No se necesita `pip install` de nada: toda la interfaz usa la librería
  estándar de Python.

---

## 2. Levantar el sistema (paso a paso)

### 2.1. Clonar y entrar

```bash
git clone <URL-del-repositorio> taller-01-linea-base-minihotel
cd taller-01-linea-base-minihotel
```

### 2.2. Ejecutar

**Windows (PowerShell):**
```powershell
.\scripts\run.ps1
```

**Linux / macOS / Git Bash:**
```bash
bash scripts/run.sh
```

**Manual (cualquier sistema):**
```bash
python main.py
```

Si aparece la ventana **MiniHotel v0.1 (escritorio)** con la botonera (`1) Ver
habitaciones` … `0) Salir`) y un panel de salida, **el sistema ya está
levantado**. Toma una captura → es tu primera evidencia (E1).

> Necesitas un entorno gráfico (no funciona por SSH sin X). La primera vez se
> crea `datos/reservas.txt` con el catálogo demo; a partir de ahí ese archivo
> es la "base de datos" del sistema.

---

## 3. Guion de exploración (haz esto y anota TODO lo que observes)

Ejecuta el sistema y prueba, en orden (cada paso es un **botón** de la ventana):

| # | Acción | Fíjate en… |
|---|---|---|
| 1 | Botón **1) Ver habitaciones** | ¿Se entiende el formato? ¿Alineación, moneda? |
| 2 | Botón **3) Aplicar descuento (consulta)**, código `H101`, descuento `10` | ¿El "precio con descuento" tiene sentido? |
| 3 | Botón **2) Reservar**: `H101`, noches `2`, descuento `10` | ¿Cuánto cobró? ¿Coincide con el 10 %? |
| 4 | Botón **2) Reservar**: `H101` otra vez (la misma habitación) | ¿Deja reservar una habitación ya ocupada? |
| 5 | Botón **5) Ver caja** | ¿Te pidió clave? ¿El total cuadra con tus reservas? |
| 6 | Botón **4) Cancelar reserva**: `H101`; luego botón **1) Ver habitaciones** | ¿Realmente quedó "Libre"? ¿Pidió confirmación? |
| 7 | Botón **6) Reporte: habitacion mas reservada** | ¿Cuánto tardó? ¿Se congeló la ventana? ¿El resultado es creíble? |
| 8 | Botón **7) Exportar CSV** | ¿A dónde exportó? Abre el archivo en Excel: ¿se ve bien? |
| 9 | Botón **8) Guardar**; cierra la ventana; vuelve a levantar la app | ¿Se conservaron tus cambios? |
| 10 | Botón **2) Reservar**: en **Cantidad de noches** escribe una **letra** (ej. `x`) | ¿Qué pasa? ¿Mensaje claro o error sin control (mira la consola)? |

Cada cosa rara que veas es un **hallazgo**. Anótalo con: qué hiciste, qué
esperabas, qué pasó, y una captura.

---

## 4. La actividad y los instrumentos

| Documento | Para qué | Lo usa |
|---|---|---|
| [`docs/ACTIVIDAD_LINEA_BASE_MINIHOTEL.md`](docs/ACTIVIDAD_LINEA_BASE_MINIHOTEL.md) | Consigna completa, entregables, ISO/IEC 25010 resumida | Estudiante |
| [`docs/FICHA_DIAGNOSTICO_ISO25010_MINIHOTEL.docx`](docs/FICHA_DIAGNOSTICO_ISO25010_MINIHOTEL.docx) (fuente: [`.md`](docs/FICHA_DIAGNOSTICO_ISO25010_MINIHOTEL.md)) | **Ficha de diagnóstico** en formato checklist: guía paso a paso, casillas, líneas amarillas para escribir y recuadros para pegar la captura de cada bloque. Se llena entera dentro del Word. | Estudiante |
| [`docs/LISTA_COTEJO_MINIHOTEL.md`](docs/LISTA_COTEJO_MINIHOTEL.md) | **Instrumento de evaluación** (lista de cotejo) de la sesión | Docente |

---

## 5. Estructura del repositorio

```
taller-01-linea-base-minihotel/
├── src/minihotel/
│   ├── app.py         # Ventana Tkinter: UI + flujo (God class a propósito)
│   ├── hotel.py        # Lógica de negocio + persistencia (bug de descuento, "cancelar" que no libera, sobreventa)
│   ├── habitacion.py    # Clase Habitacion
│   └── reporte.py      # Reporte O(n^2) + pausa; export CSV no portable/incompatible
├── main.py            # Punto de entrada (usado por los scripts)
├── scripts/           # run.ps1 / run.sh  (ejecutan main.py)
├── datos/             # "base de datos" local: reservas.txt (generado; git-ignored)
├── docs/              # actividad + ficha ISO 25010 (.md y .docx) + lista de cotejo
└── README.md
```

> **Nota:** los defectos son intencionales y están comentados en el código
> para el docente. Los estudiantes deben encontrarlos **usando** el sistema,
> no leyendo el código (el análisis de código llega en semanas posteriores).
