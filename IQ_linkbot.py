from iqoptionapi.stable_api import IQ_Option
import logging
import time
from datetime import datetime
import numpy as np
import pandas as pd
import time
import joblib
import warnings
from sklearn.ensemble import RandomForestClassifier
 
warnings.filterwarnings("ignore", category=DeprecationWarning)
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings("ignore", category=FutureWarning)
from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
etime=time.time()

## EDITABLE


#I_want_money = IQ_Option("bashokauto@outlook.com", "Qwertyuiop@1234")
I_want_money = IQ_Option("bashok2005@outlook.com", "Qwertyuiop@1234")
I_want_money.connect()  # connect to iqoption
goal = ["EURUSD","USDJPY","EURJPY"] #ASSET
time_frame = 60 # pred only for 60
loc='random_forestEU_UJ_EJ_.joblib' # location of saved weights 
money = 1 #inetial money
pe = 80  # percentage return

## Don't edid any thing below this

net="nul"
x=0
df = []
null = []
nup= pd.DataFrame(null)
df = pd.DataFrame(df)
while x<600:
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
df = pd.DataFrame(df)
x=0
df1 = []
null1 = []
nup1= pd.DataFrame(null)
df1 = pd.DataFrame(df1)
while x<199:
    df1[f"id_{x}"]=null1
    df1[f"from_{x}"]=null
    df1[f"to_{x}"]=null
    df1[f"open_{x}"]=null1
    df1[f"close_{x}"]=null1
    df1[f"min_{x}"]=null1
    df1[f"max_{x}"]=null1
    df1[f"volume_{x}"]=null1
    df1[f"color_{x}"]=null1
    x = x+1
df1 = pd.DataFrame(df1)
df2 = []
null1 = []
nup1= pd.DataFrame(null)
df2 = pd.DataFrame(df2)
x=199
while x<398:
    df2[f"id_{x}"]=null1
    df2[f"from_{x}"]=null
    df2[f"to_{x}"]=null
    df2[f"open_{x}"]=null1
    df2[f"close_{x}"]=null1
    df2[f"min_{x}"]=null1
    df2[f"max_{x}"]=null1
    df2[f"volume_{x}"]=null1
    df2[f"color_{x}"]=null1
    x = x+1
df2 = pd.DataFrame(df2)
df3 = []
null1 = []
nup1= pd.DataFrame(null)
df3 = pd.DataFrame(df3)
x=398
while x<597:
    df3[f"id_{x}"]=null1
    df3[f"from_{x}"]=null
    df3[f"to_{x}"]=null
    df3[f"open_{x}"]=null1
    df3[f"close_{x}"]=null1
    df3[f"min_{x}"]=null1
    df3[f"max_{x}"]=null1
    df3[f"volume_{x}"]=null1
    df3[f"color_{x}"]=null1
    x = x+1
df3 = pd.DataFrame(df3)
etime=time.time()        
def pred(df1,df2,df3,df):
    global loc
    global net
    global goal
    etime=time.time()
    try:
        etime=etime
        c = I_want_money.get_candles(goal[0],60,199,etime)
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
        for i in range(len(df1.columns)):
            data_to_append[df1.columns[i]] = pp[i]
        df1 = df1.append(data_to_append, ignore_index = True)
        x=0
        while x<199:
            ip=f'id_{x}'
            from1 =f'from_{x}'
            to1=f'to_{x}'
            df1=df1.drop([ip,from1,to1], axis = 1)
            x=x+1
        #==============================================================================
        etime=time.time()
    #     try:
        # etime=etime
        c = I_want_money.get_candles(goal[1],60,199,etime)
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
        for i in range(len(df2.columns)):
            data_to_append[df2.columns[i]] = pp[i]
        df2 = df2.append(data_to_append, ignore_index = True)
        x=199
        while x<398:
            ip=f'id_{x}'
            from1 =f'from_{x}'
            to1=f'to_{x}'
            df2=df2.drop([ip,from1,to1], axis = 1)
            x=x+1
        #==============================================================================
        etime=time.time()
    #     try:
        # etime=etime
        c = I_want_money.get_candles(goal[2],60,199,etime)
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
        for i in range(len(df3.columns)):
            data_to_append[df3.columns[i]] = pp[i]
        df3 = df3.append(data_to_append, ignore_index = True)
        x=398
        while x<597:
            ip=f'id_{x}'
            from1 =f'from_{x}'
            to1=f'to_{x}'
            df3=df3.drop([ip,from1,to1], axis = 1)
            x=x+1
        #==============================================================================
        df=df=pd.concat([df1, df2, df3], axis=1)
        regp = joblib.load(loc)
        kill = regp.predict(df)
        net=''.join(str(i) for i in kill)
        net=round(float(net))
        net=int(net)
        
        # print(net)

        # print(df)
        #print('s')
    except:
        print("calc: data input error")
    return


from datetime import datetime

balancep = I_want_money.get_balance()
now = datetime.now()
net='null'
pred(df1,df2,df3,df)
current_time = now.strftime("%H:%M:%S")

print(goal,balancep,current_time)
t = now.strftime("%S")    
while True:
    x = money
    y=((100/pe)*x)
    ACTIVES = goal[2]
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
    p = I_want_money.check_win_v3(id)
    pred(df1,df2,df3,df)    

    if p > 0:
        print("win")
    elif p == 0:
        print("null")    
    else:
        while p<0:
            print("lose")
            x=(100/pe)*y +0.5
            x = round(x)
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
            time.sleep(57)
            p = I_want_money.check_win_v3(id)
            pred(df1,df2,df3,df)
            if p > 0:
                print("win")
                break
            elif p == 0 :
                while p==0 :
                    print("null")
                    pred(df1,df2,df3,df)
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
                    time.sleep(57)
                    p = I_want_money.check_win_v3(id)
            else:
                y = x+y
                