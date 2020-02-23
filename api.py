from collections import defaultdict
from typing import Iterator, List, Union

from downloads import get_matches
from models import FocusedGame, WinRate


def get_games(team_name: str, *, region='eu', season=11, division: Union[int, str] = 4) -> Iterator[FocusedGame]:
    for match in get_matches(region=region, season=season, division=division, team_name=team_name):
        for game in match.games:
            is_blue = game.blue_team.name == team_name
            yield FocusedGame(
                team=game.blue_team if is_blue else game.red_team,
                enemies=game.red_team if is_blue else game.blue_team,
                did_win=game.winner.name == team_name,
                map=game.map,
            )


def print_popular_heroes(games: List[FocusedGame]):
    games_by_hero = defaultdict(list)
    for game in games:
        for player in game.team.players:
            games_by_hero[player.hero].append(game)

    print('Popular picks:\n')
    for (hero, games) in sorted(games_by_hero.items(), key=lambda t: (-len(t[1]), t[0])):
        win_rate = WinRate(wins=len([g for g in games if g.did_win]), total=len(games))
        print(f'- {hero}: {win_rate}')
