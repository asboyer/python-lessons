bad_data = [
        'available_markets', 
        'album_type', 
        'album_group', 
        'type',
        'external_urls', 
        'external_ids', 
        'copyrights', 
        'release_date_precision',
        'href',
        'is_local',
        'limit',
        'next',
        'offset',
        'previous',
        'added_by',
        'album',
        "video_thumbnail",
        "added_at",
        "primary_color",
        ]        

def clean_playlist_tracks(result):
    for track in list(result):
        for data in list(track):
            if data in bad_data:
                del track[data]
            for d in list(track['track']):
                if d in bad_data:
                    del track['track'][d]
        artist_list = []

        for artist in track['track']['artists']:
            artist_list.append(artist['name'])
        artists_string = ''
        for i in range(len(artist_list)):
            if i == len(artist_list) - 1:
                artists_string += artist_list[i]
            else:
                artists_string += f'{artist_list[i]}, '
        track['track']['artists'] = artists_string

    songs = {}

    rank = 1
    for track in list(result):
        songs[str(rank)] = {}
        songs[str(rank)]['name'] = track['track']['name']
        songs[str(rank)]['artists'] = track['track']['artists']
        rank += 1

    return songs

def clean_album_result(result):
    for data_field in list(result):
        if data_field in bad_data:
            del result[data_field]
    artist_list = []
    for artist in result['artists']:
        artist_list.append(artist['name'])
    artists_string = ''
    for i in range(len(artist_list)):
        if i == len(artist_list) - 1:
            artists_string += artist_list[i]
        else:
            artists_string += f'{artist_list[i]}, '
    result['artists'] = artists_string

    best_image_url = ''
    for image in result['images']:
        if image['height'] == 640:
            best_image_url = image['url']
    del result['images']
    result['image'] = best_image_url

    for data_field in list(result['tracks']):
        if data_field in bad_data:
            del result['tracks'][data_field]

    for track in list(result['tracks']['items']):
        for data_field in list(track):
            if data_field in bad_data:
                del track[data_field]
        artist_list = []
        for artist in track['artists']:
            artist_list.append(artist['name'])
        artists_string = ''
        for i in range(len(artist_list)):
            if i == len(artist_list) - 1:
                artists_string += artist_list[i]
            else:
                artists_string += f'{artist_list[i]}, '
        track['artists'] = artists_string

    tracks = result['tracks']['items']
    del result['tracks']
    result['tracks'] = tracks


    return result