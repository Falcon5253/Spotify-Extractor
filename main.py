import spotipy
from spotipy.oauth2 import SpotifyOAuth

spotic = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="3cb1cea287e24d4395d6dfcc5bac9a93",
                                                client_secret="fac02fd8794044d6986e8ff0cc17d564",
                                                redirect_uri="http://localhost:8888/callback",
                                                scope="user-library-read user-top-read playlist-modify-private playlist-modify-public"))

name = spotic.current_user()['display_name']
print(name)
offset_var = 0
idx = 1
amount_of_tracks = input("Введите количество треков (не больше, чем у вас есть всего): ")

file1 = open('numbered_list.txt', 'w', encoding='utf-8')
file2 = open('list.txt', 'w', encoding='utf-8')
while(idx-1 < int(amount_of_tracks)):
    results = spotic.current_user_saved_tracks(limit=50, offset=offset_var)
    for item in results['items']:
        # Выбираем трек, выводим данные в консоль
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])
        # Записываем его параметры в нумерованный список
        text = str(idx) + " " + track['artists'][0]['name'] + " – " + track['name'] + "\n"
        file1.write(text)
        # Записываем его параметры в ненумерованный список
        text = track['artists'][0]['name'] + " – " + track['name'] + "\n"
        file2.write(text)
        # Увеличиваем счетчик
        idx += 1
    offset_var+=50

print("That's it!")

