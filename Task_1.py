# Task_1: Number Guessing Game  in Python :

import random
import math

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    if lower_bound >= upper_bound:
        print("Invalid range! The upper bound must be greater than the lower bound.")
        return
    
    secret_number = random.randint(lower_bound, upper_bound)
    
    max_guesses = math.ceil(math.log2(upper_bound - lower_bound + 1))
    print(f"You have {max_guesses} attempts to guess the number between {lower_bound} and {upper_bound}.")

    attempts = 0

    while attempts < max_guesses:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Try Again! You guessed too small.")
            elif guess > secret_number:
                print("Try Again! You guessed too high.")
            else:
                if attempts <= max_guesses:
                    print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                return  # End the game after a correct guess
            
        except ValueError:
            print("Please enter a valid integer.")
    
    print(f"Better Luck Next Time! The correct number was {secret_number}.")


number_guessing_game()

