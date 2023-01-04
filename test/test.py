import requests


url = "https://api.jikan.moe/v4/anime/22199/full"
data = requests.get(url) # return status code 200
anime = data.json()

# keyboard copy g, G, h, H, '_', "_"

# ambil data anime
# print(anime)
# print(anime['data']['mal_id']) # 22199
# print(anime['data']['url']) # https://myanimelist.net/anime/22199/Akame_ga_Kill
# print(anime['data']['images']['jpg']['image_url']) # https://cdn.myanimelist.net/images/anime/1429/95946.jpg
# print(anime['data']['score']) # 7.47
# print(anime['data']['titles'][0]['title']) # Akame ga Kill!
# print(anime['data']['titles'][2]['title']) # アカメが斬る！
# print(anime['data']['season']) # summer
# print(anime['data']['year']) # 2014

# ambil data studio produksi anime
# print(anime['data']['studios'][0]) # {'mal_id': 314, 'type': 'anime', 'name': 'White Fox', 'url': 'https://myanimelist.net/anime/producer/314/White_Fox'}
# print(anime['data']['studios'][0]['name']) # White Fox
# print(anime['data']['studios'][0]['url']) # https://myanimelist.net/anime/producer/314/White_Fox
