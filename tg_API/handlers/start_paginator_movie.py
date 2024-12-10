from telebot.types import CallbackQuery

from tg_API.core import bot
from tg_API.states.movie_info import MovieInfoState
from tg_API.utils.send_film_page import send_film_page


@bot.callback_query_handler(state=MovieInfoState.start_paginator_movie)
def start_paginator_movie(call_button: CallbackQuery) -> None:
    """
    Функция при соответствующем выборе, либо запускает функцию для формирования данных для пагинатора и переводе
    бота в состояние запуска пагинатора, либо закрывает меню выбора действий с пагинатором
    и переводит бот в состояние menu.
    """
    bot.delete_message(call_button.message.chat.id, call_button.message.message_id)
    if call_button.data == "да":
        bot.set_state(call_button.from_user.id, MovieInfoState.paginator_movie, call_button.message.chat.id)
        send_film_page(call_button.from_user.id)
    else:
        bot.send_message(call_button.from_user.id, "Можете вернуться к основному меню в панели.")
        bot.delete_state(call_button.from_user.id)
        bot.set_state(call_button.from_user.id, MovieInfoState.menu, call_button.message.chat.id)


@bot.message_handler(content_types=['text'])
def message_input_step(message) -> None:
    """
    Функция блокирует возможность ввода при открытом меню выбора действий с пагинатором или пагинаторе.
    """
    bot.reply_to(message, 'Для продолжения выберите действие в открывшемся меню,\n'
                          'если Пагинатор открыт закройте его')
