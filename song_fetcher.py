#!/usr/bin/python3

import pprint
import requests
from secrets.token import token

class SongFetcher:
    def __init__(self):
        self.CURRENTLY_PLAYING_ENDPOINT = "https://api.spotify.com/v1/me/player/currently-playing?market=ES"
        self.CURRENTLY_PLAYING_HEADERS = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(token)
        }


    def get_current_song(self):

        r = requests.get(self.CURRENTLY_PLAYING_ENDPOINT, headers=self.CURRENTLY_PLAYING_HEADERS)

        status = r.status_code

        entry = {}

        if status == 204:
            entry['message'] = 'Sorry, nothing is playing'

        elif status == 200:

            data = r.json()

            entry['play_timestamp'] = data['timestamp']
            entry['duration_elapsed'] = round(data['progress_ms'] / data['item']['duration_ms'], 2)

            entry['album_id'] = data['item']['album']['id']
            entry['album_name'] = data['item']['album']['name']

            artists = data['item']['artists']
            primary_artist = artists.pop(0)

            features = '/'.join([artist['name'] for artist in artists])
    
            entry['artist_id'] = primary_artist['id']
            entry['artist_name'] = primary_artist['name']

            entry['artist_features'] = features
   
            entry['song_id'] = data['item']['id']
            entry['song_name'] = data['item']['name']

        else:
            entry['message'] = 'Sorry, there was an error in the request'

        return entry

