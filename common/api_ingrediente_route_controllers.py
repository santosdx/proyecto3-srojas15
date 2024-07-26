from app import app
from db import db
from flask import request, render_template
from flask_login import AnonymousUserMixin
from models.heladeria import Heladeria
import common.seguridad as seguridad
import common.funciones as funciones


@app.route("/ingredientes")
def ingredientes():
    usuario = seguridad.obtener_usuario_logueado()
    template = "401.html"
    mensaje = "No autorizado!"
    if isinstance(usuario, AnonymousUserMixin):
        return render_template(template, mensaje=mensaje)
    else:
        heladeria = Heladeria("La Heladeria")
        items = heladeria.get_all_ingredientes()
        response = seguridad.get_response_json(items)
        if usuario.is_admin:
            '''Administrador'''
            return response
        elif usuario.is_employee:
            '''Empleado'''
            return response
        else:
            '''Cliente'''
            mensaje = "El cliente: {0}, No esta autorizado!".format(usuario.full_name)
    return render_template(template, mensaje=mensaje)


@app.route("/ingredientes/<id_ingrediente>")
def ingredientes_id(id_ingrediente):
    usuario = seguridad.obtener_usuario_logueado()
    template = "401.html"
    mensaje = "No autorizado!"
    if isinstance(usuario, AnonymousUserMixin):
        return render_template(template, mensaje=mensaje)
    else:
        heladeria = Heladeria("La Heladeria")
        item = heladeria.get_ingredientes_by_id(id_ingrediente)
        response = seguridad.get_response_json(item)
        if usuario.is_admin:
            '''Administrador'''
            return response
        elif usuario.is_employee:
            '''Empleado'''
            return response
        else:
            '''Cliente'''
            mensaje = "El cliente: {0}, No esta autorizado!".format(usuario.full_name)
    return render_template(template, mensaje=mensaje)


@app.route("/ingredientes/")
def ingrediente_nombre():
    usuario = seguridad.obtener_usuario_logueado()
    template = "401.html"
    mensaje = "No autorizado!"
    if isinstance(usuario, AnonymousUserMixin):
        return render_template(template, mensaje=mensaje)
    else:
        nombre = request.args.get('nombre')
        heladeria = Heladeria("La Heladeria")
        item = heladeria.get_ingrediente_by_name(nombre)
        response = seguridad.get_response_json(item)
        if usuario.is_admin:
            '''Administrador'''
            return response
        elif usuario.is_employee:
            '''Empleado'''
            return response
        else:
            '''Cliente'''
            mensaje = "El cliente: {0}, No esta autorizado!".format(usuario.full_name)
    return render_template(template, mensaje=mensaje)


@app.route("/ingredientes/<id_ingrediente>/sano")
def ingredientes_sano(id_ingrediente):
    usuario = seguridad.obtener_usuario_logueado()
    template = "401.html"
    mensaje = "No autorizado!"
    if isinstance(usuario, AnonymousUserMixin):
        return render_template(template, mensaje=mensaje)
    else:
        heladeria = Heladeria("La Heladeria")
        item = heladeria.get_ingredientes_by_id(id_ingrediente)
        if item is None:
            response = seguridad.get_response_json(item)
        else:
            es_sano = funciones.is_ingrediente_sano(item.calorias, item.vegetariano)
            response = seguridad.get_response_json(es_sano)
        if usuario.is_admin:
            '''Administrador'''
            return response
        elif usuario.is_employee:
            '''Empleado'''
            return response
        else:
            '''Cliente'''
            mensaje = "El cliente: {0}, No esta autorizado!".format(usuario.full_name)
    return render_template(template, mensaje=mensaje)


@app.route("/ingredientes/<id_ingrediente>/reabastecer")
def ingredientes_reabastecer(id_ingrediente):
    usuario = seguridad.obtener_usuario_logueado()
    template = "401.html"
    mensaje = "No autorizado!"
    if isinstance(usuario, AnonymousUserMixin):
        return render_template(template, mensaje=mensaje)
    else:
        heladeria = Heladeria("La Heladeria")
        item = heladeria.get_ingredientes_by_id(id_ingrediente)
        if item is None:
            response = seguridad.get_response_json(item)
        else:
            item.abastecer()
            db.session.commit()
            response = seguridad.get_response_json(item)
        if usuario.is_admin:
            '''Administrador'''
            return response
        elif usuario.is_employee:
            '''Empleado'''
            return response
        else:
            '''Cliente'''
            mensaje = "El cliente: {0}, No esta autorizado!".format(usuario.full_name)
    return render_template(template, mensaje=mensaje)


@app.route("/ingredientes/<id_ingrediente>/inventario/<inventario>")
def ingredientes_inventario(id_ingrediente, inventario):
    usuario = seguridad.obtener_usuario_logueado()
    template = "401.html"
    mensaje = "No autorizado!"
    if isinstance(usuario, AnonymousUserMixin):
        return render_template(template, mensaje=mensaje)
    else:
        heladeria = Heladeria("La Heladeria")
        item = heladeria.get_ingredientes_by_id(id_ingrediente)
        if item is None:
            response = seguridad.get_response_json(item)
        else:
            item.renovar_inventario(inventario)
            db.session.commit()
            response = seguridad.get_response_json(item)
        if usuario.is_admin:
            '''Administrador'''
            return response
        elif usuario.is_employee:
            '''Empleado'''
            return response
        else:
            '''Cliente'''
            mensaje = "El cliente: {0}, No esta autorizado!".format(usuario.full_name)
    return render_template(template, mensaje=mensaje)
