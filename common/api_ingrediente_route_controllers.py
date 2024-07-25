from app import app
from db import db
from flask import request
from flask_login import login_required, AnonymousUserMixin
from models.heladeria import Heladeria
import common.seguridad as seguridad
import common.funciones as funciones


@app.route("/ingredientes")
def ingredientes():
    heladeria = Heladeria("La Heladeria")
    items = heladeria.get_all_ingredientes()
    response = seguridad.get_response_json(items)
    return response


@app.route("/ingredientes/<id_ingrediente>")
def ingredientes_id(id_ingrediente):
    heladeria = Heladeria("La Heladeria")
    item = heladeria.get_ingredientes_by_id(id_ingrediente)
    response = seguridad.get_response_json(item)
    return response


@app.route("/ingredientes/")
def ingrediente_nombre():
    nombre = request.args.get('nombre')
    heladeria = Heladeria("La Heladeria")
    item = heladeria.get_ingrediente_by_name(nombre)
    response = seguridad.get_response_json(item)
    return response


@app.route("/ingredientes/<id_ingrediente>/sano")
def ingredientes_sano(id_ingrediente):
    heladeria = Heladeria("La Heladeria")
    item = heladeria.get_ingredientes_by_id(id_ingrediente)
    if item is None:
        response = seguridad.get_response_json(item)
    else:
        es_sano = funciones.is_ingrediente_sano(item.calorias, item.vegetariano)
        response = seguridad.get_response_json(es_sano)
    return response


@app.route("/ingredientes/<id_ingrediente>/reabastecer")
def ingredientes_reabastecer(id_ingrediente):
    heladeria = Heladeria("La Heladeria")
    item = heladeria.get_ingredientes_by_id(id_ingrediente)
    if item is None:
        response = seguridad.get_response_json(item)
    else:
        item.abastecer()
        db.session.commit()
        response = seguridad.get_response_json(item)
    return response


@app.route("/ingredientes/<id_ingrediente>/inventario/<inventario>")
def ingredientes_inventario(id_ingrediente, inventario):
    heladeria = Heladeria("La Heladeria")
    item = heladeria.get_ingredientes_by_id(id_ingrediente)
    if item is None:
        response = seguridad.get_response_json(item)
    else:
        item.renovar_inventario(inventario)
        db.session.commit()
        response = seguridad.get_response_json(item)
    return response
