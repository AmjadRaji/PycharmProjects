password = "bluejay"
guess = ""
guessCount = 0
guessLimit = 3
outOfGuess = False

while guess != password and not (outOfGuess):
    if guessCount < guessLimit:
        guess = input("Enter guess: ")
        guessCount += 1
    else:
        outOfGuess = True 

if outOfGuess:
    print("Out of Guesses, YOU LOSE")
else:
    print("You Win!!!")