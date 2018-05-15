my_number = 30

import random

computer_number = random.randint(0, 100)
counter = 0


for guess in range(5):
    computer_number = random.randint(0, 100)
    guess = computer_number
    counter = counter + 1
    if computer_number < my_number:
        print ("That's too low.")
        computer_number = random.randint(guess, 100)
    if computer_number > my_number:
        print ("That's too high.")
        computer_number = random.randint(0, guess)
    if computer_number == my_number:
        print ("That's correct!")
        break




print(counter)
