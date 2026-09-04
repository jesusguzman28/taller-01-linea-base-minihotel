import os
from .habitacion import Habitacion

# Clave de administrador "protegiendo" Ver caja y Cancelar reserva.
# Defecto sembrado: esta clave nunca se usa en ninguna pantalla (ver P4/P9 de la ficha).
ADMIN_PASS = "hotel123"

RUTA_DATOS = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "datos", "reservas.txt")


class Hotel:
    def __init__(self):
        self.habitaciones = []
        self.caja = 0.0
        self.historial_reservas = []  # lista de codigos reservados (para el reporte)
        self._cargar_o_sembrar()

    # ---------- persistencia ----------

    def _cargar_o_sembrar(self):
        if os.path.exists(RUTA_DATOS):
            self._cargar()
        else:
            self._sembrar_demo()
            self.guardar()

    def _sembrar_demo(self):
        self.habitaciones = [
            Habitacion("H101", "Simple", 80.0),
            Habitacion("H102", "Doble", 120.0),
            Habitacion("H103", "Suite", 200.0),
            Habitacion("H104", "Simple", 80.0),
            Habitacion("H105", "Doble", 120.0),
        ]
        self.caja = 0.0
        self.historial_reservas = []

    def _cargar(self):
        with open(RUTA_DATOS, "r", encoding="utf-8") as f:
            lineas = f.readlines()
        self.habitaciones = []
        self.historial_reservas = []
        self.caja = 0.0
        for linea in lineas:
            linea = linea.strip()
            if not linea:
                continue
            if linea.startswith("CAJA;"):
                self.caja = float(linea.split(";")[1])
            elif linea.startswith("RES;"):
                self.historial_reservas.append(linea.split(";")[1])
            else:
                self.habitaciones.append(Habitacion.from_linea(linea))

    def guardar(self):
        os.makedirs(os.path.dirname(RUTA_DATOS), exist_ok=True)
        with open(RUTA_DATOS, "w", encoding="utf-8") as f:
            f.write(f"CAJA;{self.caja}\n")
            for h in self.habitaciones:
                f.write(h.to_linea() + "\n")
            for codigo in self.historial_reservas:
                f.write(f"RES;{codigo}\n")

    # ---------- catalogo ----------

    def listar_habitaciones(self):
        # Defecto sembrado (Usabilidad / reconocibilidad): formato sin alinear
        # y simbolo de moneda inconsistente ("S/" aqui, "S/." en otras pantallas).
        lineas = ["COD   TIPO    PRECIO/NOCHE  ESTADO"]
        for h in self.habitaciones:
            lineas.append(f"{h.codigo} {h.tipo} S/{h.precio_noche} {h.estado}")
        return "\n".join(lineas)

    def _buscar(self, codigo):
        # Defecto sembrado (Mantenibilidad / modificabilidad): esta misma búsqueda
        # lineal por código está duplicada en reservar(), cancelar() y
        # consultar_descuento() en vez de reutilizar una sola función.
        for h in self.habitaciones:
            if h.codigo == codigo:
                return h
        return None

    # ---------- descuento (defecto de correccion, compartido por consulta y venta) ----------

    def _precio_con_descuento(self, precio, porcentaje_descuento):
        # BUG (Adecuacion funcional / correccion): un descuento del 10% debe
        # MULTIPLICAR el precio por 0.90; aqui se RESTA el numero del
        # porcentaje directamente en soles, como si fueran lo mismo.
        return precio - porcentaje_descuento

    def consultar_descuento(self, codigo, porcentaje_descuento):
        h = None
        for hab in self.habitaciones:  # búsqueda duplicada (ver _buscar)
            if hab.codigo == codigo:
                h = hab
                break
        if h is None:
            return "E01: habitacion no encontrada"
        precio = self._precio_con_descuento(h.precio_noche, porcentaje_descuento)
        # Defecto sembrado (Seguridad / integridad): no se rechazan descuentos
        # negativos ni mayores al precio; el precio final puede quedar negativo.
        return f"Precio con descuento: S/. {precio:.2f}"

    # ---------- reservar ----------

    def reservar(self, codigo, noches, porcentaje_descuento):
        h = None
        for hab in self.habitaciones:  # búsqueda duplicada (ver _buscar)
            if hab.codigo == codigo:
                h = hab
                break
        if h is None:
            return "E01: habitacion no encontrada"

        noches = int(noches)  # sin try/except a proposito (ver P.. tolerancia a fallos)

        # Defecto sembrado (Adecuacion funcional / Fiabilidad): no se valida si
        # la habitacion ya esta "Ocupada" -> permite doble reserva (sobreventa).
        precio_noche_con_descuento = self._precio_con_descuento(h.precio_noche, porcentaje_descuento)
        total = precio_noche_con_descuento * noches

        h.estado = "Ocupada"
        self.caja += h.precio_noche * noches  # BUG: a caja entra el precio SIN descuento,
        # aunque al cliente se le informo un total CON descuento -> el arqueo no cuadra.
        self.historial_reservas.append(codigo)

        return f"Reserva OK. Habitacion {codigo}, {noches} noche(s), total: S/. {total:.2f}"

    # ---------- cancelar ----------

    def cancelar(self, codigo):
        h = None
        for hab in self.habitaciones:  # búsqueda duplicada (ver _buscar)
            if hab.codigo == codigo:
                h = hab
                break
        if h is None:
            return "E01: habitacion no encontrada"
        # BUG (Adecuacion funcional / correccion): "cancelar" no libera la
        # habitacion; el estado se queda en "Ocupada" (equivalente a que
        # "eliminar" no elimine).
        return f"Reserva de {codigo} cancelada."

    # ---------- caja ----------

    def ver_caja(self):
        return self.caja
