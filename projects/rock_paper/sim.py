from random import randint

number_of_outcomes = []

amount_of_rounds = 10
amount_of_simulations = 10000

for i in range(amount_of_rounds + 1):
    number_of_outcomes.append(0)

for i in range(amount_of_simulations):

    rock = 0
    paper = 0
    scissors = 0

    for i in range(amount_of_rounds):  

        computer_choice = randint(1, 3)

        if computer_choice == 1:
            rock += 1
        if computer_choice == 2:
            paper += 1
        if computer_choice == 3:
            scissors += 1

    # fraction = amount of rocks/amount of times played
    # print("______________________________")
    # print("In a sample of 10 rounds:")
    # print("Amount of rock: " + str(rock)) # should be 1/3 
    # print("Amount of paper: " + str(paper)) # should be 1/3
    # print("Amount of scissors: " + str(scissors) + "\n") # should be 1/3

    list_of_outcomes = [rock, paper, scissors]

    for outcome in list_of_outcomes:
        for number in range(len(number_of_outcomes)):
            if outcome == number:
                number_of_outcomes[number] += 1

print(f'In {str(amount_of_simulations)} rounds of 10:')
for number in range(len(number_of_outcomes)):
    print(f'Amount of {str(number)}\'s: {str(number_of_outcomes[number])}') #TODO: print the probability of this outcome occruing