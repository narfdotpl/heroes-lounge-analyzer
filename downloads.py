from dataclasses import dataclass
from os import mkdir
from os.path import dirname, exists, join, realpath
from typing import Iterator, List, Union

import hashlib

import requests
import lxml.html


CURRENT_DIR = dirname(realpath(__file__))
CACHE_DIR = join(CURRENT_DIR, 'cache')

URL_PREFIX = 'https://heroeslounge.gg'


@dataclass
class MatchLink:
    url: str
    team1_name: str
    team2_name: str


def get_html(path: str) -> str:
    cached_file_path = join(CACHE_DIR, hashlib.sha1(path.encode('utf8')).hexdigest())
    if exists(cached_file_path):
        with open(cached_file_path) as f:
            return f.read()

    response = requests.get(URL_PREFIX + path)
    print(response.status_code)
    html = response.content.decode('utf8')

    if not exists(CACHE_DIR):
        mkdir(CACHE_DIR)

    with open(cached_file_path, 'w') as f:
        f.write(html)

    return html


def p(el):
    print(lxml.html.tostring(el))


def get_match_links(region: str, season: int, division: Union[int, str]) -> Iterator[MatchLink]:
    if division == 's':
        path = f'/{region}-division-s-season-{season}/{region}-division-s-season-{season}'
    else:
        path = f'/{region}season-{season}/division-{division}'

    html = get_html(path)
    doc = lxml.html.fromstring(html)
    links = doc.cssselect('.card a:contains("VS")')

    for link in links:
        url = link.attrib['href']
        row = link.getparent().getparent()
        team_links = row.cssselect('a[href*="/team/view"]')
        team_names = [el.text for el in team_links]
        yield MatchLink(url, *team_names)
