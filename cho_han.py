"""Cho-han is a dice game played in gambling houses of feudal Japan. 
Two six-sided dice are rolled in a cup, and gamblers must guess if the 
sum is even (cho) or odd (han). The house takes a small cut of all 
winnings. The simple random number generation and basic math used to 
determine odd or even sums make this project especially suitable for 
beginners.
"""

"""
House will take 10% of the player's bet every time.
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
        bet = input(f"You have {purse} mon. How much do you bet? ")
        valid_input = validate_bet(bet, purse)
    return int(bet)

def validate_bet(bet, purse):
    if (
        (not bet.isnumeric())
        or (int(bet) > purse) 
        or (int(bet) < 0)
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
        print("Please enter CHO if you think the sum will be even,"
            f"or HAN if you think the sum will be odd.")
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

def announce_roll(die_1, die_2):
    return JAPANESE_NUMBERS[die_1], JAPANESE_NUMBERS[die_2]

def sum_roll(die_1, die_2):
    return die_1 + die_2

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
        purse -= (purse // 10)
        print(purse)
    else:
        purse -= bet
        print(purse)
    return purse

def ask_replay():
    is_input_valid = False
    while not is_input_valid:
        replay = input("Keep playing? (y/n): ").lower()
        if replay == "n":
            is_input_valid = True
            return False
        elif replay == "y":
            is_input_valid = True
            return True
        else:
            print("Enter y or n.")

def gameplay():
    purse = 5000
    playing = True
    while purse > 0 and playing:
        bet = get_user_bet(purse)
        prediction = get_user_prediction()
        die_1, die_2 = dice_roll()
        jn_1, jn_2 = announce_roll(die_1, die_2)
        sum_of_roll = sum_roll(die_1, die_2)
        cho_or_han = even_or_odd(sum_of_roll)
        win = player_win(prediction, cho_or_han)
        print(f"{jn_1} - {jn_2}")
        print(f"{die_1} - {die_2}")
        print(f"{sum_of_roll}")
        print(cho_or_han)
        print(player_win(prediction, cho_or_han))
        purse = purse_result(win, bet, purse)
        print(purse)
        playing = ask_replay()

gameplay()