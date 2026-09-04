import tkinter as tk
from tkinter import simpledialog, messagebox

from .hotel import Hotel
from . import reporte


class MiniHotelApp:
    # Defecto sembrado (Mantenibilidad / modularidad): esta clase mezcla
    # interfaz, flujo y llamadas de negocio en un solo archivo (God class),
    # igual que MiniPOSApp en el Taller 01.

    def __init__(self, root):
        self.root = root
        self.hotel = Hotel()

        root.title("MiniHotel v0.1 (escritorio)")
        root.geometry("560x480")

        botonera = tk.Frame(root)
        botonera.pack(side=tk.LEFT, fill=tk.Y, padx=8, pady=8)

        botones = [
            ("1) Ver habitaciones", self.on_ver_habitaciones),
            ("2) Reservar", self.on_reservar),
            ("3) Aplicar descuento (consulta)", self.on_consultar_descuento),
            ("4) Cancelar reserva", self.on_cancelar),
            ("5) Ver caja", self.on_ver_caja),
            ("6) Reporte: habitacion mas reservada", self.on_reporte),
            ("7) Exportar CSV", self.on_exportar),
            ("8) Guardar", self.on_guardar),
            ("0) Salir", root.destroy),
        ]
        for texto, comando in botones:
            tk.Button(botonera, text=texto, width=30, anchor="w", command=comando).pack(pady=2)

        self.salida = tk.Text(root, width=48, height=28)
        self.salida.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=8, pady=8)

        self._escribir(
            "=== MiniHotel v0.1 ===\n"
            f"Cargadas {len(self.hotel.habitaciones)} habitaciones | Caja S/. {self.hotel.caja:.2f}\n"
        )

    def _escribir(self, texto):
        self.salida.insert(tk.END, texto + "\n")
        self.salida.see(tk.END)

    # ---------- handlers ----------

    def on_ver_habitaciones(self):
        self._escribir(self.hotel.listar_habitaciones())

    def on_reservar(self):
        codigo = simpledialog.askstring("Reservar", "Codigo de habitacion:")
        if codigo is None:
            return
        noches_txt = simpledialog.askstring("Reservar", "Cantidad de noches:")
        if noches_txt is None:
            return
        descuento_txt = simpledialog.askstring("Reservar", "% de descuento (puede ir vacio):")
        descuento = float(descuento_txt) if descuento_txt else 0.0

        # Sin try/except a proposito: si "noches" no es un numero, la
        # excepcion sube sin control (ver ficha de diagnostico).
        resultado = self.hotel.reservar(codigo, noches_txt, descuento)
        self._escribir(resultado)

    def on_consultar_descuento(self):
        codigo = simpledialog.askstring("Consultar descuento", "Codigo de habitacion:")
        if codigo is None:
            return
        descuento_txt = simpledialog.askstring("Consultar descuento", "% de descuento:")
        descuento = float(descuento_txt) if descuento_txt else 0.0
        self._escribir(self.hotel.consultar_descuento(codigo, descuento))

    def on_cancelar(self):
        # Defecto sembrado (Usabilidad / proteccion ante errores): no pide
        # confirmacion antes de una accion destructiva.
        # Defecto sembrado (Seguridad / control de acceso): no pide clave
        # de administrador pese a existir ADMIN_PASS en hotel.py.
        codigo = simpledialog.askstring("Cancelar reserva", "Codigo de habitacion a cancelar:")
        if codigo is None:
            return
        self._escribir(self.hotel.cancelar(codigo))

    def on_ver_caja(self):
        # Defecto sembrado (Seguridad / control de acceso): no pide clave
        # de administrador pese a existir ADMIN_PASS en hotel.py.
        self._escribir(f"Caja actual: S/. {self.hotel.ver_caja():.2f}")

    def on_reporte(self):
        self._escribir("Calculando reporte...")
        self.root.update()  # fuerza a pintar el mensaje antes de congelarse
        resultado = reporte.habitacion_mas_reservada(self.hotel.historial_reservas)
        self._escribir(resultado)

    def on_exportar(self):
        ruta = reporte.exportar_csv(self.hotel.habitaciones)
        self._escribir(f"Exportado a: {ruta}")

    def on_guardar(self):
        self.hotel.guardar()
        self._escribir("Datos guardados.")


def main():
    root = tk.Tk()
    MiniHotelApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
