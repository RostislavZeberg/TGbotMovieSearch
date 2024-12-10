from database.common.models import User, Movie
from database.utils.CRUD import DatabaseFacade

# Создаем экземпляры класса с разными таблицами
user_facade = DatabaseFacade(User)
movie_facade = DatabaseFacade(Movie)


