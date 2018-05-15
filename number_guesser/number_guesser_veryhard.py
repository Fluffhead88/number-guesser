my_number = 30

import random

A = 0

B = 100

computer_number = random.randint(A, B)
counter = 0





for guess in range(5):

    counter = counter + 1
    if computer_number < my_number:
        print ("That's too low.")
        computer_number = 
    if computer_number > my_number:
        print ("That's too high.")
        computer_number < B
    if computer_number == my_number:
        print ("That's correct!")
        break




print(counter)
