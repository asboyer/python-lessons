import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
from tools import clean_result


from secret import client_id, client_secret
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# result = sp.search("asboyer", type="playlist", limit=20)
# playlist_uri = result["playlists"]["items"][0]["uri"]
# # result = sp.playlist_tracks(playlist_uri)
# result = clean_result(sp.playlist_tracks(playlist_uri)["items"])

playlist_uri = "spotify:playlist:37i9dQZEVXbLRQDuF5jeBp"
result = clean_result(sp.playlist_tracks(playlist_uri)["items"])

with open("result.json", "w") as file:
    json.dump(result, file, indent=4)