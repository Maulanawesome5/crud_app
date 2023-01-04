import requests


try:
    input_judul = input("Cari judul anime: ")
    url = f"https://api.jikan.moe/v4/anime?q={input_judul}&sfw"
    data = requests.get(url)
    result = data.json()

    if data.status_code == 200:
        print(result)

    # print(type(data.status_code)) # 200 int

except:
    print(f"{input_judul} tidak ditemukan")
