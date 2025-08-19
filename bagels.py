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
        print()
        if user_input.isdigit() and (len(user_input) == MAX_DIGIT_LENGTH):
            valid_input = True

        else:
            print(f"Your guess must be a {MAX_DIGIT_LENGTH} digit number.")
        
    return user_input

def set_secret_number():
    """Sets the secret number the user is trying to guess. Unique digits,
    allows a leading 0.

    Args:
        None

    Returns:
        string: The secret number the user is trying to guess.
    """
    
    return "".join(random.sample("0123456789", MAX_DIGIT_LENGTH))

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
        if user_input[i] == secret_number[i]:
            hints.append("Fermi")
        elif user_input[i] in secret_number:
            hints.append("Pico")
    
    if not hints:
        return "Bagels"

    random.shuffle(hints)
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
    
    else:
        print(hints)
        return True

def num_guesses_left(MAX_GUESSES, num_guesses):
    return (f"Guesses left: {MAX_GUESSES - num_guesses}")


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
            print(num_guesses_left(MAX_GUESSES, num_guesses))
            print()
    
    if waiting_for_correct:
        print(f"The secret number was {secret_number}.")
    
    elif not waiting_for_correct:
        print(f"You had {MAX_GUESSES - num_guesses} guesses left.")

def ask_replay():
    """Keeps asking until user types y or n. Return true for replay,
    False to exit the game.
    """
    while True:
        print()
        replay = input("Play again? (y/n): ").lower()
        if replay == "y":
            return True
        elif replay == "n":
            return False
        else:
            print("I only know y or n!")

def play_bagels():
    playing = True
    game_count = 0
    while playing:
        bagels_game()
        game_count += 1
        
        playing = ask_replay()
        if playing:
            print()
            print("--- New Game ---")
            print()
    
    if game_count == 1:
        print(f"You played {game_count} game. Thanks for playing!")
    else:
        print(f"You played {game_count} games. Thanks for playing!")

play_bagels()