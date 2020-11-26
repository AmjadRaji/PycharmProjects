import random

rollingNumber = input("Number of rollings: ")
rollingNumber = int(rollingNumber)


for index in range(rollingNumber):
    dice = random.randrange(1, 7)
    print(dice)