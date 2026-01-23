import random

# Solution for the Week 02 Lab
choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Enter a number between 1-3 for following choices: 1-Rock, 2,Paper, 3-Scissors: ")

#for debugging
#print(playerChoice)
playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice should be between 1 and 3")
else:
    #Develop the game logic using if/elif/else
    computerChoice = random.randint(1,3)
    print("You chose {choices[playerChoice - 1]}, Computer chose {choices[computerChoice - 1]}")
    
    if playerChoice == computerChoice:
        print("It's a tie!")
    elif playerChoice == 1 and computerChoice == 3:
        print("Rock beats scissors -- You Win!")
    elif playerChoice == 2 and computerChoice == 1:
        print("Paper beats Rock -- You Win!")
    elif playerChoice == 3 and computerChoice == 2:
        print("Scissors beat Paper -- You Win!")
    else:
        print("You Lose!")