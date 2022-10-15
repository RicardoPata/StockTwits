# -*- coding: utf-8 -*-
"""
Created on Mon May  8 23:45:53 2022

@author: Richie Paw

Use this Bot to spam other boards on stocktwits , using library pyautogui to simulate mouse and keyboard moves

Line 20, Stock symbols its a text file with bio stocks 

Def Post - will get each stock on stocksymbols and will write on stocktwits  1st stock message A, 2nd stock message B, 3rd stock Message A.

Message A and Message B must be different

Def Comment - Go to your profile on stocktwits, to each post you made, will open it and write the stock you want to link to it.

Def comment its useful because on stocktwits you shouldnt tag 2 different stocks 
 
-----------------------
Attention: 
    
coordinates must be updated according to your monitor size / resolution

Go to StockTwits_Message_Rev_0_Rev_0, save a copy of this file with a different name for now,
change pg.click to pg.moveTo and check if coordinantes matche. 
If coordinates dont match, on console move your mouse to the position where the button is and write on console pg.position() ,
this will give you the coordinates

-
1 - update on github
"""

#libraries used

from StockTwits_Message_Rev_0 import Message
from StockTwits_Comment_Rev_0 import Comment
import pyautogui as pg
import time
from datetime import datetime

#code

Symbols = []

with open("StockSymbols.txt") as file:
    for line in file: 
        line = line.strip() #preprocessing
        Symbols.append(line) #storing everything in list
        
size = len(Symbols)   
file.close()

time.sleep(5)

messageA = '''Hi guys, sorry to come in your board spamming. Please don't report, if i'm bothering you, just comment "stop", and i will not come to this board again.

I'm software developer that enjoys trading. Recently i created a algorithm to look for trade opportunities which also alerts to my discord.

I've been backtesting this for the past 2 weeks and looks ok so far. 

Im opening my discord for free to anyone that wants to join and receives the alerts. Use it at your own risk, do not trade on the first day, see for yourself how it works and if it suits your risk management.

The alerts consists on day trading penny stocks / stock options -> 2-6 alerts per day.

https://discord.gg/cvJhUBMM
'''


messageB = '''Hello, guys sorry to come to your board spamming. Please don't report, if i'm bothering you, just write "stop", and i will not come to this board again.

I'm software developer that enjoys trading.
Recently i created a algorithm to look for trade opportunities which also alerts to my discord.

Im opening my discord for free to anyone that wants to join and receives the alerts. Use it at your own risk, do not trade on the first day, see for yourself how it works and if it suits your risk management. 
I've been backtesting this for the past 2 weeks and looks ok so far. 

The alerts consists on stock options / day trading penny stocks -> 2-6 alerts per day.

https://discord.gg/cvJhUBMM
'''

def Post():    # write posts on stocktwits 
    
    DifferentMessage = False
    for each_stock in Symbols:    
        
        today = datetime.now()
    
        if DifferentMessage == False:
            stockMessage = str('\n {} \n \n{} \n \n {}').format(each_stock,messageA,today)
            #print(stockMessage)
            Message(stockMessage)
            time.sleep(5)
            DifferentMessage = True
        
        else:
            stockMessage = str('\n {} \n \n {} \n \n {}').format(each_stock,messageB,today)
            #print(stockMessage)
            Message(stockMessage)
            time.sleep(5)
            DifferentMessage = False
    

def Comentarios(): 
    
    for posts in range(size):
        today = datetime.now()
        MensagemComentario = str('$BFRI {}').format(today)
        time.sleep(2)
        #print(MensagemComentario)
        Comment(MensagemComentario)
        time.sleep(2)


Post()  
      
# pg.click(x=1184, y=95) # go to your profile
# time.sleep(2)
# pg.click(x=1135, y=146)

# #Comentarios()

# pg.click(x=14, y=743) # power off your computer
# time.sleep(2)
# pg.click(x=14, y=700)
# time.sleep(2)
# pg.click(x=14, y=620)
    
    