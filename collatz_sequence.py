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
import matplotlib.pyplot as plt
import numpy as np


def get_starting_number():
    """Prompts user for an input (a number) to start off the sequence.
    Also validates input to ensure it is a positive integer.

    Parameters:
    None

    Returns:
    int
        The starting number for the Collatz sequence.
    """
    valid_input = False
    while not valid_input:
        starting_number = input("Enter a number to start with: ")
        valid_input = validate_starting_number(starting_number)

    return int(starting_number)

def validate_starting_number(starting_number):
    """Checks if user input is an integer greater than 1.

    Parameters:
    starting_number : string
        The starting number of the Collatz sequence.
    
    Returns:
    bool
        Switches flag in get_starting_number() if input is an int > 1.
    """
    if (starting_number.isnumeric() 
            and int(starting_number) > 1
        ):
            return True

    else:
        print("Enter a positive number greater than 1.")
        return False

def next_collatz_value(n):
    """Calculates the next term in a Collatz sequence.

    Parameters:
    n : int
        The current term in the Collatz sequence.

    Returns:
    int
        The next term in the Collatz sequence.
    """
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int((n * 3) + 1)
    
def print_steps(sequence):
    """Prints out the step number and term in Collatz sequence.

    Parameters:
    sequence : list
        The list of terms after a completed Collatz sequence.
    
    Returns:
        None
    """
    for i in range(len(sequence)):
        if i == 0:
            print(f"Start: {sequence[i]}")
        else:
            print(f"{i}. {sequence[i]}")

def compute_stats(sequence):
    """Finds the starting value, the number of steps taken, and the 
    maximum value in a Collatz sequence.

    Parameters:
    sequence : list
        The list of terms after a completed Collatz sequence.

    Returns:
    dictionary
        Keys are titles of stats, values are the value of each relevant term.
    """
    stats = {"start": sequence[0], 
            "steps": len(sequence) - 1, 
            "max": max(sequence)}
    return stats

def print_summary(stats):
    """Prints a summary of the Collatz sequence.

    Parameters:
    stats : dictionary
        Dictionary containing relevant statistics of the sequence.
    
    Returns:
        None.
    """
    print(f"Starting from {stats['start']}, it took {stats['steps']} "
        f"steps to reach 1. Maximum value reached was {stats['max']}.")

def run_collatz():
    """Main function to generating a Collatz sequence and printing 
    relevant statistics.

    Parameters:
    None

    Returns
    list
        List of terms in the Collatz sequence, starting with starting
        number.
    """
    starting_number = get_starting_number()
    term = starting_number
    collatz_sequence = [starting_number]

    while term > 1:
        term = next_collatz_value(term)
        collatz_sequence.append(term)

    print_steps(collatz_sequence)
    print_summary(compute_stats(collatz_sequence))

    return collatz_sequence

collatz_sequence = run_collatz()

def axes(sequence):
    x_axis = []
    y_axis = sequence
    for i in range(len(sequence)):
        x_axis.append(i)
    return x_axis, y_axis

x_values, y_values = axes(collatz_sequence)

plt.plot(x_values, y_values, 'ro')
plt.axis((0, len(collatz_sequence), 0, max(collatz_sequence)))
plt.show()