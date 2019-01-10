import requests
import json
from config import *


LOGIN_URI = '/sessions'
LOGIN_CREDS = {"email": "olga.nezhuta.cr@gmail.com", "password": "Qwerty1"}
LOGOUT_URI = '/sessions'


def login(creds):
    url = BASE_URL + LOGIN_URI
    r = requests.post(url, data=json.dumps(creds), headers=BASE_HEADERS)
    assert r.status_code == LOGIN_SUCCESS_STATUS_CODE
    my_token = r.json()['data']['session']['accessToken']
    return 'Bearer {}'.format(my_token)


def logout(token):
    url = BASE_URL + LOGOUT_URI
    headers = BASE_HEADERS
    headers.update({'Authorization': token})
    print(headers)
    r = requests.delete(url, headers=headers)
    print(r.status_code)
    assert r.status_code == LOGOUT_SUCCESS_STATUS_CODE







