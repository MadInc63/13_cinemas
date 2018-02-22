import requests
import argparse
from tqdm import tqdm
from tabulate import tabulate
from bs4 import BeautifulSoup


def parse_args():
    parser = argparse.ArgumentParser(description='Number of output films')
    parser.add_argument(
        '-count',
        default=10,
        type=int,
        help='enter number of output films')
    return parser.parse_args()


def fetch_page(url, params=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/64.0.3282.140 Safari/537.36',
        'Accept-Language': 'ru,en;q=0.9'
    }
    return requests.get(url, params=params, headers=headers)


def parse_afisha_list(raw_html):
    films_information = {}
    min_showing_cinemas_count = 50
    soup = BeautifulSoup(raw_html, 'html.parser')
    tags = soup.find_all(class_='m-disp-table')
    for tag in tags:
        film_title = tag.h3.string
        cinemas_count = len(
            tag.next_sibling.next_sibling.find_all(class_='b-td-item')
        )
        if min_showing_cinemas_count < cinemas_count:
            films_information[film_title] = cinemas_count
    return films_information


def fetch_movie_page(movie_title):
    url = 'https://www.kinopoisk.ru/index.php'
    params = {'kp_query': movie_title, 'first': 'yes', 'what': ''}
    response = fetch_page(url, params)
    return response


def parse_film_rating(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    try:
        rating = soup.find(class_='rating_ball').string
        rating_count = soup.find(
            class_='ratingCount'
        ).string.replace(u'\xa0', '')
    except AttributeError:
        rating = 0
        rating_count = 0
    return float(rating), int(rating_count)


def output_movies_to_console(movies_list, number_of_output_films):
    headers = ['Movie title', 'Rating', 'Rating count', 'Votes']
    print(tabulate(
        movies_list[:number_of_output_films], headers, tablefmt="psql"
    ))


if __name__ == '__main__':
    args = parse_args()
    afisha_page_url = 'https://www.afisha.ru/msk/schedule_cinema/'
    afisha_page_raw = fetch_page(afisha_page_url)
    print('Get a list of movies shown in the cinema from Afisha.ru...')
    showing_films = parse_afisha_list(afisha_page_raw.text)
    print('Get movies rating from Kinopoisk.ru...')
    movie_list_info = []
    for movie_name, votes in tqdm(
            showing_films.items(), desc='Collecting data:'
    ):
        movie_page = fetch_movie_page(movie_name)
        movie_rating, movie_rating_count = parse_film_rating(movie_page.text)
        movie_info = [movie_name, movie_rating, movie_rating_count, votes]
        movie_list_info.append(movie_info)
    sorted_movie_list = (sorted(
        movie_list_info, key=lambda movie: movie[1], reverse=True
    ))
    output_movies_to_console(sorted_movie_list, args.count)
