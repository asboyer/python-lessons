import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import sys
import tools

from secret import client_id, client_secret
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri = sys.argv[1]

result = tools.clean_album_result(sp.album(uri))
album_name = result['name'].replace(" ", "_").lower()

with open(f"albums/{album_name}.json", "w") as file:
    json.dump(result, file, indent=4)
    