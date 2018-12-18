from random import randint
from linereader import getline
from time import sleep
import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='eu-west-1')
# Change variable production to 0 for in order to enable verbose mode. 
production = 1
if production == 1: 
    v = input("Would you like to enable verbose mode? (0/1)")
else:
    v=0

while 1: 
    choice = str.lower(input("What would you like to do? (Play/ Quit)"))
    if v == 1:
        print('Calling DetectSentiment')
    if choice != "":
        result = comprehend.detect_sentiment(Text=choice, LanguageCode='en') #, sort_keys=True, indent=4)
        p = result["SentimentScore"]["Positive"]
        if v == 1:
            print("P = ", p)
        n = result["SentimentScore"]["Negative"]
        if v == 1:
            print("N = ", n)
    else: 
        print("No input detected, quitting...")
        sleep(1)
        break
    if p>=n:
        randline = getline("dogs.txt", randint(1,30))
        excersise = randint(1,5)
        inteligence = randint(1,100)
        friendliness = randint(1,10)
        drool = randint(1,10)
        print("Welcome!")
        print(excersise)
        print(randline)
    else:
        print("Exiting...")
        break