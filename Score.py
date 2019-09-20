from Utils import SCORES_FILE_NAME

def write_score(difflevel):
    with open(SCORES_FILE_NAME, 'a+') as f:
        POINTS_OF_WINNING = (difflevel * 3) + 5
        f.write(POINTS_OF_WINNING)


def add_score(difficulty):
    #check if file is empty then it fails
    if os.path.exists(SCORES_FILE_NAME) and os.path.getsize(SCORES_FILE_NAME) > 0:
        with open(SCORES_FILE_NAME, 'r') as f:
            score = f.readlines(SCORES_FILE_NAME)
            return score
    else:
        with open('New_Scorefile', 'a+') as f:
            f.write(difficulty)


























    with open(SCORES_FILE_NAME, 'r'):


SCORES_FILE_NAME = "1"

import os
path = os.getcwd()
if os.path.exists(path + '/' + SCORES_FILE_NAME) and os.path.getsize(path + '/' + SCORES_FILE_NAME) > 0:
    print('File is not empty')
else:
    print('File is empty')
