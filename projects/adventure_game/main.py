print("You are on a lake. You see a shark.")
choice = input('What do you do? ')

if choice == "run":
    print("You survived!")
elif choice.startswith("kill"):
    print("You can't kill the shark, and it eats you")
elif choice.startswith("befriend"):
    print("The shark becomes a close ally after you choose to befriend it")
else:
    print("The shark kills you!")