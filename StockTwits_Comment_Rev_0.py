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
    pg.click(680,600)
    time.sleep(1)
    pg.moveTo(450,550)
    time.sleep(3)
    pg.typewrite(stockComentario)
    time.sleep(3)
    pg.press("right",presses=1)
   # pg.press("enter")
    time.sleep(3)
    pg.click(760,620)
    time.sleep(1)
    pg.click(950,550)
    time.sleep(1)
    pg.moveTo(680,600)
    if x <3:    
        pg.press("down",presses=10)
        
    else:
        pg.press("down",presses=15)
        x=0
    x =+ 1
    
    