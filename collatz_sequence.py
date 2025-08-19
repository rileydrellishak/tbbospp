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
            and int(starting_number) > 1
        ):
            return True

    else:
        print("Enter a positive number greater than 1.")
        return False

def next_collatz_value(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int((n * 3) + 1)
    
def collatz_sequence():
    starting_number = get_starting_number()
    modified_number = starting_number
    list_of_terms = []
    steps = 0
    while modified_number > 1:

        steps += 1
        modified_number = next_collatz_value(modified_number)

        list_of_terms.append(modified_number)
        print(f"{steps}. {modified_number}")
    
    max_value = max(list_of_terms)
    
    print(f"Starting number: {starting_number}")
    print(f"Number of steps: {steps}")
    print(f"Maximum value reached: {max_value}")

    return list_of_terms


collatz_sequence()