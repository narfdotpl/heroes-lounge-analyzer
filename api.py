from collections import defaultdict
from itertools import combinations
from typing import Iterator, List, Set, Union

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


def print_compositions(games: List[FocusedGame]):
    print(f'{games[0].team.name}, compositions after {len(games)} games\n')

    def get_heroes(game: FocusedGame) -> Set[str]:
        return {p.hero for p in game.team.players}

    d = defaultdict(lambda: defaultdict(list))

    for (g1, g2) in combinations(games, 2):
        common_heroes = get_heroes(g1) & get_heroes(g2)
        for count in range(2, len(common_heroes) + 1):
            for heroes in combinations(common_heroes, count):
                key = ' + '.join(sorted(heroes))
                games = d[count][key]

                for g in [g1, g2]:
                    if g not in games:
                        games.append(g)

    for count in reversed(sorted(d.keys())):
        games_by_key = d[count]
        print(f'{count} heroes picked together:\n')
        for (key, games) in sorted(games_by_key.items(), key=lambda t: (-len(t[1]), t[0])):
            win_rate = WinRate(wins=len([g for g in games if g.did_win]), total=len(games))
            print(f'- {key}: {win_rate}')
        print()
