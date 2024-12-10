from telebot.types import CallbackQuery

from database.core import user_facade
from tg_API.core import bot
from tg_API.states.movie_info import MovieInfoState
from tg_API.utils.send_history_page import send_history_page


@bot.callback_query_handler(state=MovieInfoState.start_paginator_history)
def start_paginator_history(call_button: CallbackQuery) -> None:
    """
    Функция при соответствующем выборе, либо запускает функцию для формирования данных для пагинатора и переводе
    бота в состояние запуска пагинатора, либо очищает историю просмотренных фильмов и переводит бот в состояние menu.
    """
    bot.delete_message(call_button.message.chat.id, call_button.message.message_id)
    if call_button.data == "показать":
        bot.set_state(call_button.from_user.id, MovieInfoState.paginator_history, call_button.message.chat.id)
        send_history_page(user_id=call_button.from_user.id, chat_id=call_button.message.chat.id)
    else:
        user_facade.delete(call_button.from_user.id)
        bot.send_message(call_button.from_user.id,
                         "История просмотренных фильмов очищена.\n"
                         "Можете вернуться к основному меню в панели.")
        bot.delete_state(call_button.from_user.id)
        bot.set_state(call_button.from_user.id, MovieInfoState.menu, call_button.message.chat.id)

