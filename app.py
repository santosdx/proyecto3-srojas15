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


api.add_resource(InfoController, '/info')
api.add_resource(IndexController, '/index', endpoint="index")
api.add_resource(HeladeriaController, '/heladeria', endpoint="heladeria")
api.add_resource(ProductosController, '/los_productos', endpoint="lst_productos")
api.add_resource(IngredientesController, '/los_ingredientes',  endpoint="lst_ingredientes")
api.add_resource(ProductosIngredientesController, '/productos_ingredientes')
