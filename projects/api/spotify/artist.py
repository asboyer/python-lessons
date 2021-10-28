import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

from secret import client_id, client_secret
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri = 'spotify:artist:3fMbdgg4jU18AjLCKBhRSm'

result = spotify.artist(uri)

with open("result.json", "w") as file:
    json.dump(result, file, indent=4)