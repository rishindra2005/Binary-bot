import logging
import time
from datetime import datetime
import numpy as np
import pandas as pd
import time
import joblib
import warnings
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
warnings.filterwarnings("ignore", category=DeprecationWarning)
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings("ignore", category=FutureWarning)
from iqoptionapi.stable_api import IQ_Option
from load_env import load_env, get_env
#API = IQ_Option("bashokauto@outlook.com","Qwertyuiop@1234")
etime=time.time()

## EDITABLE


# Load environment variables from .env file
load_env()

# Get credentials from environment variables
IQ_EMAIL = get_env('IQ_EMAIL')
IQ_PASSWORD = get_env('IQ_PASSWORD')

# I_want_money = IQ_Option("bashokauto@outlook.com", "Qwertyuiop@1234")
I_want_money = IQ_Option(IQ_EMAIL, IQ_PASSWORD)
I_want_money.connect()  # connect to iqoption
goal = "EURUSD" #ASSET
time_frame = 60 # pred only for 60
loc1='random_forest.joblib'
loc2= 'DecisionTreeClassifier.joblib' # location of saved weights 
money = 2 #inetial money
pe = 80  # yield percentage


## Don't edid any thing below this

net="nul"
df = []
null = []
x=0
nup= pd.DataFrame(null)
df = pd.DataFrame(df)
while x<199:
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
    global net
    global goal
    global net1
    global net2
    global net3
    etime=time.time()-60
    c = I_want_money.get_candles(goal,60,199,etime)
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
    while x<199:
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
    while x<199:
        ip=f'id_{x}'
        from1 =f'from_{x}'
        to1=f'to_{x}'
        df=df.drop([ip,from1,to1], axis = 1)
        x=x+1
    regp = joblib.load(loc1)
    kill = regp.predict(df)
    net=''.join(str(i) for i in kill)
    net=round(float(net))
    net1=int(net)
    regp = joblib.load(loc2)
    kill = regp.predict(df)
    net=''.join(str(i) for i in kill)
    net=round(float(net))
    net2=int(net)
    I_want_money.start_candles_stream(goal,time_frame,1)
    CART = I_want_money.get_realtime_candles(goal,time_frame)
    for CARTS in list(CART.keys()):
        open = (CART[CARTS]['open'])
        close = (CART[CARTS]['close'])
        net3 = open - close
        break
    if net3<=0:
        net3=1
    else:
        net3=2
    net=net1+net2+net3
    return
from datetime import datetime
balancep = I_want_money.get_balance()
now = datetime.now()
net='null'
net1="null"
net2="null"
net3="null"
pred(df)
current_time = now.strftime("%H:%M:%S")
print(goal,balancep,current_time)
t = now.strftime("%S")
while True:
    x = money
    y=((100/pe)*x)
    ACTIVES = goal
    expirations_mode = 1
    if x>I_want_money.get_balance():
        x=I_want_money.get_balance()
    pred(df)
    if net<5:
        check, id = I_want_money.buy(x, ACTIVES, "call", expirations_mode)
    elif net>=5:
        check, id = I_want_money.buy(x, ACTIVES, "put", expirations_mode)
    else:
        print('ERROR')
        break
    time.sleep(28)
    p = I_want_money.check_win_v3(id)
    if p > 0:
        print(f"win {net1} {net2} {net3}")
    elif p == 0:
        print(f"null {net1} {net2} {net3}")
    else:
        while p<0:
            print(f"lose {net1} {net2} {net3}")
            x=(100/pe)*y +0.5
            x = round(x)
            # x = x+y
            if x>I_want_money.get_balance():
                x=I_want_money.get_balance()
            pred(df)
            if net<5:
                check, id = I_want_money.buy(x, ACTIVES, "call", expirations_mode)
            elif net>=5:
                check, id = I_want_money.buy(x, ACTIVES, "put", expirations_mode)
            else:
                print('ERROR')
                break
            time.sleep(50)
            p = I_want_money.check_win_v3(id)
            if p > 0:
                print(f"win {net1} {net2} {net3}")
                break
            elif p == 0 :
                while p==0 :
                    print(f"null {net1} {net2} {net3}")
                    if x>I_want_money.get_balance():
                        x=I_want_money.get_balance()
                    pred(df)
                    if net<5:
                        check, id = I_want_money.buy(x, ACTIVES, "call", expirations_mode)
                    elif net>=5:
                        check, id = I_want_money.buy(x, ACTIVES, "put", expirations_mode)
                    else:
                        print('ERROR')
                        break
                    time.sleep(50)
                    p = I_want_money.check_win_v3(id)
            else:
                y = x+y