from iqoptionapi.stable_api import IQ_Option
#API = IQ_Option("bashokauto@outlook.com","Qwertyuiop@1234")
from iqoptionapi.stable_api import IQ_Option
import logging
import time
from datetime import datetime
import pandas as pd
import os
from load_env import load_env, get_env

# Load environment variables from .env file
load_env()

# Get credentials from environment variables
IQ_EMAIL = get_env('IQ_EMAIL')
IQ_PASSWORD = get_env('IQ_PASSWORD')

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
I_want_money = IQ_Option(IQ_EMAIL, IQ_PASSWORD)
I_want_money.connect()
# I_want_money.change_balance("REAL")
goal = "EURJPY"
time_frame = 60
maxdict = 1
from datetime import datetime
I_want_money.start_candles_stream(goal,time_frame,maxdict)
balancep = I_want_money.get_balance()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
print(balancep,goal,time_frame)
CART = I_want_money.get_realtime_candles(goal,time_frame)
for CARTS in list(CART.keys()):
    open = (CART[CARTS]['open'])
    close = (CART[CARTS]['close'])
    net = open - close 
    break
now = datetime.now()
pe = 80
t = now.strftime("%S")
tim=0.7
init=1
while True:
    x = init
    y = (100/pe)*x
    ACTIVES = goal
    #ACTION = "call"  # or "put"
    expirations_mode = 1
    time.sleep(tim)    
    if net<=0:
        check, id = I_want_money.buy(x, ACTIVES, "call", expirations_mode)
    else:
        check, id = I_want_money.buy(x, ACTIVES, "put", expirations_mode)
    time.sleep(28)
    p = I_want_money.check_win_v3(id)
    CART = I_want_money.get_realtime_candles(goal,time_frame)
    for CARTS in list(CART.keys()):
        open = (CART[CARTS]['open'])
        close = (CART[CARTS]['close'])
        net = open - close 
        break
    if p > 0:
        print("win")
    elif p == 0:
        print("null")    
    else:
        while p<0:
            print("lose")
            x=(100/pe)*y +0.5
            x = round(x)
           # x = x+init
            time.sleep(tim)    
            if x>I_want_money.get_balance():
                x=I_want_money.get_balance()
            if net<=0:
                check, id = I_want_money.buy(x, ACTIVES, "call", expirations_mode)
            else:
                check, id = I_want_money.buy(x, ACTIVES, "put", expirations_mode)
            time.sleep(58)

            p = I_want_money.check_win_v3(id)
            CART = I_want_money.get_realtime_candles(goal,time_frame)
            for CARTS in list(CART.keys()):
                open = (CART[CARTS]['open'])
                close = (CART[CARTS]['close'])
                net = open - close 
                break
            if p > 0:
                print("win")
                break
            elif p == 0 :
                while p==0 :
                    print("null")
                    time.sleep(tim)    
                    if x>I_want_money.get_balance():
                            x=I_want_money.get_balance()
                    if net <= 0:
                        check, id = I_want_money.buy(x, ACTIVES, "call", expirations_mode)
                    else:
                        check, id = I_want_money.buy(x, ACTIVES, "put", expirations_mode)
                    time.sleep(58)
                    p = I_want_money.check_win_v3(id)
                    CART = I_want_money.get_realtime_candles(goal,time_frame)
                    for CARTS in list(CART.keys()):
                        open = (CART[CARTS]['open'])
                        close = (CART[CARTS]['close'])
                        net = open - close 
                        break
            else:
                y = x+y