"""MemoryGame.py
The purpose of memory game is to display an amount of random numbers to the users for 0.7
seconds and then prompt them from the user for the numbers that he remember. If he was right
with all the numbers the user will win otherwise he will lose.
Properties
1. Difficulty

Methods
1. generate_sequence - Will generate a list of random numbers between 1 to 101. The list
length will be difficulty.
2. get_list_from_user - Will return a list of numbers prompted from the user. The list length
will be in the size of difficulty.
3. is_list_equal - A function to compare two lists if they are equal. The function will return
True / False.
4. play - Will call the functions above and play the game. Will return True / False if the user
lost or won.
"""

import Live
import random, time, subprocess, Score
from os import name

#Clear the screen
def clear():
    if name == 'nt':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('export TERM=xterm-color', shell=True)
        subprocess.call('clear', shell=True)

def generate_sequence(generatelist_difflevel):
    global generated_list
    list = []
    for num in range(1, generatelist_difflevel+1):
        num = random.randint(1,102)
        list.append(num)
    generated_list = list

def get_list_from_user(difflevel_list):
    global user_list_entry
    print("""A bunch of numbers will be appeared on the screen as per your difficulty level
             Please remember them quickly :) """)
    print(generated_list)
    time.sleep(.7)
    print("Times Up !")
    """"
    NOTE: It will not clear you screen because you are using Pycharm and not terminal.
    So for Pycharm needs a library (import pyautogui; pyautogui.hotkey('command', 'l')) 
    """
    clear()
    user_list_entry = [int(num) for num in input("Please enter the %s numbers from your memory : " % difflevel_list).split()]


def is_list_equal():
    if generated_list == user_list_entry:
        return True
    else:
        return False

def play(num):
    generate_sequence(num)
    get_list_from_user(num)
    result = is_list_equal()
    if result:
        Score.write_score(num)
        print("You have guessed right and won the game. \n The computer have also chosen %s" % generated_list)
    else:
        print("Wrong guess , You have lost! \n The computer have chosen %s" % generated_list)


