from datetime import datetime

from telebot.types import Message

from site_API.core import site_api, url, headers
from tg_API.core import bot
from tg_API.states.movie_info import MovieInfoState
from tg_API.utils.output_genre import output_genre


@bot.message_handler(content_types=['text'], state=MovieInfoState.movie_genre_and_year)
def movie_by_year_and_genre(message: Message) -> None:
    """
    Функция получает сохранённое названия жанра и введённый год выпуска фильмов и передаёт в функцию получения
    списка фильмов от сервера, полученный список фильмов передаёт в функцию, которая формирует отображение
    списка фильмов в боте.
    Переводит бот в состояние для запуска погинатора показа списка фильмов.
    При вводе не корректной даты перезапускает состояние для повторного ввода даты.
    """
    year_input = message.text.strip()

    if int(year_input) < 1895:
        bot.reply_to(message, 'Первый фильмом был снят братьями Люмьер в 1895 году!\nПопробуйте ещё раз:')
        bot.set_state(message.from_user.id, MovieInfoState.movie_genre_and_year, message.chat.id)
    elif year_input.isdigit() and int(year_input) <= datetime.now().year:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['movie_year'] = message.text
            genre = data['movie_genre']
        movie_year_and_genre = site_api.get_movie_by_year_and_genre()
        response_movie = movie_year_and_genre(url=url, headers=headers, year=year_input, genres_name=genre)
        output_genre(message, response_movie.json()['docs'])
        bot.set_state(message.from_user.id, MovieInfoState.start_paginator_movie, message.chat.id)
    else:
        bot.reply_to(message, 'Год должен быть числом!\nРавен или менее текущего года!\nПопробуйте ещё раз:')
        bot.set_state(message.from_user.id, MovieInfoState.movie_genre_and_year, message.chat.id)
