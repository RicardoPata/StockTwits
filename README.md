# StockTwits
Use this Bot to spam other boards on stocktwits , using library pyautogui to simulate mouse and keyboard moves
Bot to create posts (stocks symbols  + message ). Also able to comment on your own posts to link to your stock symbol as you cant write 2 stock symbols on same message on stocktwits

Bot_stocktwits_post_comment is the main file that use other 2 libraries

def post will just create new posts

def comment will go to your profile and start comment on your own posts

-------------------


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
