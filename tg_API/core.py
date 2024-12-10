import telebot
from telebot.storage import StateMemoryStorage
from telebot.types import BotCommand

from settings import site, DEFAULT_COMMANDS

storage = StateMemoryStorage()

bot = telebot.TeleBot(site.bot_token.get_secret_value(), state_storage=storage)


def set_default_commands(bot):
    """
    Функция запускает метод, который позволяет установить команды бота
    :param bot:
    :return:
    """
    bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )
