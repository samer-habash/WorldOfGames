"""
CurrencyRouletteGame.py
This game will use the free currency api to get the current exchange rate from USD to ILS, will
generate a new random number between 1-100 a will ask the user what he thinks is the value of
the generated number from USD to ILS, depending on the user’s difficulty his answer will be
correct if the guessed value is between the interval surrounding the correct answer

Properties
1. Difficulty
Methods
1. get_money_interval -Will get the current currency rate from USD to ILS and will
generate an interval as follows:
a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t +
(5 - d))

2. get_guess_from_user - A method to prompt a guess from the user to enter a guess of
value to a given amount of USD
3. play - Will call the functions above and play the game. Will return True / False if the user
lost or won.
"""
import Live
import json
import requests
import Score

def get_money_interval(difflevel_interval):
    global from_interval, upto_interval, USDILS

    #choose_difficulty = int(input("Please choose your difficulty level in Memory Game : "))
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    # Making our request
    response = requests.get(url)
    data = json.loads(response.text)
    USDILS = data['rates']['ILS']
    from_interval = float(USDILS - (5 - difflevel_interval))
    upto_interval = float(USDILS + (5 - difflevel_interval))

def get_guess_from_user():
    global user_guess_entry
    user_guess_entry = float(input("Please guess the currency rate of 1 USD interns of ILS : "))

def play(difflevel):
    get_money_interval(difflevel)
    get_guess_from_user()
    if user_guess_entry > from_interval and user_guess_entry < upto_interval:
        print("You have guessed it approximately right and won the game. \n The rate of USDILS is %f" % USDILS)
        Score.write_score(difflevel)
        return True
    else:
        print("Wrong guess , You have lost! \n  The rate of USDILS is %f" % USDILS)
        return False