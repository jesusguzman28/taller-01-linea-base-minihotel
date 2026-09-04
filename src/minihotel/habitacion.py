class Habitacion:
    def __init__(self, codigo, tipo, precio_noche, estado="Libre"):
        self.codigo = codigo
        self.tipo = tipo
        self.precio_noche = precio_noche
        self.estado = estado

    def to_linea(self):
        return f"{self.codigo};{self.tipo};{self.precio_noche};{self.estado}"

    @staticmethod
    def from_linea(linea):
        codigo, tipo, precio_noche, estado = linea.strip().split(";")
        return Habitacion(codigo, tipo, float(precio_noche), estado)
