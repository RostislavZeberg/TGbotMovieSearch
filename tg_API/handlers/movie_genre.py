from telebot.types import Message

from site_API.core import site_api, url, headers
from tg_API.core import bot
from tg_API.states.movie_info import MovieInfoState


@bot.message_handler(state=MovieInfoState.movie_genre)
def movie_by_genre(message: Message) -> None:
    """
    Функция предлагает выбрать жанр фильмов, при ошибке ввода выдаёт список существующий жанров,
    при правильном введении названия жанра сохраняет название жанра, предлагает выбрать года выпуска фильма и
    переводит состояние бота к функции обращения к серверу для получения списка фильмов.
    """
    genre = message.text.strip()
    genres_list = site_api.get_genre_names()
    response_genres_list = genres_list(url=url, headers=headers)
    if response_genres_list == 504:
        bot.send_message(message.from_user.id,
                         "Возникла проблема на сервере.\n"
                         "Повторите запрос позже.\n"
                         "Вы возвращены в основное меню.")
        bot.delete_state(message.from_user.id)
        bot.set_state(message.from_user.id, MovieInfoState.menu, message.chat.id)
    else:
        response_genres_list = response_genres_list.json()
        genre_names_list = [el['name'].lower().strip() for el in response_genres_list]

        if genre.lower().strip() in genre_names_list:
            bot.set_state(message.from_user.id, MovieInfoState.movie_genre_and_year, message.chat.id)
            mess = f'<b>{message.from_user.first_name}</b>!\nВведите год создания фильма:'
            bot.send_message(message.from_user.id, mess, parse_mode='html')
            with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
                data['movie_genre'] = message.text
        else:
            bot.reply_to(message, 'Такого жанра нет! Выберите из существующих:')
            for genre_name in genre_names_list:
                bot.send_message(message.chat.id, genre_name)
            bot.set_state(message.from_user.id, MovieInfoState.movie_genre, message.chat.id)
