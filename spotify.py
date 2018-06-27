import sys
import random
from pytz import timezone
import datetime
from datetime import datetime
import pytz
from libs import post_text
import spotipy
import os
import requests
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

username = os.environ.get("USERNAME")
client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
playlist_id = os.environ.get("SPOTIPY_PLAYLIST_ID")
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Post a random song from my main playlist
def post_rand_song(bot_id):
    print("Finding spotify song")
    results = sp.user_playlist(username, playlist_id, 'tracks,next')
    tracks = results['tracks']
    all_tracks = tracks['items']
    while tracks['next']:
        tracks = sp.next(tracks)
        all_tracks += tracks['items']

    random_track = random.choice(all_tracks)
    post_text(u'\U0001F3B5: ' + random_track['track']['name'] + ' - ' + random_track['track']['artists'][0]['name']
    + ' ' + random_track['track']['external_urls']['spotify'], bot_id)

def get_top_song(bot_id):
    print("Finding Dyl's top song")
    scope = 'user-top-read'
    username = os.environ.get("USERNAME")
    token = util.prompt_for_user_token(username, scope)
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        results = sp.current_user_top_tracks(time_range='short_term', limit=1)
        for i, item in enumerate(results['items']):
            print( i, item['name'], '//', item['artists'][0]['name'])
        print()

    else:
        print("Can't get token for", username)
