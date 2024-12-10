from tg_API.core import bot
from tg_API.utils.create_paginator import create_paginator


def send_film_page(user_id: str, page: int = 1) -> None:
    """
    Функция получает из базы данных бота список фильмов и преобразует его для демонстрации в боте,
    а также запускает функцию пагинатора.
    :param user_id: индификатор пользователя.
    :param page: начальная страница пагинатора.
    """
    with bot.retrieve_data(user_id) as data:
        movies = data['movie_data']
        movie_info = 'Название: "{movie_name}"\n' \
                     'Рейтинг: {rating}\n' \
                     'Год выпуска: {movie_year}\n' \
                     'Жанры фильма: {movie_genres}\n' \
                     'Возрастное ограничение: {ageRating}\n' \
                     'Описание фильма: {description}' \
                     '\n{poster_url}' \
            .format(**movies[page - 1])

        paginator = create_paginator(movies, page)

        bot.send_message(
            user_id,
            movie_info,
            reply_markup=paginator.markup,
        )
        data['history_watched_movies'].append(movies[page - 1])
