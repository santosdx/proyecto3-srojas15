from flask import render_template, make_response
from flask_restful import Resource
from models.info import Info


class InfoController(Resource):

    def get(self):
        info = Info.query.get(1)
        return make_response(render_template("info.html", app=info))
