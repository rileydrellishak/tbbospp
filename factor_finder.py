"""
A number's factors are any two other numbers that, when multiplied 
with each other, produce the number. For example, 2 x 13 = 26, so 2 and
13 are factors of 26. Also, 1 x 26 = 26, so 1 and 26 are also factors 
of 26. Therefore, we say that 26 has four factors: 1, 2, 13, and 26.

If a number only has two factors (1 and itself), we call that a prime 
number. Otherwise, we call it a composite number. Use the factor finder 
to discover some new prime numbers! (Hint: Prime numbers always end 
with an odd number that isn't 5.) You can also have the computer 
calculate them with Project 56, “Prime Numbers.”
"""
import sys

def get_user_input():
    valid_input = False
    while not valid_input:
        number = input("Enter a number to factor (or " \
        "'QUIT' to quit): ")
        if number.upper() == "QUIT":
            sys.exit()
        else:
            valid_input = validate_user_input(number)
    return int(number)

def validate_user_input(number):
    if number.isnumeric() and int(number) > 0:
        return True
    
    else:
        print("Please enter a number greater than 0.")

def list_of_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def factor_string(factor_list):
    factor_string = ""
    for item in factor_list:
        if item == factor_list[-1]:
            factor_string += f"{item}"
        else:
            factor_string += f"{item}, "
    return factor_string

def factor_finder():
    running = True
    while running:
        number = get_user_input()
        factors = list_of_factors(number)
        string_factors = factor_string(factors)
        print(factor_string(factors))

factor_finder()