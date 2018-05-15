# This is a draft of a game that shows you hot and cold
# based on how close you are to a random number

import random



computer_number = random.randint(1, 101)

guesses = 0

for guess in range(5):
    guesses = guesses + 1
    guess = input("Please guess a number between 1 and 100. > ")
    guess = int(guess)
    if guess < computer_number:
        print ("That's too low.")
    if guess > computer_number:
        print ("That's too high.")
    if guess == computer_number:
        print ("That's correct!")
        break



print(guesses)





#my_number = 30

#import random

#computer_number = random.randint(0, 100)
#counter = 1
