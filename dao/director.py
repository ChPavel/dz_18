from dao.model.director import Director


class DirectorDAO:
    """
    Класс работы с БД имеет методы:
    get_all - возвращает все объекты модели Director;
    get_one - возвращает объект модели Director по "id".
    """
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return Director.query.all()

    def get_one(self, genre_id):
        return Director.query.get(genre_id)
