from random import randint
from linereader import getline
from time import sleep
import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='eu-west-1')

while 1: 
    choice = str.lower(input("What would you like to do? (Play/ Quit)"))
    if choice != "":
        result = comprehend.detect_sentiment(Text=choice, LanguageCode='en') #, sort_keys=True, indent=4)
        p = result["SentimentScore"]["Positive"]
        n = result["SentimentScore"]["Negative"]
    else: 
        print("No input detected, quitting...")
        sleep(1)
        break
    if p>=n:
        dname = getline("dogs.txt", randint(1,30))
        excersise = randint(1,5)
        inteligence = randint(1,100)
        friendliness = randint(1,10)
        drool = randint(1,10)
        print("Welcome!")
        print("Excersise: ", excersise)
        print("Intelignece: ", inteligence)
        print("Friendliness: ", friendliness)
        print("Drool: ", drool)
        print(dname)
        selection = input("Please select a category... \n")
        if selection.lower() == "drool":
            if drool <= randint(1,10):
                print("You won!")
            else:
                print("You loose!")
        elif selection.lower() == "excersise": 
            if excersise > randint(1,100):
                print("You win!")
            else:
                print("You loose!")
        elif selection.lower() == "inteligence": 
            if inteligence > randint(1,100):
                print("You win!")
            else: 
                print("You loose!")
        elif selection.lower() == "friendliness":
            if friendliness > randint(1,10):
                print("You win!")
            else: 
                print("You loose!")
        else: print("Not recognised")
    else:
        print("Exiting...")
        break