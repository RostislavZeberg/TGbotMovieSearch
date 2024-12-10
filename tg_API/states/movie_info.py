from telebot.handler_backends import State, StatesGroup


class MovieInfoState(StatesGroup):
    """
    Класс определяющий группу состояний в боте.
    """
    movie_name = State()
    movie_genre = State()
    movie_genre_and_year = State()
    paginator_movie = State()
    start_paginator_movie = State()
    menu = State()
    block_keyboard = State()
    paginator_history = State()
    start_paginator_history = State()
