from telebot.types import Message

from tg_API.core import bot
from tg_API.states.movie_info import MovieInfoState
from tg_API.utils.create_keyboards import keyboards_paginator_history_show


@bot.message_handler(state=MovieInfoState.menu)
def on_click(message: Message) -> None:
    """
    Функция определяющая ответы бота при выборе команды из меню панели бота, запускает соответствующие функции
    и переводит бот в соответствующее состояние.
    """
    if message.text == 'Выбрать фильм по названию':
        bot.set_state(message.from_user.id, MovieInfoState.movie_name, message.chat.id)
        mess = f'<b>{message.from_user.first_name}</b>!\nВведите название фильма:'
        bot.send_message(message.from_user.id, mess, parse_mode='html')
    elif message.text == 'Выбрать фильм по жанру и году выпуска':
        bot.set_state(message.from_user.id, MovieInfoState.movie_genre, message.chat.id)
        mess = f'<b>{message.from_user.first_name}</b>!\nВведите название жанра:'
        bot.send_message(message.from_user.id, mess, parse_mode='html')
    elif message.text == 'Помощь':
        mess = f'<b>{message.from_user.first_name}</b>!\n' \
               f'Я расскажу вам про мои основные команды:\n' \
               f'- /start - перезапуск бота;\n'\
               f'- /help - помощь в навигации по боту;\n' \
               f'- "Выбрать фильм по названию" - введите название искомого фильма;\n' \
               f'- "Выбрать фильм по жанру и году выпуска" - введите сначала название фильма, затем год создания;\n' \
               f'- "История запросов" - можете узнать, какие фильмы были вами найдены.'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        bot.set_state(message.from_user.id, MovieInfoState.menu, message.chat.id)
    elif message.text == 'История запросов':
        mess = f'<b>{message.from_user.first_name}</b>!\nВы перешли в меню управления историей'
        bot.send_message(message.chat.id, mess, parse_mode='html')
        keyboard = keyboards_paginator_history_show()
        bot.send_message(message.from_user.id, "Что вы хотите предпринять?", reply_markup=keyboard)
        bot.set_state(message.from_user.id, MovieInfoState.start_paginator_history, message.chat.id)
    else:
        bot.send_message(message.chat.id, 'Пожалуйста выберите команду из списка ниже:')
        bot.set_state(message.from_user.id, MovieInfoState.menu, message.chat.id)
