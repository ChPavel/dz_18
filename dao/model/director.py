from setup_db import db
from marshmallow import Schema, fields

class Director(db.Model):
    """
    Модель для режиссёров.
    """
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class DirectorSchema(Schema):
    """
    Схема для режиссёров.
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()


director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)