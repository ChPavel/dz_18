from dao.genre import GenreDAO


class GenreService:
    """
    Класс подготовки данных, получаемых от GenreDAO, для представлений, имеет методы:
    get_all - возвращяет все объекты, полученные через get_all() класса GenreDAO;
    get_one - возвращает объект модели Genre по "id", полученные через get_one() класса GenreDAO;
    """
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_all(self):
        return self.genre_dao.get_all()

    def get_one(self, genre_id):
        return self.genre_dao.get_one(genre_id)
