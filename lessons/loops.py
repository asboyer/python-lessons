# while loop:
while hungry:
    eat food
    drink

    if full:
        hungry = False
        # once hungry == false, while loop condition is no longer true

# for loops:
# dumplngs list of 16 dumplings
for dumpling in dumplings:
    eat(dumpling)
    
    if dumplings_eaten == 25:
        full = True

    if full:
        break

# looping through list (certain amount of times) ONLY using while loop:
my_list = [1, 2, 3]
i = 0
while i < len(my_list):
    print(my_list[i])

