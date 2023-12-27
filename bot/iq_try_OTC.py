from iqoptionapi.stable_api import IQ_Option
#API = IQ_Option("bashokauto@outlook.com","Qwertyuiop@1234")
from iqoptionapi.stable_api import IQ_Option
import logging
import time

#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
I_want_money = IQ_Option("bashokauto@outlook.com", "Qwertyuiop@1234")
I_want_money.connect()  # connect to iqoption
goal = "EURUSD"
time_frame = 60
maxdict = 1

I_want_money.start_candles_stream(goal,time_frame,maxdict)
balancep = I_want_money.get_balance()
print(balancep,goal,time_frame)
CART = I_want_money.get_realtime_candles(goal,time_frame)
for CARTS in list(CART.keys()):
    open = (CART[CARTS]['open'])
    close = (CART[CARTS]['close'])
    net = open - close 
    break
    
while True:
    x = 1
    ACTIVES = goal
    #ACTION = "call"  # or "put"
    expirations_mode = 1
    
    CART = I_want_money.get_realtime_candles(goal,time_frame)
    for CARTS in list(CART.keys()):
        open = (CART[CARTS]['open'])
        close = (CART[CARTS]['close'])
        net = open - close 
        break
        
    if net>=0:
        check, id = I_want_money.buy(x, ACTIVES, "call", expirations_mode)
    else:
        check, id = I_want_money.buy(x, ACTIVES, "put", expirations_mode)
    p = I_want_money.check_win_v3(id)
    if p > 0:
        print("win")
    elif p == 0:
        print("null")    
    else:
        while p<0:
            print("lose")
            y = x
            y = y*2
            #x = x+0.5
            x = round(y)
                      
            CART = I_want_money.get_realtime_candles(goal,time_frame)
            for CARTS in list(CART.keys()):
                open = (CART[CARTS]['open'])
                close = (CART[CARTS]['close'])
                net = open - close
                break
                
            if net>=0:
                check, id = I_want_money.buy(x, ACTIVES, "call", expirations_mode)
            else:
                check, id = I_want_money.buy(x, ACTIVES, "put", expirations_mode)

                #check, id = I_want_money.buy(x, ACTIVES, ACTION, expirations_mode)
            p = I_want_money.check_win_v3(id)
            
            if p > 0:
                print("win")
                break
            elif p == 0 :
                while p==0 :
                    print("null")
                    CART = I_want_money.get_realtime_candles(goal,time_frame)
                    for CARTS in list(CART.keys()):
                        open = (CART[CARTS]['open'])
                        close = (CART[CARTS]['close'])
                        net = open - close
                        break
                        
                    if net>=0:
                        check, id = I_want_money.buy(x, ACTIVES, "call", expirations_mode)
                    else:
                        check, id = I_want_money.buy(x, ACTIVES, "put", expirations_mode)

                        #check, id = I_want_money.buy(x, ACTIVES, ACTION, expirations_mode)
                    p = I_want_money.check_win_v3(id)
                