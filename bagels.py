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
MAX_GUESSES = 10

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

def compare_guess_to_secret_number(guessed_number, secret_number):
    """Compares the values between user guess and the secret_number to
    generate the hint string.

    Args:
        guessed_number (str): The MAX_DIGIT_LENGTH digit number the 
        user guessed.
        secret_number (str): The secret number the user is trying to
        guess.

    Returns:
        " ".join(hints) (str): A string that

    """
    hints = []
    
    for i in range(0, (MAX_DIGIT_LENGTH)):
        if guessed_number[i] == secret_number[i]:
            hints.append("Fermi")
        
        # elif guessed_number[i] in secret_number AND it isn't already 
        # example: secret_number is 304, guess is 333 -- output should be Fermi.
        # example: secret is 123, guess is 222 -- output should just be Fermi
        # example: secret is 212, guess is 222 -- output should be Fermi Fermi
        # example: secret is 555, guess is 456 -- output is Fermi
        # example: secret is 631, guess is 133 -- output is Pico Fermi
        # example: secret is 123, guess is 444 -- output is Bagels

    if hints.count("Fermi") == MAX_DIGIT_LENGTH:
        hints.clear()
        hints.append("You guessed the secret number!")
    
    elif len(hints) == 0:
        hints.append("Bagels")
    
    return " ".join(hints)


def bagels_game():
    secret_number = set_secret_number()
    # Debugging info
    print(secret_number)

    user_guess = get_user_input()

    print(type(user_guess))

    hints = compare_guess_to_secret_number(user_guess, secret_number)
    print(hints)
    

bagels_game()