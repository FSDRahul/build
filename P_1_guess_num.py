# Number Guessing Game in Python

# Computer generates a random number between 1 and 100.
# User has a maximum of 7 attempts to guess the number.
# User wins immediately if the guess matches the randomly generated number.
# If the guess is lower than the selected number, the program displays "Too Low" and the user should try a higher number.
# If the guess is higher than the selected number, the program displays "Too High" and the user should try a lower number.
# Invalid input or numbers outside the range of 1 to 100 do not count as an attempt.
# If the user does not guess the number within 7 valid attempts, the game ends and reveals the correct number.

import random

max_attempts = 7

def guess_number():
    print("Welcome to the Number Guessing Game!")
    print(f"Guess the number between 1 and 100. You have {max_attempts} attempts.")

    random_guess = random.randint(1, 100)
    attempts = 0

    while attempts < max_attempts:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < random_guess:
                print("Too Low! Try a higher number.")
            elif user_guess > random_guess:
                print("Too High! Try a lower number.")
            else:
                print(f"Congratulations! You've guessed the number {random_guess} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer between 1 and 100.")
            attempts -= 1  # Invalid input does not count as an attempt
            continue

    if attempts == max_attempts and user_guess != random_guess:
        print(f"Sorry! You've used all {max_attempts} attempts. The correct number was {random_guess}. Better luck next time!")


guess_number()