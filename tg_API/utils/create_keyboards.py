from telebot import types
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


def keyboards_send_welcome() -> ReplyKeyboardMarkup:
    """
    Функция создаёт клавиатуру в панели бота с основными действиями.
    :return: ReplyKeyboardMarkup - клавиатура в панели бота с основными действиями
    """
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_name_movie = types.KeyboardButton(text='Выбрать фильм по названию')
    button_year_genre = types.KeyboardButton(text='Выбрать фильм по жанру и году выпуска')
    button_history = types.KeyboardButton(text='История запросов')
    button_help = types.KeyboardButton(text='Помощь')
    keyboard.row(button_name_movie)
    keyboard.row(button_year_genre)
    keyboard.add(button_history, button_help)
    return keyboard


def keyboards_paginator_history_show():
    """
    Функция создаёт клавиатуру, которая привязана к сообщению для выбора соответствующего действия.
    :return: InlineKeyboardMarkup - клавиатура, которая привязана к сообщению.
    """
    keyboard = InlineKeyboardMarkup()
    buttons = [InlineKeyboardButton("Показать историю", callback_data="показать"),
               InlineKeyboardButton("Очистить историю", callback_data="очистить"), ]
    keyboard.add(*buttons)
    return keyboard


def keyboards_paginator_show():
    """
    Функция создаёт клавиатуру, которая привязана к сообщению для выбора соответствующего действия.
    :return: InlineKeyboardMarkup - клавиатура, которая привязана к сообщению.
    """
    keyboard = InlineKeyboardMarkup()
    buttons = [InlineKeyboardButton("Да", callback_data="да"),
               InlineKeyboardButton("нет", callback_data="нет"), ]
    keyboard.add(*buttons)
    return keyboard
