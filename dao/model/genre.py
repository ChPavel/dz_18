from setup_db import db
from marshmallow import Schema, fields


class Genre(db.Model):
    """
    Модель для жанров.
    """
    __tablename__ = 'genres'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250))


class GenreSchema(Schema):
    """
    Схема для жанров.
    """
    id = fields.Int(dump_only=True)
    name = fields.Str()


genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)