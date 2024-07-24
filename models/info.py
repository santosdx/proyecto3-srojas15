from db import db


class Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(), nullable=False)
