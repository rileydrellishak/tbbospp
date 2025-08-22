"""Cho-han is a dice game played in gambling houses of feudal Japan. 
Two six-sided dice are rolled in a cup, and gamblers must guess if the 
sum is even (cho) or odd (han). The house takes a small cut of all 
winnings. The simple random number generation and basic math used to 
determine odd or even sums make this project especially suitable for 
beginners.
"""

"""
House will take 10% of the player's bet every time they win.
Winning doubles the player's bet.
Losing means player loses the total from their pot.
"""
import random, sys
JAPANESE_NUMBERS = {
    1: 'ICHI', 
    2: 'NI', 
    3: 'SAN', 
    4: 'SHI', 
    5: 'GO', 
    6: 'ROKU'
    }

def get_user_bet(purse):
    valid_input = False
    while not valid_input:
        bet = input(f"\nYou have {purse} mon. How much do you bet? ")
        valid_input = validate_bet(bet, purse)
    return int(bet)

def validate_bet(bet, purse):
    if (
        (not bet.isnumeric())
        or (int(bet) > purse) 
        or (int(bet) <= 0)
        ):
            print(f"You must bet a number greater than 0 and less "
                f"than {purse}.")
            return False
    else:
        return True

def validate_prediction(prediction):
    if (
        (prediction.upper() == "CHO")
        or (prediction.upper() == "HAN")
    ):
        return True
    else:
        print("Please enter CHO if you think the sum will be even, \n"
            "or HAN if you think the sum will be odd.\n")
        return False

def get_user_prediction():
    prediction_received = False
    while not prediction_received:
        prediction = input("CHO (even) or HAN (odd)? ").upper()
        prediction_received = validate_prediction(prediction)
    return prediction

def dice_roll():
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)
    return die_1, die_2

def even_or_odd(sum_of_roll):
    if sum_of_roll % 2 == 0:
        return "CHO"
    else:
        return "HAN"

def player_win(prediction, outcome):
    return prediction == outcome

def purse_result(player_win, bet, purse):
    if player_win:
        purse += (2 * bet)
        purse -= (bet // 10)
    else:
        purse -= bet
    return purse

def print_purse_outcome(player_win, bet):
    if player_win:
        print(f"You won! You take {bet - (bet //10)} mon.")
        print(f"The house collects a {bet // 10} mon fee.\n")
    else:
        print(f"You lost!\n")

def ask_replay(purse):
    # Will only give the option to keep playing while the purse is > 0
    is_input_valid = False
    while not is_input_valid and purse > 0:
        replay = input("Keep playing? (y/n): ").lower()
        if replay == "n":
            is_input_valid = True
            return False
        elif replay == "y":
            is_input_valid = True
            return True
        else:
            print("Enter y or n.")
    if purse == 0:
        return False

def print_roll_dialogue(die_1, die_2):
    print("\nThe dealer lifts the cup to reveal:")
    print(f"{JAPANESE_NUMBERS[die_1]} - {JAPANESE_NUMBERS[die_2]}")
    print(f"{die_1} - {die_2}\n")

def print_opening_dialogue():
    print("""
        
        Cho-Han, by Al Sweigart.
        
        In this traditional Japanese dice game, two die are rolled in 
        a bamboo cup by the dealer sitting on the floor. The player 
        must guess if the sum of the die will be even (cho) or odd
        (han).
        
        House will take 10% of the player's bet every time they win. 
        Winning doubles the player's bet.
        Losing means player loses the total from their pot.
        """)

def print_prediction_dialogue():
    print("\nThe dealer swirls the cup and you hear the rattle of the " \
    "dice.")
    print("The dealer slams the cup on the floor, still covering the \n" \
    "dice and asks for your bet.\n")

def gameplay():
    purse = 5000
    playing = True
    print_opening_dialogue()
    while playing:
        # Gets user bet based on the amount in their purse
        bet = get_user_bet(purse)
        # Gets user prediction -- Cho (even) or Han (odd)
        print_prediction_dialogue()
        prediction = get_user_prediction()

        # Simulates dice roll and sums the die
        die_1, die_2 = dice_roll()
        sum_roll = die_1 + die_2

        # Checks if sum is even or odd, assigns Cho or Han accordingly
        cho_or_han = even_or_odd(sum_roll)

        # Checks if user prediction is same as roll outcome -- T/F
        win = player_win(prediction, cho_or_han)

        # Prints game dialogue
        print_roll_dialogue(die_1, die_2)

        # Updates purse according to roll outcome, prints outcome of bet
        purse = purse_result(win, bet, purse)
        print_purse_outcome(win, bet)

        # Asks user to keep playing, will update flag if purse == 0 or F
        playing = ask_replay(purse)


    if purse == 0:
        print("You're out of money!")
    
    print("Thanks for playing!")

gameplay()