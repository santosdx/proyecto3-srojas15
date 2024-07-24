import os
from flask import Flask, render_template
from flask_restful import Api
from dotenv import load_dotenv
from db import db
from controllers.info_controller import InfoController
from controllers.index_controller import IndexController
from controllers.heladeria_controller import HeladeriaController
from controllers.productos_controller import ProductosController
from controllers.ingredientes_controller import IngredientesController
from controllers.productos_ingredientes_controller import ProductosIngredientesController
from models.heladeria import Heladeria

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (f'mysql'
                                         f'://{os.getenv("USER_DB")}'
                                         f':{os.getenv("PASSWORD_DB")}'
                                         f'@{os.getenv("HOST_DB")}'
                                         f':{os.getenv("HOST_PORT")}'
                                         f'/{os.getenv("SCHEMA_DB")}')
db.init_app(app)
api = Api(app)


@app.route("/")
def main():
    return "Bienvenidos..."


@app.route("/index")
def menu():
    heladeria = Heladeria("La Heladeria")
    items = heladeria.lista_productos()
    return render_template("index.html", items=items)


@app.route("/productos")
def lst_productos():
    heladeria = Heladeria("La Heladeria")
    items = heladeria.lista_productos()
    return render_template("productos.html", items=items)


@app.route("/ingredientes")
def lst_ingredientes():
    heladeria = Heladeria("La Heladeria")
    items = heladeria.lista_ingredientes()
    return render_template("ingredientes.html", items=items)


api.add_resource(InfoController, '/info')
api.add_resource(IndexController, '/index')
api.add_resource(HeladeriaController, '/heladeria')
api.add_resource(ProductosController, '/productos')
api.add_resource(IngredientesController, '/ingredientes')
api.add_resource(ProductosIngredientesController, '/productos_ingredientes')
