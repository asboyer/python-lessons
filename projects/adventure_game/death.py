from sys import argv
import os

level = int(argv[1])
choices = argv[2]

types = ['description', 'choice']

# delete all files after that level and corresponding choices
for text in types:
    for filename in os.listdir(f'./text/{text}s/'):
        filename = filename.split("_")
        l = filename[0][-1]
        c = filename[1].split('.txt')[0]
        if l >= level and c.startswith(choices):
            os.remove(f'./text/{text}s/{filename}')
