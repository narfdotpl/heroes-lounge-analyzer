from dataclasses import dataclass
from typing import List


@dataclass
class Player:
    name: str
    hero: str


@dataclass
class Team:
    name: str
    players: List[Player]


@dataclass
class Game:
    blue_team: Team
    red_team: Team
    winner: Team
    map: str


@dataclass
class FocusedGame:
    team: Team
    enemies: Team
    did_win: bool
    map: str


@dataclass
class Match:
    url: str
    team1_name: str
    team2_name: str
    games: List[Game]


class WinRate:
    def __init__(self, wins, total):
        self.wins = wins
        self.total = total

        if total == 0:
            self.percentage = 0.0
        else:
            self.percentage = float(wins) / total

    @property
    def percentage_text(self):
        return str(int(round(100 * self.percentage))) + "%"

    @property
    def loses(self):
        return self.total - self.wins

    @property
    def diff(self):
        return self.wins - self.loses

    @property
    def diff_sign(self):
        diff = self.diff
        if diff < 0:
            return "-"
        elif diff == 0:
            return ""
        else:
            return "+"

    def __str__(self):
        return '{} ({}/{})'.format(self.percentage_text, self.wins, self.total)
