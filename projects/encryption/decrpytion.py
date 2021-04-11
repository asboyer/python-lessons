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

alphabet = 'abcdefghijklmnopqrstuvwxyz'
string = input('Please enter a string: ').lower().strip()

print()
for c in string:
    print("-", end="")
print("-------")

for i in range(1, len(alphabet)):
    print(str(i), end=": ")
    print(decryption(i, string, alphabet))

for c in string:
    print("-", end="")
print("-------")