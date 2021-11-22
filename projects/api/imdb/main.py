import imdb, json

ia = imdb.IMDb()

# topsters = ia.get_top250_movies()

# f = open('movies.txt', 'w')
# for i in range(250):
#     f.write(topsters[i]['title'] + "\n")

movie = ia.get_movie('0121766')
# f = open('movie_ref.txt', 'w')
# for key in movie.keys():
#     f.write(key + "\n")
movie_json = {}
for key in movie.keys():
    print(key)
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

with open(movie['title'].replace(" ", "_").lower() + ".json", 'w') as jsf:
    json.dump(movie_json, jsf, indent=4)