"""Bagels: A logic deduction game. Guess a secret number (str) using
logical clues.

3 unique digits, can include a leading zero. 10 guesses.

Clues after each guess:
Fermi - correct digit, correct position
Pico - correct digit, wrong position
Bagels - no digits match

Clues appear in random order. Reveal secret number if guesses run out.

Example: if the secret number is 420 and user guesses 324,
Fermi pico

If secret number is 024 and user guesses 111,
Bagels
"""
import random

MAX_DIGIT_LENGTH = 3
MAX_GUESSES = 5

def get_user_input():
    """Validates the user input - checks if it is a sequence of 
    MAX_DIGIT_LENGTH numbers.

    Args:
        None

    Returns:
        string: The three digit guess of the mystery number.
    """
    valid_input = False

    while not valid_input:
        user_input = input(f"Guess a {MAX_DIGIT_LENGTH} digit number: ")
        
        if user_input.isdigit() and (len(user_input) == MAX_DIGIT_LENGTH):
            valid_input = True

        else:
            print(f"Your guess must be a {MAX_DIGIT_LENGTH} digit number.")
        
    return user_input

def set_secret_number():
    """Sets the secret number the user is trying to guess. First as a
    list then converted to a string of numbers to allow for the
    first digit to be 0.

    Args:
        None

    Returns:
        string: The secret number the user is trying to guess.
    """
    secret_number = []
    
    while len(secret_number) < MAX_DIGIT_LENGTH:
        secret_number.append(str(random.randint(0,9)))
    
    return "".join(secret_number)

def compare_guess_to_secret_number(user_input, secret_number):
    """Compares the values between user guess and the secret_number to
    generate the hint string.

    Args:
        user_input (str): The MAX_DIGIT_LENGTH digit number the 
        user guessed.
        secret_number (str): The secret number the user is trying to
        guess.

    Returns:
        " ".join(hints) (str): A string that joins the clues 
        (alphabetical order).

    """
    hints = []
    
    for i in range(0, (MAX_DIGIT_LENGTH)):
        if user_input[i] not in secret_number:
            hints = hints
        else:
            if user_input[i] == secret_number[i]:
                hints.append("Fermi")
            else:
                hints.append("Pico")

    hints.sort()
    return " ".join(hints)

def still_playing(hints):
    """Checks the hints to see if the secret number was guessed.

    Args:
        hints: the string produced from 
        compare_guess_to_secret_number(user_input, secret_number)

    Returns:
        Boolean: will switch the True/False flag in the main game loop
        according to the contents of the hints string.
    """

    if hints.count("Fermi") == MAX_DIGIT_LENGTH:
        hints = "You guessed the secret number!"
        print(hints)
        return False
    
    elif len(hints) == 0:
        hints = "Bagels"
        print(hints)
        return True

    else:
        hints = hints
        print(hints)
        return True

def bagels_game():
    secret_number = set_secret_number()
    # Debugging info
    print(secret_number)
    num_guesses = 0
    waiting_for_correct = True

    while (num_guesses < MAX_GUESSES) and waiting_for_correct:
        num_guesses += 1
        user_guess = get_user_input()

        hints = compare_guess_to_secret_number(user_guess, secret_number)

        waiting_for_correct = still_playing(hints)
    
    if waiting_for_correct:
        print(f"The secret number was {secret_number}.")

bagels_game()