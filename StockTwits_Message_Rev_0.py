import pyautogui as pg
import time

def Message(stock):

    pg.press("esc")
    time.sleep(2)
    #pg.click(x=1189,y=399) #click on post button
    #time.sleep(5)
    pg.click(x=860, y=378) #click to comment area
    time.sleep(5)
    pg.typewrite(stock)  #write comment
    time.sleep(5)
    #pg.press("down",presses=2)
    #time.sleep(5)
    #pg.press("enter")
    #time.sleep(5)
    pg.click(x=1024, y=931) #click on bullish button
    time.sleep(5)
    pg.moveTo(x=1203, y=383) #click on post message button
    time.sleep(5)
    pg.click(x=1912, y=79) # go up
    time.sleep(5)
    pg.press("pgup",presses=5)
    time.sleep(5)
    
    
