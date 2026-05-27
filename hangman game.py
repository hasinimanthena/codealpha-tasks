import random

# words list
words = ["apple", "tiger", "house", "chair", "plant"]

# select random word
word = random.choice(words)

# store guessed letters
guessed = ""

# chances
chances = 6

print("WELCOME TO HANGMAN GAME")

while chances > 0:

    display = ""

    # display guessed letters
    for letter in word:
        if letter in guessed:
            display = display + letter
        else:
            display = display + "_"

    print("\nWord :", display)

    # check win condition
    if display == word:
        print("You Won!")
        break

    # user input
    guess = input("Enter a letter: ")

    # correct guess
    if guess in word:
        guessed = guessed + guess
        print("Correct Guess")

    # wrong guess
    else:
        chances = chances - 1
        print("Wrong Guess")
        print("Remaining Chances:", chances)

# lose condition
if chances == 0:
    print("\nYou Lost!")
    print("Correct Word is:", word)