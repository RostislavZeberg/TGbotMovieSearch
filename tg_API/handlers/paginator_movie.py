from telebot.types import CallbackQuery

from database.core import movie_facade
from main import user_facade
from tg_API.core import bot
from tg_API.states.movie_info import MovieInfoState
from tg_API.utils.send_film_page import send_film_page


@bot.callback_query_handler(state=MovieInfoState.paginator_movie)
def handler_pagination(call_button: CallbackQuery):
    """
    Функция запускает функцию для создания данных страницы пагинатора и для запуска пагинатора.
    В случае закрытия пагинатора переводит бот в состояние menu и сохраняет просмотренные фильмы в базу данных.
    """
    if call_button.data == "close paginator":
        bot.delete_message(call_button.message.chat.id, call_button.message.message_id)
        bot.send_message(call_button.from_user.id, "Можете вернуться к основному меню в панели.")
        user_name = call_button.from_user.username
        user_telegram_id = call_button.from_user.id
        user_facade.add(name=user_name, telegram_id=user_telegram_id)
        with bot.retrieve_data(call_button.from_user.id) as data:
            movies = data['history_watched_movies']
        user = user_facade.get_by_telegram_id(user_telegram_id)
        for movie in movies:
            movie_facade.add(movie_name=movie['movie_name'],
                             movie_year=movie['movie_year'],
                             movie_genres=movie['movie_genres'],
                             rating=movie['rating'],
                             user=user)
        bot.delete_state(call_button.from_user.id)
        bot.set_state(call_button.from_user.id, MovieInfoState.menu, call_button.message.chat.id)
        return
    current_page = call_button.data.split("#")[1]
    bot.delete_message(call_button.message.chat.id, call_button.message.message_id)
    send_film_page(call_button.from_user.id, int(current_page))
