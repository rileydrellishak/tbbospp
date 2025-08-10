""" Bagels, by Al Sweigart
A deductive logic game where you must guess a number based on clues
"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(f"I'm thinking of a {NUM_DIGITS}-digit number with no repeated digits. Try to guess what it is")