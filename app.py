# основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy и все остальное что требуется для приложения.
# этот файл часто является точкой входа в приложение
from flask import Flask
from flask_restx import Api
from config import Config
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from setup_db import db
from views.director import director_ns
from views.genre import genre_ns
from views.movie import movie_ns


def create_app(config_object):
    """
    Функция создания основного объекта app.
    """
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    configure_app(app)
    return app


def configure_app(app):
    """
    Функция настойки приложения.
    """
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    create_data(app, db)


def create_data(app, db):
    """
    Функция создания базы данных.
    """
    with app.app_context():
        db.create_all()
        m1 = Movie(id=1, title='Йеллоустоун', description='Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»', trailer='https://www.youtube.com/watch?v=UKei_d0cbP4', year=2018, rating=8.6, genre_id=17, director_id=1)
        m2 = Movie(id=2, title='Омерзительная восьмерка', description='США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке Вешатель конвоирует заключенную. По пути к ним прибиваются еще несколько путешественников. Снежная буря вынуждает компанию искать укрытие в лавке на отшибе, где уже расположилось весьма пестрое общество: генерал конфедератов, мексиканец, ковбой… И один из них - не тот, за кого себя выдает.', trailer='https://www.youtube.com/watch?v=lmB9VWm0okU', year=2015, rating=7.8, genre_id=4, director_id=2)
        m3 = Movie(id=3, title='Вооружен и очень опасен', description='События происходят в конце XIX века на Диком Западе, в Америке. В основе сюжета — сложные перипетии жизни работяги — старателя Габриэля Конроя. Найдя нефть на своем участке, он познает и счастье, и разочарование, и опасность, и отчаяние...', trailer='https://www.youtube.com/watch?v=hLA5631F-jo', year=1978, rating=6, genre_id=17, director_id=3)
        m4 = Movie(id=4, title='Рокетмен', description='История превращения застенчивого парня Реджинальда Дуайта, талантливого музыканта из маленького городка, в суперзвезду и культовую фигуру мировой поп-музыки Элтона Джона.', trailer='https://youtu.be/VISiqVeKTq8', year=2019, rating=7.3, genre_id =18, director_id =4)
        g1 = Genre(id=1, name="Комедия")
        g2 = Genre(id=4, name="Драма")
        g3 = Genre(id=17, name="Вестерн")
        g4 = Genre(id=18, name="Мюзикл")
        d1 = Director(id=1, name="Тейлор Шеридан")
        d2 = Director(id=2, name="Квентин Тарантино")
        d3 = Director(id=3, name="Владимир Вайншток")
        d4 = Director(id=4, name="Декстер Флетчер")
        with db.session.begin():
            db.session.add_all([m1, m2, m3, m4])
            db.session.add_all([g1, g2, g3, g4])
            db.session.add_all([d1, d2, d3, d4])


app = create_app(Config())


if __name__ == '__main__':
    app.run(host="localhost", port=10001)
