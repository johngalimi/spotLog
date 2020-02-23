#!/usr/bin/python3

import pprint
import requests
from secrets.token import token

endpoint = "https://api.spotify.com/v1/me/player/currently-playing?market=ES"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(token)
}

r = requests.get(endpoint, headers=headers)

status = r.status_code

if status == 204:
    print('no track playing')

elif status == 200:

    data = r.json()
    entry = {}

    entry['album_id'] = data['item']['album']['id']
    entry['album_name'] = data['item']['album']['name']
 
    artists = data['item']['artists']
    primary_artist = artists.pop(0)

    features = '/'.join([artist['name'] for artist in artists])
    
    entry['artist_id'] = primary_artist['id']
    entry['artist_name'] = primary_artist['name']

    entry['features'] = features
   
    entry['song_id'] = data['item']['id']
    entry['song_name'] = data['item']['name']

    print(entry)
else:
    print('error requesting song')
