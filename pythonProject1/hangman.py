import random
with open('wordlist.txt', 'r') as f:
    words = f.readlines()


word = random.choice(words)[:-1]


errorsAllowed = 7
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
            
        else:
            print("_", end= " ")
    print("")
    

    guess = input(f"Allowed errors left {errorsAllowed}, Next guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        errorsAllowed -= 1
        if errorsAllowed == 0:
            break


    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"You found the word!!! It was {word}!")
else:
    print(f"Game over! The word was {word}!")