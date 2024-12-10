from telebot import types
from telebot.types import Message

from tg_API.core import bot
from tg_API.states.movie_info import MovieInfoState


@bot.message_handler(commands=["help"])
def send_help(message: Message) -> None:
    """
    Функция определяющая ответ бота при введении команды help
    """
    mess = f'Здравствуйте <b>{message.from_user.first_name}!</b>\n' \
           'Выберите команду из списка ниже\n' \
           'Следуйте инструкции'
    bot.send_message(message.chat.id, mess, parse_mode='html')
    bot.set_state(message.from_user.id, MovieInfoState.menu, message.chat.id)

