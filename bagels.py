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

def set_secret_number():
    secret_number = []
    while len(secret_number) < MAX_DIGIT_LENGTH:
        secret_number.append(random.randint(0,9))
    return secret_number

def bagels_game():

    mystery_number = set_secret_number()
    print(mystery_number)

bagels_game()