# rest api
# GET: Pobiera dane z serwera (np. listę produktów).
# POST: Tworzy nowy zasób na serwerze (np. dodaje nowego użytkownika).
# PUT / PATCH: Aktualizuje istniejące dane (PUT zastępuje całość, PATCH tylko wskazany fragment)
# DELETE: Usuwa wskazany zasób z serwera.

# klient http httpx, niquests
import requests

# pip install requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
print(response)  # <Response [200]>
# 2xx ok
# 3xx warningi, przekierowanie
# 4xx 404 - brak strony, 400 Bad request
# 5xx błedy po stronie serwera

print(response.text)

data = response.json()
print(data)

print("Kawał:", data['value'])

icon_url = data['icon_url']
print(icon_url)

response_img = requests.get(icon_url)
with open('icon.png', "wb") as f:
    f.write(response_img.content)
