import pyautogui as pg
import time

def Message(stock):

    pg.press("esc")
    time.sleep(1)
    pg.click(1254,105) #click on post button
    time.sleep(5)
    pg.click(462,387) #click to comment area
    time.sleep(5)
    pg.typewrite(stock)  # write comment
    time.sleep(5)
    pg.press("down",presses=2)
    time.sleep(5)
    pg.press("enter")
    time.sleep(5)
    pg.click(764,489) #click on bullish button
    time.sleep(5)
    pg.click(943,347) #click on post message button
    time.sleep(5)
    pg.click(1357,133) # go up
    time.sleep(5)
    pg.press("pgup",presses=5)
    time.sleep(5)
    
    
