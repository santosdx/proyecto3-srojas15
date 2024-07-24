from models.productos import Productos
from datetime import datetime


class Venta:
    def __init__(self, producto: Productos, resultado: str, id_transaccion: str, valor: float):
        self.producto = producto
        self.resultado = resultado
        self.id_transaccion = id_transaccion
        self.valor = valor
        self.fecha = datetime.now()
