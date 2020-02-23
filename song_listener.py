#!/usr/bin/python3

import time

from flask import Flask, request
from song_fetcher import SongFetcher

app = Flask(__name__)


@app.route('/listen')
def listen():

    time_parameters = request.args

    fetcher = SongFetcher()

    songs = []
    
    for i in range(int(time_parameters['duration'])):
        
        songs.append(fetcher.get_current_song())
        time.sleep(int(time_parameters['sleep']))
    
    return {'played': songs}


if __name__ == '__main__':
    app.run(debug = True)
