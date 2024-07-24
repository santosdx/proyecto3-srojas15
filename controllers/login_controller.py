from flask import render_template, make_response, request, redirect, url_for
from flask_restful import Resource
from models.usuarios import Usuarios
from flask_login import login_user
from models.heladeria import Heladeria


class LoginController(Resource):

    def get(self):
        return make_response(render_template("login.html"))

    def post(self):
        username = request.form['username']
        password = request.form['password']
        user = Usuarios.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            if user.is_admin:
                return redirect(url_for("productos"))
            else:
                return redirect(url_for("ingredientes"))

        heladeria = Heladeria("La Heladeria")
        items = heladeria.lista_productos()
        return make_response(render_template("index.html", items=items))
