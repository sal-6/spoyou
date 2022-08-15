import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials
import json
import os
import pprint
import math

def set_creds(cred_file="./../creds/spotify_creds.json"):


    with open(cred_file) as fi:
        spot_ids = json.load(fi)
    
    os.environ["SPOTIPY_CLIENT_ID"] = spot_ids["client_id"]
    os.environ["SPOTIPY_CLIENT_SECRET"] = spot_ids["client_secret"]
    os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:8888/callback"


def get_user_liked_songs(limit=50, start_offset=0):
    scope = "user-library-read"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    tracks = []
    count = start_offset
    repeat = True
    while repeat:
        results = sp.current_user_saved_tracks(limit=limit, offset=count)
        for idx, item in enumerate(results['items']):
            track = item['track']
            tracks.append({"artist": track['artists'][0]['name'], "name": track['name']})
            #print(count + 1, track['artists'][0]['name'], " – ", track['name'])
            count += 1

        repeat = False
        if results["total"] > count:
            repeat = True

    return tracks

set_creds()