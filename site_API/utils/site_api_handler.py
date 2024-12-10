from typing import Dict, Callable

import requests
from requests import Response


def _make_movie_response(url: str,
                         headers: Dict,
                         params: Dict,
                         success: int = 200,
                         mark: str = 'v1.4',
                         item: str = '', ) -> Response | int:
    """
    Функция создаёт URI обращения к серверу, для дальнейшего использования в других функциях

    :return: статус код ответа от сервера, если ответ success - ответ от сервера
    """
    url = '{0}/{1}/movie{2}'.format(url, mark, item)
    response = requests.get(
        url=url,
        headers=headers,
        params=params
    )
    status_code = response.status_code
    if status_code == success:
        return response
    return status_code


# https://api.kinopoisk.dev/v1/movie/possible-values-by-field?field=genres.name
def _get_genre_names(url: str, headers: Dict, func=_make_movie_response) -> Response:
    """
    Функция формирует запрос для получения списка жанров

    :return: ответ от сервера со списком жанров
    """
    params = {
        'field': 'genres.name'
    }

    response = func(url=url, headers=headers, params=params, mark='v1', item='/possible-values-by-field')
    return response


# https://api.kinopoisk.dev/v1.4/movie?page=1&limit=10&selectFields=&year=2012&genres.name=%D0%BA%D1%80%D0%B8%D0%BC%D0%B8%D0%BD%D0%B0%D0%BB"
# https://api.kinopoisk.dev/v1.4/movie?year=2023&genres.name=криминал
def _get_movie_by_year_and_genre(url: str,
                                 headers: Dict,
                                 year: str,
                                 genres_name: str,
                                 func=_make_movie_response) -> Response:
    """
    Функция формирует запрос для получения списка фильмов по жанру и году создания

    :return: ответ от сервера со списком фильмов
    """
    params = {
        'page': 1,
        'limit': 10,
        'selectFields': '',
        'year': year,
        'genres.name': genres_name,
    }
    response = func(url=url, headers=headers, params=params)
    return response


#  https://api.kinopoisk.dev/v1.4/movie/search?page=1&limit=10&query=1%2B1
def _get_movie_by_name(url: str, headers: Dict, movie_name: str, func=_make_movie_response) -> Response:
    """
    Функция формирует запрос для получения списка фильмов по названию

    :return: ответ от сервера со списком фильмов
    """
    name = movie_name
    params = {
        'page': 1,
        'limit': 10,
        'query': name

    }

    response = func(url=url, headers=headers, params=params, item='/search')
    return response


class SiteApiInterface:
    """
    Класс группирует функции обращения к серверу
    """

    @staticmethod
    def get_movie_by_year_and_genre() -> Callable[
            [str, dict, str, str, Callable[[str, dict, dict, int, str, str], Response | int]], Response]:
        return _get_movie_by_year_and_genre

    @staticmethod
    def get_movie_by_name() -> Callable[
            [str, dict, str, Callable[[str, dict, dict, int, str, str], Response | int]], Response]:
        return _get_movie_by_name

    @staticmethod
    def get_genre_names() -> Callable[
            [str, dict, Callable[[str, dict, dict, int, str, str], Response | int]], Response]:
        return _get_genre_names


if __name__ == '__main__':
    # _make_movie_response()
    # _get_movie_by_year_and_genre()
    # _get_movie_by_name()
    # _get_genre_names()

    SiteApiInterface()
