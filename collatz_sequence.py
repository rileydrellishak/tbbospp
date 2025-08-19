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
    
def print_steps(sequence):
    for i in range(len(sequence)):
        if i == 0:
            print(f"Start: {sequence[i]}")
        else:
            print(f"{i}. {sequence[i]}")

def compute_stats(sequence):
    stats = {"start": sequence[0], 
            "steps": len(sequence) - 1, 
            "max": max(sequence)}
    return stats

def print_summary(stats):
    print(f"Starting from {stats['start']}, it took {stats['steps']} "
        f"steps to reach 1. Maximum value reached was {stats['max']}.")

def run_collatz():
    starting_number = get_starting_number()
    term = starting_number
    list_of_terms = [starting_number]

    while term > 1:
        term = next_collatz_value(term)
        list_of_terms.append(term)

    print_steps(list_of_terms)
    print_summary(compute_stats(list_of_terms))

    return list_of_terms

run_collatz()