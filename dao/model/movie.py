# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью (но не с базой, с базой мы работает в классе DAO)


from setup_db import db
from marshmallow import Schema, fields
# from sqlalchemy.orm import relationship


class Movie(db.Model):
    """
    Модель для фильмов.
    """
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250))
    description = db.Column(db.String(500))
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))
    genres = db.relationship('Genre')
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))
    directors = db.relationship('Director')

class MovieSchema(Schema):
    """
    Схема для фильмов.
    """
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


