from flask_restx import Resource, Namespace
from implemented import director_service
from dao.model.director import directors_schema, director_schema


director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    """
    Класс имеет метод возвращающий всех режиссёров.
    """
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200


@director_ns.route('/<int:director_id>/')
class DirectorView(Resource):
    """
    Класс имеет метод, возвращающий режиссёра по id.
    """
    def get(self, director_id):
        director = director_service.get_one(director_id)
        return director_schema.dump(director), 200