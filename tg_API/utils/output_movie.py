from typing import List, Dict

from tg_API.core import bot
from tg_API.utils.create_keyboards import keyboards_paginator_show
from tg_API.utils.search_movie import search_movie


def output_movie(message, movies: List[Dict]) -> None:
    """
    Функция преобразует полученный список кортежей и список жанров в отображаемый в боте вид.
    :param message: аргумент телеграмм бота - словарь данных.
    :param movies: список картежей фильмов
    """
    movie_list = search_movie(message, movies)
    keyboard = keyboards_paginator_show()

    bot.send_message(message.from_user.id,
                     f'С название:\n"{message.text.strip()}"\n'
                     f'Найдено фильмов: {len(movie_list)}\n'
                     f'Показать найденные фильмы в пагинаторе?',
                     reply_markup=keyboard)
