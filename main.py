from random import randint
from linereader import getline
import boto3
import json

comprehend = boto3.client(service_name='comprehend', region_name='eu-west-1')
randline = getline("dogs.txt", randint(1,30))

while 1: 
    choice = str.lower(input("What would you like to do? (Play/ Quit)"))
    print('Calling DetectSentiment')
    result = comprehend.detect_sentiment(Text=choice, LanguageCode='en') #, sort_keys=True, indent=4)
    positiveness = result["SentimentScore"]["Positive"]
    print(positiveness)
    print('End of DetectSentiment\n')

    if choice == "play":
        print("Welcome!")
        print(randline)
    elif choice=="quit":
        print("")
        break
    else:
        print('Unrecognised Input, Damnit!')