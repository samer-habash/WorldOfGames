from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


googledriver = webdriver.Chrome(executable_path="/home/sam/Desktop/browsers_webdrivers/chromedriver")
googledriver.implicitly_wait(1)

def test_scores_service():
    googledriver.get("http://localhost:5002/")
    Grab_Score = googledriver.find_element_by_id("Score").text
    Score=''.join([n for n in Grab_Score if n.isdigit()])
    if Score in range(1, 1001):
        return True
    else:
        return False

def main_function():
    Score_result=test_scores_service()
    if Score_result:
        return 0
    else:
        return -1

