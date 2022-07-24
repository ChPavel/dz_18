from flask_restx import Resource, Namespace
from implemented import genre_service
from dao.model.genre import genres_schema, genre_schema


genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    """
    Класс имеет метод возвращающий все жанры.
    """
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:genre_id>/')
class GenreView(Resource):
    """
    Класс имеет метод, возвращающий жанр по id.
    """
    def get(self, genre_id):
        genre = genre_service.get_one(genre_id)
        return genre_schema.dump(genre), 200
