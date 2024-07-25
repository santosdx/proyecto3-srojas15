from app import app
from json import JSONEncoder
from models.usuarios import Usuarios
from flask_login import current_user, AnonymousUserMixin

"""
Clase que contiene los atributos y funciones propias para la seguridad de la pagina.
"""


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.to_dict()


def obtener_usuario_logueado() -> Usuarios:
    usuario = AnonymousUserMixin()
    if isinstance(current_user, AnonymousUserMixin) is False:
        id_usuario = current_user.id
        usuario = Usuarios.query.get(id_usuario)
    return usuario


def get_response_json(items: list) -> str:
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
