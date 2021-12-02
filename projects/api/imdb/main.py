import imdb, json, sys

ia = imdb.IMDb()

movie_id = sys.argv[1] 
movie = ia.get_movie(movie_id)

movie_json = {}
characters = []
for member in movie['cast']:
    try:
        role = member.currentRole
        if len(role) > 1:
            for character in role:
                characters.append(character['name'])
        else:
            characters.append(role['name'])
    except KeyError:
        pass
movie_json['characters'] = characters

for key in movie.keys():
    if key == 'cast':
        movie_json['cast'] = []
        for p in movie['cast']:
            movie_json['cast'].append(p['name'])
    elif isinstance(movie[key], list) and (
        isinstance(movie[key][0], imdb.Person.Person) or 
        isinstance(movie[key][0], imdb.Company.Company)):
        movie_json[key] = []
        for p in movie[key]:
            try:
                movie_json[key].append(p['name'])
            except KeyError:
                pass
    else:
        movie_json[key] = movie[key]

with open(movie['title'].replace(" ", "_").lower() + ".json", 'w', encoding='utf8') as jsf:
    json.dump(movie_json, jsf, indent=4, ensure_ascii=False)