"""Collatz Sequence

Goal: Generate and analyze a Collatz number sequence.

Requirements:
* Ask for a starting number
* Apply rules until sequence reaches 1
* If even, / 2
* If odd, * 3, add 1
* Print each step of the sequence

Optional Enhancements:
* Count steps to reach 1
* Track the highest number in the sequence
"""

def get_starting_number():
    valid_input = False
    while not valid_input:
        starting_number = input("Enter a number to start with: ")

        valid_input = validate_starting_number(starting_number)

    return int(starting_number)

def validate_starting_number(starting_number):
    if (starting_number.isnumeric() 
            and int(starting_number) > 0
        ):
            return True

    else:
        print("Enter a positive number.")
        return False