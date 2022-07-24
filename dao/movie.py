# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД
from dao.model.movie import Movie


class MovieDAO:
    """
    Класс работы с БД имеет методы:
    get_all - возвращает все объекты модели Movie;
    get_one - возвращает объект модели Movie по "id";
    update - обновляет полученный объект в БД;
    delete - удаляет объект в БД по "id";
    create - создаёт объект в БД по полученным данным.
    """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie)

    def get_one(self, movie_id):
        return Movie.query.get(movie_id)

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    def delete(self, movie_id):
        movie = self.get_one(movie_id)
        self.session.delete(movie)
        self.session.commit()

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
