#!/usr/bin/python

import random
import os


def game():
    number = int(input("What number do you want?: "))

    value = int(random.randint(1, 6))
    
    if int(number) == int(value):
        print("You died, the number was", value)
        print("logging out...")
        os.system("shutdown /l")
        
    if (number) != (value):
        print("you survived , the number was", value)
        print("You dont have to continue (:")
        print("Quitting..")
        quit()

game()