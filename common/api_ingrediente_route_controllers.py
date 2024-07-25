from app import app
from flask import render_template, request
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
    es_sano = funciones.is_ingrediente_sano(item.calorias, item.vegetariano)
    response = seguridad.get_response_json(es_sano)
    return response


@app.route("/ingredientes/<id_ingrediente>/reabastecer/<cantidad>")
def ingredientes_reabastecer(id_ingrediente, cantidad):
    heladeria = Heladeria("La Heladeria")
    item = heladeria.get_ingredientes_by_id(id_ingrediente)
    es_sano = funciones.is_ingrediente_sano(item.calorias, item.vegetariano)
    response = seguridad.get_response_json(es_sano)
    return response
