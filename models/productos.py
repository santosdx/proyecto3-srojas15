from db import db
from models.productos_ingredientes import ProductosIngredientes
import common.funciones as funciones


class Productos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(), nullable=False)
    precio = db.Column(db.Float(), nullable=False)
    vaso = db.Column(db.String(), nullable=True)
    volumen = db.Column(db.Integer(), nullable=True)

    ingredientes = db.relationship('Ingredientes', secondary='productos_ingredientes',
                                   lazy='subquery', backref=db.backref('productos', lazy=True))

    def __init__(self, nombre: str, precio: float, vaso: str,  volumen: int, ingredientes: list):
        self.nombre = nombre
        self.precio = precio
        self.vaso = vaso
        self.volumen = volumen
        self.ingredientes = ingredientes

    def calcular_calorias(self) -> float:
        lista_calorias = []
        for ingrediente in self.ingredientes:
            lista_calorias.append(ingrediente.calorias)
        if self.vaso is None:
            '''Malteada'''
            return funciones.producto_conteo_calorias_v2(lista_calorias) + 200
        else:
            '''Copa'''
            return funciones.producto_conteo_calorias(lista_calorias)

    def calcular_costo(self) -> float:
        if self.vaso is None:
            '''Malteada'''
            return funciones.producto_costo_produccion(self.ingredientes) + 500
        else:
            '''Copa'''
            return funciones.producto_costo_produccion(self.ingredientes)

    def calcular_rentabilidad(self):
        return funciones.producto_rentabilidad(self.precio, self.ingredientes)

    def to_dict(self):
        dic = {"nombre": self.nombre, "precio:": self.precio, "vaso:": self.vaso, "volumen:": self.volumen}
        return dic
