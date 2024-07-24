from db import db


class Ingredientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(), nullable=False)
    precio = db.Column(db.Float(), nullable=False)
    calorias = db.Column(db.Integer(), nullable=False)
    vegetariano = db.Column(db.Boolean(), nullable=False)
    inventario = db.Column(db.Float(), nullable=False)
    sabor = db.Column(db.String(), nullable=True)

    def __init__(self, nombre: str, precio: float, calorias: int, vegetariano: bool, inventario: float, sabor: str):
        self.nombre = nombre
        self.precio = precio
        self.calorias = calorias
        self.vegetariano = vegetariano
        self.inventario = inventario
        self.sabor = sabor

    def to_dict(self):
        dic = {"nombre": self.nombre, "precio:": self.precio, "calorias:": self.calorias,
               "vegetariano:": self.vegetariano, "inventario:": self.inventario, "sabor:": self.sabor}
        return dic
