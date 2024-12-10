from typing import List, Dict

import requests

from tg_API.core import bot


def search_movie(message, movies: List[Dict]) -> List[dict]:
    """
    Функция проверяет полученный список словарей фильмов по заданным критериям, формирует список словарей фильмов
    и сохраняет его в базу данных бота. Создаёт в базе данных бота пустой список просмотренных фильмов.
    :param message: аргумент телеграмм бота - словарь данных.
    :param movies: список словарей фильмов.
    :return: список с отсортированными словарями полученных фильмов.
    """
    movies_data: List = []

    for movie in movies:
        movie_dict = {}
        name_genres = []
        for el in movie['genres']:
            name_genres.append(el['name'])
        if 'poster' in movie.keys() and movie['poster']['url'] is not None \
                and 'name' in movie.keys() and movie['name'] is not None and movie['name'] != '':
            response: requests.Response = requests.get(movie['poster']['url'])
            if int(response.headers['Content-Length']) < 3000000:
                movie_dict = {
                    'poster_url': movie['poster']['url'],
                    'movie_name': movie['name'],
                    'movie_year': movie['year'],
                    'movie_genres': ", ".join(name_genres),
                    'description': movie['description'],
                    'rating': movie['rating']['filmCritics'],
                    'ageRating': movie['ageRating']
                }
                movies_data.append(movie_dict)
        elif movie['name'] == '' or movie['name'] is None:
            movie_dict = {
                'poster_url': 'Постер отсутствует',
                'movie_name': movie['alternativeName'],
                'movie_year': movie['year'],
                'movie_genres': ", ".join(name_genres),
                'description': movie['description'],
                'rating': movie['rating']['filmCritics'],
                'ageRating': movie['ageRating']
            }
            movies_data.append(movie_dict)
        if 'description' in movie_dict and (movie['description'] is None or movie['description'] == ''):
            movie_dict['description'] = 'Описание отсутствует'
        if 'ageRating' in movie_dict and (movie['ageRating'] is None or movie['ageRating'] == ''):
            movie_dict['ageRating'] = 'Отсутствует'

    for item in movies_data:
        for key in item:
            if item[key] is None:
                item[key] = ' '

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['movie_data']: List[Dict] = movies_data
        data['history_watched_movies']: List[Dict] = []

    return movies_data
