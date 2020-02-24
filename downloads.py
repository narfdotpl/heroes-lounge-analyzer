from dataclasses import dataclass
from os import mkdir
from os.path import dirname, exists, join, realpath
from typing import Iterator, List, Optional, Union

import hashlib

import requests
import lxml.html

from models import Match, Game, Team, Player


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
    if response.status_code != 200:
        raise Exception(f'status code = {response.status_code}')

    html = response.content.decode('utf8')

    if not exists(CACHE_DIR):
        mkdir(CACHE_DIR)

    with open(cached_file_path, 'w') as f:
        f.write(html)

    return html


def p(el):
    print(lxml.html.tostring(el))


def get_match_links(*, region: str, season: int, division: Union[int, str]) -> Iterator[MatchLink]:
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


def get_matches(*, region: str, season: int, division: Union[int, str], team_name: str) -> Iterator[Match]:
    links = get_match_links(region=region, season=season, division=division)
    for link in links:
        if team_name in {link.team1_name, link.team2_name}:
            match = get_match(link.url)
            if match:
                yield match


def parse_players(el) -> Iterator[Player]:
    for figure in el.cssselect('figure'):
        yield Player(
            name=figure.cssselect('figcaption')[0].attrib['title'],
            hero=figure.cssselect('img')[0].attrib['title'],
        )


def get_match(url: str) -> Optional[Match]:
    path = url[len(URL_PREFIX):]
    html = get_html(path)
    doc = lxml.html.fromstring(html)

    games = []
    for pane in doc.cssselect('.tab-pane'):
        rows = pane.cssselect('.row')
        if not rows:
            return None

        (blue_team_name, red_team_name) = [el.text.strip() for el in rows[0].cssselect('h3 a')]
        (blue_team_players, red_team_players) = [parse_players(el) for el in rows[2].cssselect('.col')]
        blue_team = Team(name=blue_team_name, players=list(blue_team_players))
        red_team = Team(name=red_team_name, players=list(red_team_players))

        map = rows[4].cssselect('.badge-info')[0].text.strip()
        level_winner_columns = rows[5].cssselect('.col-6')[-2:]
        did_blue_team_win = len(level_winner_columns[0].cssselect('.badge-success')) == 1

        games.append(Game(
            blue_team=blue_team,
            red_team=red_team,
            winner=blue_team if did_blue_team_win else red_team,
            map=map,
        ))

    if games:
        return Match(
            url=url,
            team1_name=games[0].blue_team.name,
            team2_name=games[0].red_team.name,
            games=games,
        )
    else:
        return None
