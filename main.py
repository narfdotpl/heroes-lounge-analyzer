from downloads import get_match_links

links = get_match_links(region='eu', season=11, division=4)
print(next(links))
