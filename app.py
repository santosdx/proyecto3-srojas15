import os
import sys
from flask import Flask, redirect, url_for
from flask_restful import Api
from dotenv import load_dotenv
from db import db
from flask_login import LoginManager, logout_user, login_required
from controllers.login_controller import LoginController
from controllers.info_controller import InfoController
from controllers.index_controller import IndexController
from controllers.heladeria_controller import HeladeriaController
from controllers.productos_controller import ProductosController
from controllers.ingredientes_controller import IngredientesController
from controllers.productos_ingredientes_controller import ProductosIngredientesController
from models.usuarios import Usuarios


load_dotenv()

secret_key = os.urandom(24)

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (f'mysql'
                                         f'://{os.getenv("USER_DB")}'
                                         f':{os.getenv("PASSWORD_DB")}'
                                         f'@{os.getenv("HOST_DB")}'
                                         f':{os.getenv("HOST_PORT")}'
                                         f'/{os.getenv("SCHEMA_DB")}')
app.config["SECRET_KEY"] = secret_key
db.init_app(app)
api = Api(app)
login_manager = LoginManager(app)

import common.api_route_controllers

@login_manager.user_loader
def load_user(user_id):
    user = Usuarios.query.get(user_id)
    if user:
        return user
    return None


@app.route("/")
def main():
    return "Bienvenidos..."

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("logincontroller"))


api.add_resource(InfoController, '/info')
api.add_resource(LoginController, '/login', endpoint="login")
api.add_resource(IndexController, '/index', endpoint="index")
api.add_resource(HeladeriaController, '/heladeria', endpoint="heladeria")
api.add_resource(ProductosController, '/los_productos', endpoint="lst_productos")
api.add_resource(IngredientesController, '/los_ingredientes',  endpoint="lst_ingredientes")
api.add_resource(ProductosIngredientesController, '/productos_ingredientes')
