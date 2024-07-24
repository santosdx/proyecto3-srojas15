"""
Clase Usuarios.
"""
from db import db
from flask_login import UserMixin


class Usuarios(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=True)
    full_name = db.Column(db.String(), nullable=True)
    is_admin = db.Column(db.Boolean, nullable=True)
    is_employee = db.Column(db.Boolean, nullable=True)

    def __init__(self, id: int, username: str, password: str, full_name: str, is_admin: bool, is_employee: bool):
        self.id = id
        self.username = username
        self.password = password
        self.full_name = full_name
        self.is_admin = is_admin
        self.is_employee = is_employee
