from sys import argv
from boyer import get_num

def find(string, char):
    for i in range(len(string)):
        if string[i] == char:
            return i
    return -1

def encrypt(key, char, alphabet):
    position = find(alphabet, char)
    if position == -1:
        return char
    newPosition = (position + key) % len(alphabet)
    newChar = alphabet[newPosition]
    return newChar

def encryption(key, string, alphabet):
    finalString = ''
    for char in string:
        finalString += encrypt(key, char, alphabet)
    return finalString

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

def get_key():
    key = get_num('Please enter a key: ', start=1, finish=25, error_message='Please enter a valid key between 1 and 25!')

alphabet = 'abcdefghijklmnopqrstuvwxyz'

if __name__ == "__main__":
    if len(argv) > 2:
        min_value = 2
        try:
            key = int(argv[1])
        except ValueError:
            key = int(input('Please enter a key: '))
            min_value = 1

        string = ''
        for i in range(min_value, len(argv)):
            string += argv[i] + " "
        string = string.lower().strip()

    elif len(argv) > 1:
        try:
            key = int(argv[1])
            string = input('Please enter a string: ')
        except ValueError:
            string = argv[1]
            key = int(input('Please enter a key: '))

    else:
        string = input('Please enter a string: ')
        key = int(input('Please enter a key: '))

    print(encryption(key, string, alphabet))