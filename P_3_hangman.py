import random

words = ["apple", "banana", "mango", "orange", "grapes", "papaya"]

word = random.choice(words)
guessed = []
wrong_guesses = 0
max_attempts = 6

hangman = [
    """
     -----
     |   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """
]

print("Welcome to Hangman!")

while wrong_guesses < max_attempts:

    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print(hangman[wrong_guesses])
    print("Word: ", display)

    if "_ " not in display:
        print("Congratulations! You've guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter. Try again.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

if wrong_guesses == max_attempts:
    print(hangman[5])
    print("Game Over! The word was:", word)