from app import app
from flask import render_template, request
from flask_login import login_required, AnonymousUserMixin
from models.heladeria import Heladeria
import common.seguridad as seguridad


@app.route("/productoss")
def productoss():
    usuario = seguridad.obtener_usuario_logueado()
    template = "401.html"
    mensaje = "No autorizado!"
    if isinstance(usuario, AnonymousUserMixin):
        return render_template(template, mensaje=mensaje)
    else:
        heladeria = Heladeria("La Heladeria")
        items = heladeria.get_all_productos()
        response = seguridad.get_response_json(items)
        if usuario.is_admin:
            '''Administrador'''
            return response
        elif usuario.is_employee:
            '''Empleado'''
            mensaje = "El empleado: {0}, No esta autorizado!".format(usuario.full_name)
        else:
            '''Cliente'''
            mensaje = "El cliente: {0}, No esta autorizado!".format(usuario.full_name)

    return render_template(template, mensaje=mensaje)


@app.route("/productos")
def productos():
    heladeria = Heladeria("La Heladeria")
    items = heladeria.get_all_productos()
    response = seguridad.get_response_json(items)
    return response


@app.route("/productos/<id_producto>")
def producto_id(id_producto):
    heladeria = Heladeria("La Heladeria")
    item = heladeria.get_producto_by_id(id_producto)
    response = seguridad.get_response_json(item)
    return response


@app.route("/productos/")
def producto_nombre():
    nombre = request.args.get('nombre')
    heladeria = Heladeria("La Heladeria")
    item = heladeria.get_producto_by_name(nombre)
    response = seguridad.get_response_json(item)
    return response


@app.route("/productos/<id_producto>/calorias")
def producto_calorias(id_producto):
    heladeria = Heladeria("La Heladeria")
    item = heladeria.get_producto_by_id(id_producto)
    response = seguridad.get_response_json(item.calcular_calorias())
    return response


@app.route("/productos/<id_producto>/rentabilidad")
def producto_rentabilidad(id_producto):
    heladeria = Heladeria("La Heladeria")
    item = heladeria.get_producto_by_id(id_producto)
    response = seguridad.get_response_json(item.calcular_rentabilidad())
    return response


@app.route("/productos/<id_producto>/costo")
def producto_costo(id_producto):
    heladeria = Heladeria("La Heladeria")
    item = heladeria.get_producto_by_id(id_producto)
    response = seguridad.get_response_json(item.calcular_costo())
    return response


@app.route("/productos/vender/<id_producto>")
def producto_vender(id_producto):
    heladeria = Heladeria("La Heladeria")
    item = heladeria.get_producto_by_id(id_producto)
    if item is not None:
        try:
            resultado_venta = heladeria.vender(item.nombre)
        except ValueError as ex:
            resultado_venta = ex.__str__()
    else:
        resultado_venta = "Ooops! el ID:{0} de producto no existe.".format(request.form['idProducto'])
    return resultado_venta
