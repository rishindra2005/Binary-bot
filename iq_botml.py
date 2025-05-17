from iqoptionapi.stable_api import IQ_Option
import logging
import time
from datetime import datetime
import numpy as np
import pandas as pd
import time
import joblib
import warnings
import os
from load_env import load_env, get_env
warnings.filterwarnings("ignore", category=DeprecationWarning)
def warn(*args, **kwargs):
    pass
warnings.warn = warn
warnings.filterwarnings("ignore", category=FutureWarning)
etime=time.time()

# Load environment variables from .env file
load_env()

# Get credentials from environment variables
IQ_EMAIL = get_env('IQ_EMAIL')
IQ_PASSWORD = get_env('IQ_PASSWORD')

# Initialize IQ_Option with credentials from environment variables
I_want_money = IQ_Option(IQ_EMAIL, IQ_PASSWORD)
I_want_money.connect()  # connect to iqoption
goal = "EURJPY" #ASSET
time_frame = 60 # pred only for 60
loc='random_forest1.joblib' # location of saved weights 
# loc='random_forest2.joblib'
money = 1 #inetial money
pe = 80  # percentage return

## Don't edid any thing below this

net="nul"
# def clean():
#     global df
#     x=0
#     while x<199:
#         ip=f'id_{x}'
#         from1 =f'from_{x}'
#         to1=f'to_{x}'
#         df=df.drop([ip,from1,to1], axis = 1)
#         x=x+1
x=0
df = []
null = []
nup= pd.DataFrame(null)
df = pd.DataFrame(df)
while x<198:
    df[f"id_{x}"]=null
    df[f"from_{x}"]=null
    df[f"to_{x}"]=null
    df[f"open_{x}"]=null
    df[f"close_{x}"]=null
    df[f"min_{x}"]=null
    df[f"max_{x}"]=null
    df[f"volume_{x}"]=null
    df[f"color_{x}"]=null
    x = x+1        
def pred(df):
    global loc
    global net
    global goal
    etime=time.time()
    # try:
        # etime=etime
    c = I_want_money.get_candles(goal,60,198,etime)
    c = pd.DataFrame(c)
    c = c.drop(['at'], axis=1)
    p= []
    count = len(c['id'])
    x=1
    k=[]
    k = c['open']-c['close']
    for k in k:
        if k<=0:
            p=np.append(p,1)
        else:
            p=np.append(p,2)
    c['color']=p
    x=0
    pp = []
    while x<198:
        kp = c.iloc[[x]]
        kp=kp.to_numpy()
        kp=kp.flatten()
        pp=np.concatenate((pp, kp), axis=0)
        x = x+1
    data_to_append = {}
    for i in range(len(df.columns)):
        data_to_append[df.columns[i]] = pp[i]
    df = df.append(data_to_append, ignore_index = True)
    x=0
    while x<198:
        ip=f'id_{x}'
        from1 =f'from_{x}'
        to1=f'to_{x}'
        df=df.drop([ip,from1,to1], axis = 1)
        x=x+1
    regp = joblib.load(loc)
    kill = regp.predict(df)
    net=''.join(str(i) for i in kill)
    net=round(float(net))
    net=int(net)

    # except:
    #     print("calc: data input error")
    return
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


from datetime import datetime

balancep = I_want_money.get_balance()
now = datetime.now()
net='null'
pred(df)
current_time = now.strftime("%H:%M:%S")

print(goal,balancep,current_time,loc)
t = now.strftime("%S")    
while True:
    x = money
    y=((100/pe)*x)
    ACTIVES = goal
    #ACTION = "call"  # or "put"
    expirations_mode = 1
    if x>I_want_money.get_balance():
        x=I_want_money.get_balance()
    if net==1:
        check, id = I_want_money.buy(x, ACTIVES, "call", expirations_mode)
    elif net==2:
        check, id = I_want_money.buy(x, ACTIVES, "put", expirations_mode)
    else:
        print('ERROR')
        break
    time.sleep(26)
    pred(df)
    p = I_want_money.check_win_v3(id)
        

    if p > 0:
        print("win")
    elif p == 0:
        print("null")    
    else:
        while p<0:
            print("lose")
            x=(100/pe)*y +0.5
            x = round(x)
            if x>300:
                print("-----------------fuck_off--------------------------")
            # x = x+y
            if x>I_want_money.get_balance():
                x=I_want_money.get_balance()
            if net==1:
                check, id = I_want_money.buy(x, ACTIVES, "call", expirations_mode)
            elif net==2:
                check, id = I_want_money.buy(x, ACTIVES, "put", expirations_mode)
            else:
                print('ERROR')
                break
            time.sleep(55)
            pred(df)
            p = I_want_money.check_win_v3(id)
            
            if p > 0:
                print("win")
                break
            elif p == 0 :
                while p==0 :
                    print("null")
                    if x>I_want_money.get_balance():
                        x=I_want_money.get_balance()    
                    if net==1:
                        check, id = I_want_money.buy(x, ACTIVES, "call", expirations_mode)
                    elif net==2:
                        check, id = I_want_money.buy(x, ACTIVES, "put", expirations_mode)
                    else:
                        print('ERROR')
                        break
                        #check, id = I_want_money.buy(x, ACTIVES, ACTION, expirations_mode)     
                    time.sleep(55)
                    pred(df)
                    p = I_want_money.check_win_v3(id)
            else:
                y = x+y
                