from typing import List, Dict

from telegram_bot_pagination import InlineKeyboardPaginator, InlineKeyboardButton


def create_paginator(films: List[Dict], page: int) -> InlineKeyboardPaginator:
    """
    Функция создаёт пагинатор и кнопку для его закрытия.
    :param films: список полученных фильмов.
    :param page: номер страницы отображаемой в пагинаторе.
    :return: InlineKeyboardPaginator - пагинатор.
    """
    paginator = InlineKeyboardPaginator(
        len(films),
        current_page=page,
        data_pattern="movie#{page}")
    paginator.add_after(InlineKeyboardButton('Закрыть пагинатор', callback_data='close paginator'))
    return paginator
