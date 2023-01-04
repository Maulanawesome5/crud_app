import requests


# keyboard copy g, G, h, H, '_', "_"

# Menampilkan daftar anime paling top
# Query Parameter : type, filter, page, limit
# type -> "tv" "movie" "ova" "special" "ona" "music"
# filter -> "airing" "upcoming" "bypopularity" "favorite"
# page -> int 0...
# limit -> int 0...

# example complete url param
# https://api.jikan.moe/v4/top/anime?type=tv,movie,ova,special,ona&filter=airing,upcoming,bypopularity,favorite&page=5&limit=30

# # Cari serial anime (tv) terpopuler
# url = "https://api.jikan.moe/v4/top/anime?type=tv&filter=airing&page=1&limit=10"
url = "https://api.jikan.moe/v4/top/anime?type=tv&filter=favorite&page=1&limit=10"
data = requests.get(url) # return status code 200
anime = data.json()

# print(len(anime['data'])) # Terdapat 10 data dalam list
# print(anime['data'][0]) # anime Full Metal Alchemist B
# print(anime['data'][1]) # anime Hunter x Hunter 2011
# print(anime['data'][2]) # anime One Piece

# print(anime['data'][0]['mal_id']) # FMAB MAL id = 5114
# print(anime['data'][1]['mal_id']) # Golden Kamuy MAL id = 11061

# print(anime['data'][0]['images']['jpg']['image_url']) # anime images JPG

# print(anime['data'][0]['score']) # score anime

# print(anime['data'][4]['titles'][0]['title']) # judul utama
# print(anime['data'][4]['titles'][2]['title']) # judul dalam kanji jepang

# print(anime['data'][0]['season']) # season release
# print(anime['data'][0]['year']) # year release

# # Get data studio produksi anime
# # Biasanya dalam suatu anime, studio yang memproduksi bisa 
# lebih dari satu. Dalam API, akan berupa tipe data list dictionary
print(anime['data'][0]['studios'][0]['name']) # nama studio
print(anime['data'][0]['studios'][0]['url']) # link studio to MAL Site
