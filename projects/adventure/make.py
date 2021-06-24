from sys import argv
from itertools import product
from os import path

level = int(argv[1])

types = ["description", "choice"]

nums = list(product(range(2), repeat=level - 1))
