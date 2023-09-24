import random
import sys
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# Input value
playerChoice = input("Enter ... \n1 for ROCK,\n2 for PAPER or\n3 for SCISSORS\n\n")

# Random number generator
computerChoice = random.choice("123")

# Typecasting to int for safer conversion
playerChoice = int(playerChoice)
computerChoice = int(computerChoice)

# Catch user input issues here
if playerChoice < 1 or playerChoice > 3:
    sys.exit("You must enter 1, 2, or 3.\n")

print("\nYou chose: " + str(RPS(playerChoice)).replace("RPS.", "") + "\n")
print("Computer chose: " + str(RPS(computerChoice)).replace("RPS.", "") + "\n")

# Conditional checks to deduce game winner
if playerChoice == computerChoice:
    print("😮 Tie Game!\n")
elif playerChoice == 1 and computerChoice == 3:
    print("🎉 You won!\n")
elif playerChoice == 3 and computerChoice == 2:
    print("🎉 You won!\n")
elif playerChoice == 2 and computerChoice == 1:
    print("🎉 You won!\n")
else:
    print("🐍 Python wins!\n")
