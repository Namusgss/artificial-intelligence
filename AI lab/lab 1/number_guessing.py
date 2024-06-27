# Create a number guessing game. Where you have to generate a random number in between 1 to 100 
# and user have to prompt a number for guess. if its high or low number let the user know and guide 
# them through the process to guess correct number.*/


import random

number = random.randint(1, 100)
print("Guess a number between 1 and 100")
guess = None
while guess != number:
    guess = int(input("Enter your guess: "))
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("You guessed it right!")
        break
    