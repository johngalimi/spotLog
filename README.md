# spotLog

Real-time logging + analytics on your Spotify listening 

- activate venv + install dependencies: `source venv/bin/activate && pip3 install -r requirements.txt`
- run flask service on port 5000: `python3 song_listener.py`
- expose port via external tunnel: `./ngrok http 5000`
- make requests to listen endpoint and specify number of iterations/sleep length: `/listen?iterations2&sleep=1`
- on ios --> use shortcuts app to prompt automated request when spotify opens
