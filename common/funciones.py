"""
Módulo que contiene las funciones utilitarias para el funcionamiento de la
Heladeria.
"""


def is_ingrediente_sano(numero_calorias: int, is_vegetariano: bool) -> bool:
    """ Función que identificar si un ingrediente es sano.
    :param numero_calorias: Número de calorias.
    :param is_vegetariano: El ingrediente es vegetariano.
    :return: Es o no sano el ingrediente (True/False).
    """
    if is_vegetariano or numero_calorias < 100:
        return True
    else:
        return False


def producto_conteo_calorias(calorias: list) -> float:
    """ Función que permite hacer el conteo de calorías de un producto.
    :param calorias: Lista de calorías.
    :return: Conteo de calorías.
    """
    conteo = 0
    for caloria in calorias:
        conteo = conteo + caloria
    conteo = round(conteo * 0.95, 2)
    return conteo


def producto_conteo_calorias_v2(calorias: list) -> float:
    """ Función que permite hacer el conteo de calorías de un producto.
    :param calorias: Lista de calorías.
    :return: Conteo de calorías.
    """
    conteo = 0
    for caloria in calorias:
        conteo = conteo + caloria
    conteo = round(conteo, 2)
    return conteo


def producto_costo_produccion_v1(datos_ingredientes: list) -> float:
    """ Función que permite calcular el costo de produccion de un producto.
    :param datos_ingredientes: Lista con los diccionarios con los datos de los ingredientes.
    :return: Costo de producción.
    """
    costo = 0
    for ingrediente in datos_ingredientes:
        for llave, valor in ingrediente.items():
            if llave == "precio":
                costo = costo + float(valor)
    return costo


def producto_costo_produccion(datos_ingredientes: list) -> float:
    """ Función que permite calcular el costo de produccion de un producto.
    :param datos_ingredientes: Lista con los objetos con los datos de los ingredientes.
    :return: Costo de producción.
    """
    costo = 0
    for ingrediente in datos_ingredientes:
        costo = costo + float(ingrediente.precio)
    return costo


def producto_rentabilidad(precio_venta: float, datos_ingredientes: list) -> float:
    """ Función que permite calcular la rentabilidad de un producto.
    :param precio_venta: Precio de venta del producto.
    :param datos_ingredientes: Lista con los objetos con los datos de los ingredientes.
    :return: Rentabilidad.
    """
    return precio_venta - producto_costo_produccion(datos_ingredientes)


def producto_rentabilidad_v1(precio_venta: float, datos_ingredientes: list) -> float:
    """ Función que permite calcular la rentabilidad de un producto.
    :param precio_venta: Precio de venta del producto.
    :param datos_ingredientes: Lista con los objetos con los datos de los ingredientes.
    :return: Rentabilidad.
    """
    return precio_venta - producto_costo_produccion_v1(datos_ingredientes)


def producto_mas_rentable_v1(datos_productos: list) -> str:
    """ Función que permite identificar el producto mas rentable.
    :param datos_productos: Lista con los diccionarios con los datos de los ingredientes.
    :return: Productos más rentables.
    """
    lst_productos = []
    max_rentabilidad = max(datos_productos, key=lambda x: x['rentabilidad'])
    for producto in datos_productos:
        for llave, valor in producto.items():
            if llave == "rentabilidad" and valor == max_rentabilidad.get("rentabilidad"):
                lst_productos.append(producto.get("nombre"))
    return str(lst_productos)


def producto_mas_rentable(datos_productos: list) -> str:
    """ Función que permite identificar el producto mas rentable.
    :param datos_productos: Lista con los objetos con los datos de los ingredientes.
    :return: Productos más rentables.
    """
    lst_productos = []
    max_rentabilidad = max(datos_productos, key=lambda x: producto_rentabilidad(x.precio, x.ingredientes))
    for producto in datos_productos:
        if (producto_rentabilidad(producto.precio, producto.ingredientes) ==
                producto_rentabilidad(max_rentabilidad.precio, max_rentabilidad.ingredientes)):
            lst_productos.append(producto.nombre)
    return str(lst_productos)
