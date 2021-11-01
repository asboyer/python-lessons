import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

from tools import clean_album_result

from secret import client_id, client_secret
client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri = 'spotify:album:5CnpZV3q5BcESefcB3WJmz'

result = clean_album_result(spotify.album(uri))


with open("album.json", "w") as file:
    json.dump(result, file, indent=4)