# Heroes Lounge analyzer

Python tool for analyzing compositions of teams in [Heroes Lounge](https://heroeslounge.gg/).


## Example

```
cat main.py
```

```python
from api import *

games = list(get_games(division='s', season=2, team_name='The Vikings'))
print_compositions(games)
```

```
python main.py
```

```
The Vikings, compositions after 22 games

4 heroes picked together:

- Auriel + Leoric + Tyrael + Valla: 100% (2/2)
- Chromie + E.T.C. + Malfurion + Rexxar: 100% (2/2)
- Hanzo + Johanna + Malfurion + Rexxar: 50% (1/2)

3 heroes picked together:

- Ana + Chen + Li-Ming: 100% (2/2)
- Ana + E.T.C. + Falstad: 50% (1/2)
- Ana + E.T.C. + Jaina: 50% (1/2)
- Ana + E.T.C. + Li-Ming: 50% (1/2)
- Auriel + Leoric + Tyrael: 100% (2/2)
- Auriel + Leoric + Valla: 100% (2/2)
- Auriel + Tyrael + Valla: 100% (2/2)
- Chen + Malfurion + Tyrael: 0% (0/2)
- Chromie + E.T.C. + Malfurion: 100% (2/2)
- Chromie + E.T.C. + Rexxar: 100% (2/2)
- Chromie + Malfurion + Rexxar: 100% (2/2)
- E.T.C. + Malfurion + Rexxar: 100% (2/2)
- Hanzo + Johanna + Malfurion: 50% (1/2)
- Hanzo + Johanna + Rexxar: 50% (1/2)
- Hanzo + Malfurion + Rexxar: 50% (1/2)
- Johanna + Malfurion + Rexxar: 50% (1/2)
- Leoric + Tyrael + Valla: 100% (2/2)
- Li-Ming + Malfurion + Thrall: 0% (0/2)

2 heroes picked together:

- Ana + E.T.C.: 50% (2/4)
- Malfurion + Rexxar: 75% (3/4)
- Ana + Li-Ming: 67% (2/3)
- Auriel + Leoric: 100% (3/3)
- Auriel + Valla: 67% (2/3)
- Chen + Li-Ming: 67% (2/3)
- E.T.C. + Rexxar: 67% (2/3)
- Hanzo + Malfurion: 33% (1/3)
- Johanna + Rexxar: 33% (1/3)
- Malfurion + Tyrael: 0% (0/3)
- Ana + Chen: 100% (2/2)
- Ana + Falstad: 50% (1/2)
- Ana + Jaina: 50% (1/2)
- Auriel + Tyrael: 100% (2/2)
- Chen + Malfurion: 0% (0/2)
- Chen + Tyrael: 0% (0/2)
- Chromie + E.T.C.: 100% (2/2)
- Chromie + Malfurion: 100% (2/2)
- Chromie + Rexxar: 100% (2/2)
- E.T.C. + Falstad: 50% (1/2)
- E.T.C. + Jaina: 50% (1/2)
- E.T.C. + Li-Ming: 50% (1/2)
- E.T.C. + Malfurion: 100% (2/2)
- Falstad + Rexxar: 50% (1/2)
- Garrosh + Greymane: 50% (1/2)
- Gul'dan + Johanna: 50% (1/2)
- Gul'dan + Leoric: 100% (2/2)
- Gul'dan + Malfurion: 0% (0/2)
- Hanzo + Johanna: 50% (1/2)
- Hanzo + Rexxar: 50% (1/2)
- Johanna + Malfurion: 50% (1/2)
- Junkrat + Rehgar: 50% (1/2)
- Junkrat + Tyrael: 100% (2/2)
- Leoric + Tyrael: 100% (2/2)
- Leoric + Valla: 100% (2/2)
- Li-Ming + Mal'Ganis: 50% (1/2)
- Li-Ming + Malfurion: 0% (0/2)
- Li-Ming + Thrall: 0% (0/2)
- Mal'Ganis + Malthael: 0% (0/2)
- Mal'Ganis + Rehgar: 0% (0/2)
- Malfurion + Mephisto: 50% (1/2)
- Malfurion + Thrall: 0% (0/2)
- Tyrael + Uther: 50% (1/2)
- Tyrael + Valla: 100% (2/2)
```


## Installation

- Install [`pyenv`](https://github.com/pyenv/pyenv).
- Install [`pyenv-virtualenv`](https://github.com/pyenv/pyenv-virtualenv).

```
pyenv install 3.8.1
pyenv virtualenv analyzer
pyenv activate analyzer
pip install -r requirements.txt
```
