from flask import render_template, make_response
from flask_restful import Resource
from models.productos_ingredientes import ProductosIngredientes


class ProductosIngredientesController(Resource):

    def get(self):
        items = ProductosIngredientes.query.all()
        return make_response(render_template("productos_ingredientes.html", items=items))
