from downloads import get_matches

matches = get_matches(region='eu', season=11, division=4, team_name='Munchies')
for match in matches:
    print(match)
    print()
