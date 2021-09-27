import random

# global variables
alphabet = "abcdefghijklmnopqrstuvwxyz"
nums = "0123456789"
special = "!$@#&*%_"

def generator(length=12, special_chars=True, num_chars=True):
    chars = alphabet + alphabet.upper()
    if special_chars:
        chars += special
    if num_chars:
        chars += nums
    password = ""
    for i in range(length):
        password += random.choice(chars)
    return password

for i in range(10):
    print(generator())