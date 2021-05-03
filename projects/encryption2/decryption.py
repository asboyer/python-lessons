from sys import argv
from main import decryption, alphabet

argv = ['decryption.py', 'khoor']

string = ""
for i in range(1, len(argv)):
    string += argv[i] + " "
string = string.lower().strip()

#                1-25
for key in range(1, len(alphabet)):
    print(f"Key ({str(key)})", end=": \"")
    print(decryption(key, string, alphabet), end="\"\n")