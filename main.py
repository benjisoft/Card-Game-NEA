from random import randint
from linereader import getline

randline = getline("dogs.txt", randint(1,30))

while 1: 
    choice = str.lower(input("What would you like to do? (Play/ Quit)"))
    if choice == "play":
        print("Welcome!")
        print(randline)
    elif choice=="quit":
        print("")
        break
    else:
        print('Unrecognised Input, Damnit!')