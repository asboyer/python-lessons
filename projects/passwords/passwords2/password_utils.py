import random
from os.path import exists

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

def add(name, username, password=generator()):
    if exists("passwords.txt"):
        file = open("passwords.txt", "a")
    else:
        file = open("passwords.txt", "w")
    file.write(f"{name}:")
    file.write(f"\n   Username: {username}")
    file.write(f"\n   Password: {password}\n")
    file.close()

if __name__ == "__main__":
    name = input("Website: ")
    username = input("Username: ")
    add(name, username)