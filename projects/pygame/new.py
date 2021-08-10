r = 0

while True:

    if r == 255:
        down = True
    elif r == 0:
        down = False

    if down:
        r -= 1
    else:
        r += 1

    print(r)

