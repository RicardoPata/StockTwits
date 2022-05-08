# -*- coding: utf-8 -*-
"""
Created on Tue May  3 02:51:06 2022

@author: Asus
"""
import pyautogui as pg
import time

x = 0
def Comment(stockComentario):
    global x
    pg.press("esc")
    time.sleep(1)
    pg.press("down",presses=3)
    time.sleep(2)
    pg.click(680,600) #click on comment button
    time.sleep(1)
    pg.moveTo(450,550) #move to comment area
    time.sleep(3)
    pg.typewrite(stockComentario) #write comment
    time.sleep(3)
    pg.press("left",presses=1)
   # pg.press("enter")
    time.sleep(3)
    pg.click(760,620) #click on bullish button
    time.sleep(1)
    pg.click(950,550) #click on post message button
    time.sleep(1)
    pg.moveTo(680,600) # go down to next post. After 3 posts, go down 15 clicks to start again
    if x <3:    
        pg.press("down",presses=10)
        
    else:
        pg.press("down",presses=15)
        x=0
    x =+ 1
    
    