my_number = 30

import random

computer_number = random.randint(0, 100)
counter = 0


for guess in range(5):
    counter = counter + 1
    if computer_number < my_number:
        print ("That's too low.")
        computer_number_2 = random.randint(computer_number, 100)
    if computer_number > my_number:
        print ("That's too high.")
        computer_number_3 = random.randint(computer_number_2, computer_number)
    if computer_number == my_number:
        print ("That's correct!")
        break




print(counter)
