
import random


random_num = random.randint(1, 10)
tries = 1



name = input("Hey there, What's your name? ")

print("Hello", name + ".", )

quest = input("Do you want to play a game? [yes/no] ")
if quest.lower() == "no":
    print("OKAY, GOODBYE")
    exit()
if quest.lower() == "yes":

    print("I am thinking of a number between 1 & 10, can you guess the number ")
    guess = int(input("Have a guess: "))
    if guess > random_num:
        print("Guess Lower...")
if guess < random_num:
    print("Guess Higher...")
while guess != random_num:
    tries += 1
    guess = int(input("Try again = "))
    if guess < random_num:
        print("Guess Higher!!!!")
if guess == random_num:
    print("CONGRATS, YOU WIN!!!!", random_num, \
          "IT TOOK YOU", tries, "tries!!!")

