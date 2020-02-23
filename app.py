#!/usr/bin/python3

import pprint
import requests
from secrets.token import token

CURRENTLY_PLAYING_ENDPOINT = "https://api.spotify.com/v1/me/player/currently-playing?market=ES"

CURRENTLY_PLAYING_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format(token)
}


def get_current_song():

    r = requests.get(CURRENTLY_PLAYING_ENDPOINT, headers=CURRENTLY_PLAYING_HEADERS)

    status = r.status_code

    if status == 204:
        print('no track playing')

    elif status == 200:

        data = r.json()
        entry = {}

        entry['play_timestamp'] = data['timestamp']
        entry['duration_elapsed'] = data['progress_ms'] / data['item']['duration_ms']

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

        pprint.pprint(data)
        print('**********')
        print(entry)
    else:
        print('error requesting song')


if __name__ == '__main__':
    get_current_song()
