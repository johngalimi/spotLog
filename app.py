#!/usr/bin/python3

import requests
from secrets.token import token

endpoint = "https://api.spotify.com/v1/me/player/currently-playing?market=ES"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(token)
}

r = requests.get(endpoint,headers=headers)

if r.status_code == 204:
    print('no track playing')
else:
    print(r.json())
