from typing import List, Dict

from main import user_facade
from tg_API.core import bot
from tg_API.states.movie_info import MovieInfoState
from tg_API.utils.create_paginator import create_paginator


def send_history_page(user_id: str, chat_id: str, page: int = 1) -> None:
    """
    Функция получает из базы данных список просмотренных фильмов и преобразует его для демонстрации в боте,
    а также запускает функцию пагинатора. Если пользователь не имеет базы данных или отсутствует
    список просмотренных фильмов, бот переходит к состоянию меню.
    :param user_id: индификатор пользователя.
    :param chat_id: индификатор чата.
    :param page: начальная страница пагинатора.
    """
    user = user_facade.get_by_telegram_id(user_id)

    movies: List[dict] = []

    if user is not None:
        for movie in user.movies:
            temp: Dict = {'movie_name': movie.movie_name, 'movie_year': movie.movie_year,
                          'movie_genres': movie.movie_genres, 'rating': movie.rating}
            movies.append(temp)
    else:
        bot.delete_state(user_id)
        bot.set_state(user_id, MovieInfoState.menu, chat_id)

    if len(movies) > 0:
        film_info = 'Название: "{movie_name}"\n' \
                    'Год выпуска: {movie_year}\n' \
                    'Жанры фильма: {movie_genres}\n' \
                    'Рейтинг: {rating}\n' \
            .format(**movies[page - 1])

        paginator = create_paginator(movies, page)

        bot.send_message(
            user_id,
            film_info,
            reply_markup=paginator.markup,
        )
    else:
        bot.send_message(user_id, "В истории нет фильмов.\nМожете вернуться к основному меню в панели.")
        bot.delete_state(user_id)
        bot.set_state(user_id, MovieInfoState.menu, chat_id)

