from dao.model.genre import Genre


class GenreDAO:
    """
    Класс работы с БД имеет методы:
    get_all - возвращает все объекты модели Genre;
    get_one - возвращает объект модели Genre по "id".
    """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return Genre.query.all()

    def get_one(self, genre_id):
        return Genre.query.get(genre_id)

