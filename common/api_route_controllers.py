from app import app
from flask import render_template
from flask_login import login_required, AnonymousUserMixin
from models.heladeria import Heladeria
import common.seguridad as seguridad


@app.route("/productos")
def productos():
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


@app.route("/productos/<int:id_producto>")
@login_required
def productos_id(id_producto):
    heladeria = Heladeria("La Heladeria")
    item = heladeria.get_producto_by_id(id_producto)
    response = seguridad.get_response_json(item)
    return response
