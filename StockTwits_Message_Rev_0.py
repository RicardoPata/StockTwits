import pyautogui as pg
import time

def Message(stock):

    pg.press("esc")
    time.sleep(1)
    pg.click(1254,105)
    time.sleep(5)
    pg.click(462,387)
    time.sleep(5)
    pg.typewrite(stock)
    time.sleep(5)
    pg.press("down",presses=2)
    time.sleep(5)
    pg.press("enter")
    time.sleep(5)
    pg.click(764,489)
    time.sleep(5)
    pg.click(943,347)
    time.sleep(5)
    pg.click(1357,133)
    time.sleep(5)
    pg.press("pgup",presses=5)
    time.sleep(5)
    
    
