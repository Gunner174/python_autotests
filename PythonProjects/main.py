import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3577291f143d8025ae96e0a332f1c09d'
HEADER = {'Content-Type' : 'application/json', "trainer_token": TOKEN}
body_createPOKE = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_changename = {
    "pokemon_id": "317393",
    "name": "Не Бульбозавр",
    "photo_id": 1
}

body_catch = {
    "pokemon_id": "317393"
}


'''responce_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_createPOKE)
print(responce_create.json)

pokemon_id = responce_create.json()['id']
print(pokemon_id)

responce_changename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_changename)
print(responce_changename.json)

responce_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(responce_catch.json)'''

