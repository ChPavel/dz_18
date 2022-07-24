from dao.director import DirectorDAO


class DirectorService:
    """
    Класс подготовки данных, получаемых от DirectorDAO, для представлений, имеет методы:
    get_all - возвращяет все объекты, полученные через get_all() класса DirectorDAO;
    get_one - возвращает объект модели Director по "id", полученные через get_one() класса DirectorDAO;
    """
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_all(self):
        return self.director_dao.get_all()

    def get_one(self, director_id):
        return self.director_dao.get_one(director_id)
