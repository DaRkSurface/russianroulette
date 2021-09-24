#!/usr/bin/python

import random
import os


def game():
    number = int(input("What number do you want?: "))

    value = int(random.randint(1, 6))
    
    if int(number) == int(value):
        print("You died, the number was", value)
        main()
    if (number) != (value):
        print("you survived , the number was", value)
        print("You dont have to continue (:")
        print("Quitting..")
        quit()

def main():
    print(" (1): Delete a file.")
    print(" (2): Log out of computer.")

    option = input("Select options")

    if option == "1":
        filedel = input("What file do you want to delete (directory)")
        os.remove(filedel)
    if option == "2":
        print("logging out...")
        os.system("shutdown /l")
    else:
        print("you did not enter a number")
        again = input("Do you want to try again y/n:")
        if again == "y" or "Y":
            main()
        if again == "n" or "N":
            print("Quitting..")
            quit()
        else:
            print("you did not enter y or n")
            print("Quitting..")
            quit()
        

game()