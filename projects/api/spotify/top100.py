import spotipy, json, tools
from spotipy.oauth2 import SpotifyClientCredentials

from secret import client_id, client_secret
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_uri = "spotify:playlist:6UeSakyzhiEt4NB3UAd6NQ"
result = tools.clean_playlist_tracks(sp.playlist_tracks(playlist_uri)["items"])

with open("top100.json", "w") as file:
    json.dump(result, file, indent=4)