from telebot.types import Message

from site_API.core import site_api, url, headers
from tg_API.core import bot
from tg_API.states.movie_info import MovieInfoState
from tg_API.utils.output_movie import output_movie


@bot.message_handler(state=MovieInfoState.movie_name)
def name_movie(message: Message) -> None:
    """
    Функция передаёт полученное название фильма, так же url и headers в функцию get_movie_by_name.
    Возвращённый ответ со списком картежей фильмов передаёт в функцию output_movie для преобразования
    в отображаемый в боте вид и запуска выбора действий по запуску пагинатора. Переводит бот в состояние
    для запуска погинатора.
    """
    name = message.text.strip()
    movie_name = site_api.get_movie_by_name()

    response_name_movie = movie_name(url=url, headers=headers, movie_name=name)

    if response_name_movie == 504:
        bot.send_message(message.from_user.id,
                         "Возникла проблема на сервере.\n"
                         "Повторите запрос позже.\n"
                         "Вы возвращены в основное меню.")
        bot.delete_state(message.from_user.id)
        bot.set_state(message.from_user.id, MovieInfoState.menu, message.chat.id)
    else:
        output_movie(message, response_name_movie.json()['docs'])
        bot.set_state(message.from_user.id, MovieInfoState.start_paginator_movie, message.chat.id)

