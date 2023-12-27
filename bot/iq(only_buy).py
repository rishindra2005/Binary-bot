from iqoptionapi.stable_api import IQ_Option
#API = IQ_Option("bashokauto@outlook.com","Qwertyuiop@1234")
from iqoptionapi.stable_api import IQ_Option
import logging
import time

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
I_want_money = IQ_Option("bashok2005@outlook.com", "Qwertyuiop@1234")
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