from telebot.custom_filters import StateFilter

from database.common.models import User, Movie
from database.utils.CRUD import DatabaseFacade
from tg_API.core import set_default_commands, bot

user_facade = DatabaseFacade(User)
movie_facade = DatabaseFacade(Movie)

print('перезагрузился')

if __name__ == "__main__":
    bot.add_custom_filter(StateFilter(bot))
    set_default_commands(bot)
    bot.infinity_polling()
