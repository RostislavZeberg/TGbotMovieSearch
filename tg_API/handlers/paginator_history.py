from telebot.types import CallbackQuery

from tg_API.core import bot
from tg_API.states.movie_info import MovieInfoState
from tg_API.utils.send_history_page import send_history_page


@bot.callback_query_handler(state=MovieInfoState.paginator_history)
def handle_pagination(call_button: CallbackQuery):
    """
    Функция запускает функцию для создания данных страницы пагинатора и для запуска пагинатора.
    В случае закрытия пагинатора переводит бот в состояние menu.
    """
    if call_button.data == "close paginator":
        bot.delete_message(call_button.message.chat.id, call_button.message.message_id)
        bot.send_message(call_button.from_user.id, "Можете вернуться к основному меню в панели.")
        bot.delete_state(call_button.from_user.id)
        bot.set_state(call_button.from_user.id, MovieInfoState.menu, call_button.message.chat.id)
        return
    current_page = call_button.data.split("#")[1]
    bot.delete_message(call_button.message.chat.id, call_button.message.message_id)
    send_history_page(user_id=call_button.from_user.id, chat_id=call_button.message.chat.id, page=int(current_page))
