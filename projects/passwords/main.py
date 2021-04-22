import random

# characters

alphabet = "abcdefghijklmnopqrstuvwxyz"
caps_alphabet = alphabet.upper()
nums = "0123456789"
special = "$@#&!"

chars = alphabet + caps_alphabet + nums + special

password = ""
for i in range(17):
    password += random.choice(chars)

print(password)