# the setup
f = open('input.txt', 'r')
lines = f.readlines()
for i in range(len(lines)):
    lines[i] = int(lines[i].strip())

