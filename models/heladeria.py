import common.funciones as funciones
from models.productos import Productos
from models.ingredientes import Ingredientes
from db import db

"""
Clase que contiene los atributos y funciones propias de la Heladeria.
"""


class Heladeria:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__lista_productos = self.lista_productos()
        self.__venta_del_dia = 0

    def get_nombre(self) -> str:
        return self.__nombre

    def get_venta_del_dia(self) -> float:
        return self.__venta_del_dia

    def producto_mas_rentable(self) -> str:
        return funciones.producto_mas_rentable(self.__lista_productos)

    def vender(self, nombre_producto: str) -> str:
        resultado = ""
        producto_vender = None
        for producto in self.__lista_productos:
            if producto.nombre == nombre_producto:
                producto_vender = producto
                break
        if producto_vender is not None:
            lista_ingredientes = producto_vender.ingredientes
            ingredientes_completos = True
            lista_ingredientes_sin_inventario = []
            if len(lista_ingredientes) > 0:
                for ingrediente in lista_ingredientes:
                    "Validamos para cada ingrediente el inventario"
                    if ingrediente.sabor is not None and ingrediente.inventario < 1:
                        ingredientes_completos = False
                        lista_ingredientes_sin_inventario.append(ingrediente.nombre)
                    if ingrediente.sabor is None and ingrediente.inventario < 0.2:
                        ingredientes_completos = False
                        lista_ingredientes_sin_inventario.append(ingrediente.nombre)

                if ingredientes_completos:
                    "Como los ingredientes cumplen el inventario, entonces descontamos."
                    for ingrediente in lista_ingredientes:
                        "Descontamos del inventario"
                        if ingrediente.sabor is not None and ingrediente.inventario >= 1:
                            ingrediente.inventario = (ingrediente.inventario - 1)
                        if ingrediente.sabor is None and ingrediente.inventario >= 0.2:
                            ingrediente.inventario = (ingrediente.inventario - 0.2)
                    db.session.commit()
                    self.__venta_del_dia = self.__venta_del_dia + producto_vender.precio
                    resultado = "¡Vendido!"
                else:
                    raise ValueError("¡Oh no! Nos hemos quedado sin: {0}".format(lista_ingredientes_sin_inventario))
            else:
                raise ValueError("El producto no tiene ingredientes asignados.")

        return resultado

    def lista_productos(self) -> list:
        productos = Productos.query.all()
        for item in productos:
            if item.vaso is None:
                item.vaso = ""
            if item.volumen is None:
                item.volumen = "0"
        return productos

    def lista_ingredientes(self) -> list:
        ingredientes = Ingredientes.query.all()
        for item in ingredientes:
            if item.vegetariano:
                item.vegetariano = "Si"
            else:
                item.vegetariano = "No"
            if item.sabor is None:
                item.sabor = ""
        return ingredientes

    def get_all_productos(self) -> list:
        return Productos.query.all()

    def get_producto_by_id(self, id_producto: int) -> list:
        return Productos.query.get(id_producto)

    def get_producto_by_name(self, nombre: str) -> list:
        return Productos.query.filter(Productos.nombre == nombre).first()

    def get_all_ingredientes(self) -> list:
        return Ingredientes.query.all()

    def get_ingredientes_by_id(self, id_ingrediente: int) -> list:
        return Ingredientes.query.get(id_ingrediente)

    def get_ingrediente_by_name(self, nombre: str) -> list:
        return Ingredientes.query.filter(Ingredientes.nombre == nombre).first()
