# functions 
def find(string1, char):
    for i in range(len(string1)):
        if string1[i] == char:
            return i
    return -1

def encrypt(key, character, alphabet):
    position = find(alphabet, character)
    if position == -1:
        return character
    newPosition = (position + key) % len(alphabet)
    newCharacter = alphabet[newPosition]
    return newCharacter

def decrypt(key, character, alphabet):
    position = find(alphabet, character)
    if position == -1:
        return character
    oldPosition = (position - key) % len(alphabet)
    oldCharacter = alphabet[oldPosition]
    return oldCharacter

def encryption(key, string, alphabet):
    finalString = ''
    for character in string:
        finalString += encrypt(key, character, alphabet)
    return finalString

def decryption(key, string, alphabet):
    finalString = ''
    for character in string:
        finalString += decrypt(key, character, alphabet)
    return finalString

# variables:
alphabet = 'abcdefghijklmnopqrstuvwxyz'
string = input('Please enter a string: ').lower().strip()
key = int(input('Please enter a key: '))
    
while True:
    try:
        option = int(input("Encrypt(1) or decrypt(0)? "))
        if option == 1:
            finalString = encryption(key, string, alphabet)
        elif option == 0:
            finalString = decryption(key, string, alphabet)
        else:
            print("Please enter 1 or 0")
            continue
    except ValueError:
        print("Please enter 1 or 0")
        continue
    break

print(finalString)