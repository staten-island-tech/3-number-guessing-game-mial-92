""" number = 10
while number != 0:
    print(number)
    number = number - 1
     """

import random
RandomNumber = random.randint(1 , 10) 
guess = False
answer = int(input("Guess a number from 1 to 10"))

while guess == False:
    
    if answer == RandomNumber:
        guess = True
        print("yay youre correct")
    else:
        print("youre wrong :c")
        answer = input("guess again")
        print(RandomNumber)