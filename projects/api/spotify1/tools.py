bad_data = [
            'available_markets', 'album_type', 'album_group', 'type', 
            'external_urls', 'external_ids','release_date_precision', 
            'genres', 'is_local', 'disc_number', 'offset', 'limit', 
            'next', 'previous', 'total', 'href', 'album', 'id'
            ]

def string_comma(l):
    string = ""
    for i in range(len(l)):
        if i == len(l) - 1:
            string += l[i]
        else:
            string += l[i] + ", "
    return string

def clean_album_result(result):
    # looping through total result
    for data_key in list(result):
        if data_key in bad_data:
            del result[data_key]
    result['tracks'] = result['tracks']['items']
    # looping through each track
    for track in list(result['tracks']):
        for data_key in list(track):
            if data_key in bad_data:
                del track[data_key]
        alist = []
        for a in track['artists']:
            alist.append(a['name'])
        track['artists'] = string_comma(alist)

    # artist section
    artists_list = []
    for artist in result["artists"]:
        artists_list.append(artist["name"])

    result['artists'] = string_comma(artists_list)

    # copyrights
    # result['copyrights'] = result['copyrights']['text']
    cp_list = []
    for cp in result['copyrights']:
        cp_list.append(cp['text'])

    result['copyrights'] = string_comma(cp_list)


    # best image url
    best_image_url = ''
    for image in result['images']:
        if image['height'] == 640:
            best_image_url = image['url']
    result['image'] = best_image_url
    del result['images']

    t = result['tracks']
    del result['tracks']
    result['tracks'] = t

    return result
