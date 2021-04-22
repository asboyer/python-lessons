from sys import argv

from main import decryption, alphabet


def header(string):
    for c in string:
        print("-", end="")
    print("------------")

string = ''
for i in range(1, len(argv)):
    string += argv[i] + " "
string = string.lower().strip()

print(f"\nAll possible Caesar messages for '{string}':\n")

header(string)

for key in range(1, len(alphabet)):
    print(f"Key ({str(key)})", end=": \"")
    print(decryption(key, string, alphabet), end="\" \n")
    if key != len(alphabet) - 1:
        print("")

header(string)