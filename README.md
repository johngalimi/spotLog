# spotLog

- activate venv + install dependencies: source venv/bin/activate && pip3 install -r requirements.txt
- run flask service on port 5000: ./song_listener
- expose port via external tunnel: ./ngrok http 5000
- make requests to /listen endpoint w/ proper query params
- on ios --> use shortcuts app to prompt automated request when spotify opens
