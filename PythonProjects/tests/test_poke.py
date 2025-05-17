import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3577291f143d8025ae96e0a332f1c09d'
HEADER = {'Content-Type' : 'application/json', "trainer_token": TOKEN}
TRAINER_ID = 38095

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_id():
    responce_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert responce_get.json()['data'][0]['trainer_name'] == 'QAEngineer'