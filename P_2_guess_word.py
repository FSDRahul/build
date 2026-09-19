import random

name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the Guess the Word game.")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

guesses = ""
turns = 12

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    print()

    if failed == 0:
        print("You won!")
        print(f"The word is: {word}")
        break

    guess = input("Guess a character: ")

    if len(guess) != 1:
        print("Please enter only one character.")
        continue

    if guess in guesses:
        print("You already guessed that character. Try again.")
        continue

    guesses += guess

    if guess not in word:
        turns -= 1
        print(f"wrong guess. You have {turns} more guesses.")

        if turns == 0:
            print("You lose!")
            print(f"The word was: {word}")