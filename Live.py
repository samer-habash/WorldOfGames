import GuessGame
import MemoryGame
import CurrencyRouletteGame

def welcome(name):
    return "Hello %s and welcome to the World of Games (WoG). \
            Here you can find many cool games to play." % name

def CheckChoice(choice):
    if choice in range(1,4):
        return True
    else:
        return False

def CheckChoicediff(choice):
    if choice in range(1,6):
        return True
    else:
        return False


def load_game():
    choose_game = int(input("""
        Please choose a game to play: 
                    1. Guess Game - a sequence of numbers will appear for 1 second and you have to guess it back 
                    2. Memory Game - guess a number and see if you chose like the computer 
                    3. Currency Roulette - Guess the current temperature currently in Jerusalem 
                    
        Enter Your Choice Here : """))
    if CheckChoice(choose_game):
        choose_difficulty = int(input(" Please choose game difficulty from 1 to 5 : "))
        if CheckChoicediff(choose_difficulty):
            print("Welcome to the Game")
            if choose_game == 1:
                print("You have chosen game GuessGame with difficulty level %s" % (choose_difficulty))
                GuessGame.play(choose_difficulty)
            elif choose_game == 2:
                print("You have chosen game MemoryGame with difficulty level %s" % (choose_difficulty))
                MemoryGame.play(choose_difficulty)
            elif choose_game == 3:
                print("You have chosen game CurrencyRouletteGame with difficulty level %s" % (choose_difficulty))
                CurrencyRouletteGame.play(choose_difficulty)
        else:
            print("You Have entered an Incorrect Option!")
            return -1
    else:
        print("You Have entered an Invalid Option!")
        return -1

