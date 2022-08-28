import requests

superhero = ['Hulk', 'Captain America', 'Thanos']
url = 'https://akabab.github.io/superhero-api/api/'
superhero_info = {}
all_superhero = requests.get(url + '/all.json').json()
from pprint import pprint
pprint(all_superhero)