my_number = 30

import random

computer_number = random.randint(0, 100)
counter = 0


for guess in range(5):
    counter = counter + 1
    if computer_number < my_number:
        print ("That's too low.")
    if computer_number > my_number:
        print ("That's too high.")
    if computer_number == my_number:
        print ("That's correct!")
        break
    computer_number = random.randint(0, 100)



print(counter)
