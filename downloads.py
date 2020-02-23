from os import mkdir
from os.path import dirname, exists, join, realpath

import hashlib

import requests


CURRENT_DIR = dirname(realpath(__file__))
CACHE_DIR = join(CURRENT_DIR, 'cache')

URL_PREFIX = 'https://heroeslounge.gg'


def get_html(path: str) -> str:
    cached_file_path = join(CACHE_DIR, hashlib.sha1(path.encode('utf8')).hexdigest())
    if exists(cached_file_path):
        with open(cached_file_path) as f:
            return f.read()

    response = requests.get(URL_PREFIX + path)
    html = response.content.decode('utf8')

    if not exists(CACHE_DIR):
        mkdir(CACHE_DIR)

    with open(cached_file_path, 'w') as f:
        f.write(html)

    return html
