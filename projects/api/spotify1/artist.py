import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

from secret import client_id, client_secret
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# universal resource indentifer
uri = 'spotify:artist:3TVXtAsR1Inumwj472S9r4'

result = sp.artist(uri)

with open("result.json", "w") as file:
    json.dump(result, file, indent=4)