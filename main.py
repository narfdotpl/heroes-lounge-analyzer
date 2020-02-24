from api import *


games = list(get_games('Munchies'))
games = list(get_games('Massive Anger Disorder'))
# games = list(get_games(division='s', season=2, team_name='pepeMLADY'))
# games = list(get_games(division='s', season=2, team_name='Disgusting'))
# print_popular_heroes(games)
# print_compositions(games)

for team_name in [
    'Washed up',
    'The Vikings',
    'Laubers Fanclub',
    'Feel the Heat',
    'Crystal Gaming',
    'pepeMLADY',
    'Disgusting',
]:
    games = list(get_games(division='s', season=2, team_name=team_name))
    print_games_with_heroes(games, {'Valla', 'Malfurion'})

print('done')
