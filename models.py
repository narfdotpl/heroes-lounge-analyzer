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
class Match:
    url: str
    team1_name: str
    team2_name: str
    games: List[Game]
