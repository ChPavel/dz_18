# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.
from flask import request
from dao.model.movie import Movie
from dao.movie import MovieDAO


class MovieService:
    """
    Класс подготовки данных, получаемых от MovieDAO, для представлений, имеет методы:
    get_all - фильтрует по трём параметрам, при их поступлении, объекты Movie, и возвращяет результат или все объекты, при отсутствии фильтров;
    get_one - возвращает объект модели Movie по "id";
    update - обновляет поля объекта Movie по полученному "id" и вызывает MovieDAO.update();
    delete - вызывает MovieDAO.delete() с полученным "id";
    create - вызывает MovieDAO.create() с полученным данными.
    """
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao


    def get_all(self):
        movies_query = self.movie_dao.get_all()
        args = request.args

        genre_id = args.get('genre_id')
        if genre_id is not None:
            movies_query = movies_query.filter(Movie.genre_id == genre_id)

        director_id = args.get('director_id')
        if director_id is not None:
            movies_query = movies_query.filter(Movie.director_id == director_id)

        year = args.get('year')
        if year is not None:
            movies_query = movies_query.filter(Movie.year == year)

        return movies_query.all()


    def get_one(self, movie_id):
        return self.movie_dao.get_one(movie_id)


    def update(self, data):
        movie_id = data.get('id')
        movie = self.get_one(movie_id)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.movie_dao.update(movie)


    def delete(self, movie_id):
        return self.movie_dao.delete(movie_id)


    def create(self, data):
        return self.movie_dao.create(data)

