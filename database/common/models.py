from peewee import SqliteDatabase, Model, CharField, IntegerField, FloatField, ForeignKeyField

db = SqliteDatabase('database/history/message_history.db')


# класс, чтобы наследовать от него все таблицы базы данных
class BaseModel(Model):
    """
    Класс создания базы данных, от него наследуются класс таблица базы данных: User, Movie
    """

    class Meta:
        database = db


class User(BaseModel):
    """
    Класс описывающий таблицу пользователя в базе данных
    """

    name = CharField()
    telegram_id = IntegerField()


class Movie(BaseModel):
    """
    Класс описывающий создание таблица фильмов с привязкой к пользователю
    """

    movie_name = CharField()
    movie_year = IntegerField()
    movie_genres = CharField()
    rating = FloatField()
    user = ForeignKeyField(User, backref="movies")  # Ссылка на пользователя


db.create_tables(BaseModel.__subclasses__())  # Создание бд и таблиц
