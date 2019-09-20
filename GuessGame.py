"""
World of Games

GuessGame.py
The purpose of guess game is to start a new game, cast a random number between 1 to a
variable called difficulty. The game will get a number input from the
Properties
1. Difficulty
2. Secret number

Methods
1. generate_number - Will generate number between 1 to difficulty and save it to
secret_number.
2. get_guess_from_user - Will prompt the user for a number between 1 to difficulty and
return the number.
3. compare_results - Will compare the the secret generated number to the one prompted
by the get_guess_from_user.
4. play - Will call the functions above and play the game. Will return True / False if the user
lost or won.
"""

import Live
import random, Score

def generate_number(generate_difflevel):
    global secret_number
    secret_number = random.randint(1, generate_difflevel+1)
    """ If you want to check the number generation of the computer """
    # with open('guess.txt', 'w') as f:
    #     f.write(str(secret_number))
    # return secret_number


def get_guess_from_user(guessing_difflevel):
    global entry_guess
    entry_guess = int(input("Please guess the game difficulty level from 1 to %d abd beat the computer : " % guessing_difflevel))
    if entry_guess in range(1, guessing_difflevel+1):
        return entry_guess
    else:
        return False

def compare_results():
    if secret_number == entry_guess:  # we should convert it into integer because input value is always string.
        return True
    else:
        return False

def play(difflevel):
    generate_number(difflevel)
    if not get_guess_from_user(difflevel):
        print("You have chosen an incorrect Value! , please try again! ")
        exit(10)
    result = compare_results()
    if result == True:
        Score.write_score(difflevel)
        print("You have guessed right and won the game. \n The computer have also chosen %d" % secret_number)
    else:
        print("Wrong guess , You have lost! \n The computer have chosen %d" % secret_number)