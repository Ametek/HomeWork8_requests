import requests

superhero = ['Hulk', 'Captain America', 'Thanos']
url = 'https://akabab.github.io/superhero-api/api/'
superhero_info = {}
all_superhero = requests.get(url + '/all.json').json()
# from pprint import pprint
# pprint(all_superhero)
for superhero_list in all_superhero:
    if superhero_list['name'] in superhero:
        superhero_info[superhero_list['name']] = superhero_list['powerstats']['intelligence']
smartest_hero = max(superhero_info, key=superhero_info.get)
print(f'Самый умный: {smartest_hero}')