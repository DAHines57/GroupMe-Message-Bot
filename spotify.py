import sys
import random
from pytz import timezone
from datetime import datetime
import pytz
from libs import post_text
import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

'''
sadness_texts = [line.strip() for line in open('list of saddness.txt')]
central = timezone('US/Central')
now = datetime.now(tz=pytz.utc)
'''

username = os.environ.get("USERNAME")
client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

if request.args.get('spotify', '') != '':
    sp.user_playlist(username, request.args.get('spotify', ''), 'tracks, next')
    tracks = results['tracks']
    all_tracks = tracks['items']
    while tracks['next']:
        tracks = spotify.next('tracks')
        all_tracks += tracks['items']

    random_track = random.choice(all_tracks)
    post_text(random_track['name'] + ' - ' + track['artists'][0]['name'], sys.argv[1])
