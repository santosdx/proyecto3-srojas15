from app import app
from json import JSONEncoder
from flask import Response
from flask_login import login_user, login_required, current_user
from models.heladeria import Heladeria


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.to_dict()


@app.route("/productos/")
def productos():
    print("Usuario:", current_user.id)
    heladeria = Heladeria("La Heladeria")
    items = heladeria.get_all_productos()
    if items is None:
        response = app.response_class(
            response="{}",
            status=404,
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=MyEncoder().encode(items),
            status=200,
            mimetype='application/json'
        )
    return response


@app.route("/productos/<int:id_producto>")
@login_required
def productos_id(id_producto):
    heladeria = Heladeria("La Heladeria")
    item = heladeria.get_producto_by_id(id_producto)
    if item is None:
        response = app.response_class(
            response="{}",
            status=404,
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=MyEncoder().encode(item),
            status=200,
            mimetype='application/json'
        )
    return response
