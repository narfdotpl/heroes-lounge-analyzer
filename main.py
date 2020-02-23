from api import *


games = list(get_games('Munchies'))
# print_popular_heroes(games)
print_compositions(games)
