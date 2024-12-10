from telebot.types import Message

from tg_API.core import bot
from tg_API.states.movie_info import MovieInfoState
from tg_API.utils.create_keyboards import keyboards_send_welcome


@bot.message_handler(commands=["start"])
def send_welcome(message: Message) -> None:
    """
    Функция при получении команды start выводит клавиатуру в панели бота с основными действиями.
    Переводит бот в состояние menu.
    """
    keyboard = keyboards_send_welcome()
    mess = f'Привет, <b>{message.from_user.first_name}</b>!\nМы поможем вам в выборе фильма!\n' \
           f'Для получения информации по командам кликните /help или введите в сообщение эту команду'
    bot.send_message(message.chat.id, mess, reply_markup=keyboard, parse_mode='html')
    bot.set_state(message.from_user.id, MovieInfoState.menu, message.chat.id)
