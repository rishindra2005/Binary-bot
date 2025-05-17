from iqoptionapi.stable_api import IQ_Option
#API = IQ_Option("bashokauto@outlook.com","Qwertyuiop@1234")
from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
import os
from load_env import load_env, get_env
import logging
import time

# Load environment variables from .env file
load_env()

# Get credentials from environment variables
IQ_EMAIL = get_env('IQ_EMAIL')
IQ_PASSWORD = get_env('IQ_PASSWORD')

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
I_want_money = IQ_Option(IQ_EMAIL, IQ_PASSWORD)
I_want_money.connect()  # connect to iqoption
#I_want_money.reset_practice_balance()
balancep = I_want_money.get_balance()
while True:
    x = 2000
    ACTIVES = "EURUSD"
    ACTION = "call"  # or "put"
    expirations_mode = 1
    check, id = I_want_money.buy(x, ACTIVES, ACTION, expirations_mode)
    time.sleep(53)
    balancen = I_want_money.get_balance()
    p = I_want_money.check_win_v3(id)
    if p >= 0:
        print("win")

    else:   
        while p < 0:
            print("lose")
            x = x + x*0.8
            x = x+0.5
            x = round(x)
            check, id = I_want_money.buy(x, ACTIVES, ACTION, expirations_mode)
            balancen = I_want_money.get_balance()
            p = I_want_money.check_win_v3(id)
            if p >= 0:
                print("win")