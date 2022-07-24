# здесь контроллеры/хендлеры/представления для обработки запросов (flask ручки). сюда импортируются сервисы из пакета service
from flask import request
from flask_restx import Resource, Namespace
from implemented import movie_service
from dao.model.movie import movies_schema, movie_schema


movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    """
    Класс имеет методы возвращающий все фильмы (get), либо создающий фильм (post).
    """
    def get(self):
        all_movies = movie_service.get_all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "", 201


@movie_ns.route('/<int:movie_id>/')
class MovieView(Resource):
    """
    Класс имеет методы, возвращающий, изменяющий, удаляющий фильм по id.
    """
    def get(self, movie_id):
        movie = movie_service.get_one(movie_id)
        return movie_schema.dump(movie), 200

    def put(self, movie_id):
        req_json = request.json
        req_json['id'] = movie_id
        movie_service.update(req_json)
        return "", 204

    def delete(self, movie_id):
        movie_service.delete(movie_id)
        return "", 204
