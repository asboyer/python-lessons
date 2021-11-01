from sys import argv
from itertools import product
from os import path

levels = int(argv[1]) + 1

types = ['description', 'choice']

for level in range(1, levels):
    choices = list(product(range(2), repeat=level - 1))
    for choice in choices:
        string = ""
        for num in choice:
            string += str(num)
        for text in types:
            filename = f'./text/{text}s/{text}{level}_{string}.txt'
            if not path.exists(filename):
                file = open(filename, "w")
                file.write(f"Decisions leading to this point: {string}")
                file.close()