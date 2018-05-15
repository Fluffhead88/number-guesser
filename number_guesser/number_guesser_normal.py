# This is a draft of a game that shows you hot and cold
# based on how close you are to a random number

import random



computer_number = random.randint(1, 101)

counter = 1

for guess in range(5):
    guess = input("Please guess a number between 1 and 100. > ")
    if int(guess) == computer_number:
        print ("That's correct!")
        break
    else int(guess) > computer_number:
        print ("That's too high.")
    elif int(guess) < computer_number:
        print ("That's too low.")


counter = counter + 1
print(counter)





#my_number = 30

#import random

#computer_number = random.randint(0, 100)
#counter = 1
