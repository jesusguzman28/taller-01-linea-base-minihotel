import time
import datetime


def habitacion_mas_reservada(historial_reservas):
    # Defecto sembrado (Eficiencia de desempeño / comportamiento temporal):
    # busqueda O(n^2) + pausa artificial que congela la ventana (se llama
    # desde el hilo principal de Tkinter, sin hilo aparte).
    time.sleep(1.5)
    conteo = {}
    for codigo in historial_reservas:
        total = 0
        for otro in historial_reservas:
            if otro == codigo:
                total += 1
        conteo[codigo] = total
    if not conteo:
        return "Sin reservas registradas."
    codigo_top = max(conteo, key=conteo.get)
    return f"Habitacion mas reservada: {codigo_top} ({conteo[codigo_top]} reservas)"


def exportar_csv(habitaciones):
    # Defecto sembrado (Portabilidad / adaptabilidad): ruta fija de Windows,
    # falla en Linux/Mac o en cualquier PC sin esa carpeta.
    ruta = r"C:\temp\reservas.csv"
    import os
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    # Defecto sembrado (Compatibilidad / interoperabilidad): la cabecera usa
    # "," y las filas usan ";" -> Excel no separa las columnas correctamente.
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("codigo,tipo,precio_noche,estado\n")
        for h in habitaciones:
            f.write(f"{h.codigo};{h.tipo};{h.precio_noche};{h.estado}\n")
        # Defecto sembrado (Portabilidad / adaptabilidad): fecha fija al
        # formato del sistema, sin configuracion regional.
        f.write(f"Generado;{datetime.datetime.now()}\n")

    return ruta
