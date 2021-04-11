from sys import argv

def find(string1, char):
    for i in range(len(string1)):
        if string1[i] == char:
            return i
    return -1

def decrypt(key, character, alphabet):
    position = find(alphabet, character)
    if position == -1:
        return character
    oldPosition = (position - key) % len(alphabet)
    oldCharacter = alphabet[oldPosition]
    return oldCharacter

def decryption(key, string, alphabet):
    finalString = ''
    for character in string:
        finalString += decrypt(key, character, alphabet)
    return finalString

def head(string):
    for c in string:
        print("-", end="")
    print("--------------")

alphabet = 'abcdefghijklmnopqrstuvwxyz'

string = ''
for i in range(1, len(argv)):    
    string += argv[i] + " "
string = string.lower().strip()

print("\nAll possible Caesar messages:")

head(string)

for i in range(1, len(alphabet)):
    print(f'Key: ({str(i)})', end=": \"")
    print(decryption(i, string, alphabet), end="\" \n")

head(string)