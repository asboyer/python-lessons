import imdb

ia = imdb.IMDb()

topsters = ia.get_top250_movies()

f = open('movies.txt', 'w')
for i in range(250):
    f.write(topsters[i]['title'] + "\n")