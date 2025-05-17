import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk
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
root = tk.Tk()
net="nul"
x=0
I_want_money ="null"
money = 1
status="free"
net='null'
net1="bull"
net2="null"
net3="null"
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
while x<198:
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
x=198
while x<396:
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
x=396
while x<594:
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
def pred(df1,df2,df3,df):
    global loc
    global net
    global goal
    etime=time.time()
    try:
        etime=etime
        c = I_want_money.get_candles(goal[0],60,198,etime)
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
        for i in range(len(df1.columns)):
            data_to_append[df1.columns[i]] = pp[i]
        df1 = df1.append(data_to_append, ignore_index = True)
        x=0
        while x<198:
            ip=f'id_{x}'
            from1 =f'from_{x}'
            to1=f'to_{x}'
            df1=df1.drop([ip,from1,to1], axis = 1)
            x=x+1
        #==============================================================================
        c = I_want_money.get_candles(goal[1],60,198,etime)
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
        for i in range(len(df2.columns)):
            data_to_append[df2.columns[i]] = pp[i]
        df2 = df2.append(data_to_append, ignore_index = True)
        x=198
        while x<396:
            ip=f'id_{x}'
            from1 =f'from_{x}'
            to1=f'to_{x}'
            df2=df2.drop([ip,from1,to1], axis = 1)
            x=x+1
        #==============================================================================
        c = I_want_money.get_candles(goal[2],60,198,etime)
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
        for i in range(len(df3.columns)):
            data_to_append[df3.columns[i]] = pp[i]
        df3 = df3.append(data_to_append, ignore_index = True)
        x=396
        while x<594:
            ip=f'id_{x}'
            from1 =f'from_{x}'
            to1=f'to_{x}'
            df3=df3.drop([ip,from1,to1], axis = 1)
            x=x+1
        #==============================================================================
        df=df=pd.concat([df1, df2, df3], axis=1)
        global net1
        global net2
        global net3
        regp = joblib.load("random_forest28000_1.joblib")
        kill = regp.predict(df)
        net=''.join(str(i) for i in kill)
        net=round(float(net))
        net1=int(net)
        regp = joblib.load("random_forest_1.joblib")
        kill = regp.predict(df)
        net=''.join(str(i) for i in kill)
        net=round(float(net))
        net2=int(net)
        regp = joblib.load("random_forest_2.joblib")
        kill = regp.predict(df)
        net=''.join(str(i) for i in kill)
        net=round(float(net))
        net3=int(net)
        net=net1+net2+net3
        if net<5:
            net=1
        else:
            net=2    
    except:
        print("calc: data input error")
        time.sleep(60)




PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "bot.ui"

def run():
    mainwindow.mainloop()
def login():
    global I_want_money
    e=email.get()
    p=pasword.get()
    I_want_money = IQ_Option(e,p)
    I_want_money.connect()
def balance():
    b=I_want_money.get_balance()
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    balance_l.configure(font='TkDefaultFont', height='4', text=f"{b} {time} EURJPY ", width='50')
    print(b)
def start():
    global money
    global status
    global I_want_money
    global goal
    global net
    global pe

    money=int(money.get())
    pe=int(pe.get())
    pred(df1,df2,df3,df)
    if status=="free":
        x = money
        y=((100/pe)*x)
        ACTIVES = goal[2]
        expirations_mode = 1
        if x>I_want_money.get_balance():
            x=I_want_money.get_balance()
        if net==1:
            check, id = I_want_money.buy(x, ACTIVES, "call", expirations_mode)
        elif net==2:
            check, id = I_want_money.buy(x, ACTIVES, "put", expirations_mode)
        else:
            print("error")
            log.configure(compound='top', height='2', text='ERROR', width='75')
            # break
        time.sleep(24)
        pred(df1,df2,df3,df)
        p = I_want_money.check_win_v3(id)

        if p > 0:
            print(f"win {x}")
            log.configure(compound='top', height='2', text=f"win {x}", width='75')
        elif p == 0:
            print(f"null {x}")
            log.configure(compound='top', height='2', text=f"null {x}", width='75')
        else:
            while p<0:
                print(f"lose {x}")
                log.configure(compound='top', height='2', text=f"lose {x}", width='75')
                x=(100/pe)*y +0.5
                x = round(x)
                # x = x+y
                if x>300:
                    print("8 times reached")
                    log.configure(compound='top', height='2', text='8 times reached', width='75')
                    break
                if x>I_want_money.get_balance():
                    x=I_want_money.get_balance()
                if net==1:
                    check, id = I_want_money.buy(x, ACTIVES, "call", expirations_mode)
                elif net==2:
                    check, id = I_want_money.buy(x, ACTIVES, "put", expirations_mode)
                else:
                    print('ERROR')
                    log.configure(compound='top', height='2', text='ERROR', width='75')
                    break
                time.sleep(50)
                pred(df1,df2,df3,df)
                p = I_want_money.check_win_v3(id)
                if p > 0:
                    print(f"win {x}")
                    log.configure(compound='top', height='2', text=f"win {x}", width='75')
                    break
                elif p == 0 :
                    while p==0 :
                        print(f"null {x}")
                        log.configure(compound='top', height='2', text=f"null {x}", width='75')
                        
                        if x>I_want_money.get_balance():
                            x=I_want_money.get_balance()    
                        if net==1:
                            check, id = I_want_money.buy(x, ACTIVES, "call", expirations_mode)
                        elif net==2:
                            check, id = I_want_money.buy(x, ACTIVES, "put", expirations_mode)
                        else:
                            print('ERROR')
                            log.configure(compound='top', height='2', text='ERROR', width='75')
                            break
                        time.sleep(50)
                        pred(df1,df2,df3,df)
                        p = I_want_money.check_win_v3(id)
                else:
                    y = x+y
        root.update()            
def stop():
    global status
    status="stop"

frame1 = tk.Frame(None)
frame2 = tk.Frame(frame1)
email = tk.Entry(frame2)
bash = tk.StringVar(value='bashok2005@outlook.com')
email.configure(font='TkTextFont', justify='left', relief='raised', takefocus=False)
email.configure(textvariable=bash, width='30')
_text_ = '''bashok2005@outlook.com'''
email.delete('0', 'end')
email.insert('0', _text_)
email.pack(padx='5', pady='18', side='top')
pasword = tk.Entry(frame2)
pasword.configure(show='•')
_text_ = '''Asdfghjkl_1234'''
pasword.delete('0', 'end')
pasword.insert('0', _text_)
pasword.pack(padx='5', side='left')
button1 = tk.Button(frame2)
button1.configure(text='Login',command=login)
button1.pack(side='top')
frame2.configure(background='lightblue', borderwidth='5', height='70', padx='5')
frame2.configure(pady='5', width='600')
frame2.pack(side='top')
frame5 = tk.Frame(frame1)
frame4 = tk.Frame(frame5)
money = tk.Entry(frame4)
_text_ = '''1'''
money.delete('0', 'end')
money.insert('0', _text_)
money.pack(padx='5', pady='5', side='top')
REAL = tk.Button(frame4)
REAL.configure(compound='top', font='TkDefaultFont', height='4', justify='left')
REAL.configure(takefocus=False, text='REAL')
REAL.pack(padx='5', pady='5', side='left')
Start = tk.Button(frame4)
Start.configure(height='3', text='start',command=start)
Start.pack(fill='x', padx='5', pady='5', side='top')
pe = ttk.Entry(frame4)
_text_ = '''80'''
pe.configure(width='10')
pe.pack(side='top')
frame4.configure(background='light blue', borderwidth='10', height='130', takefocus=True)
frame4.configure(width='100')
frame4.pack(padx='5', pady='5', side='left')
frame8 = tk.Frame(frame5)
banance = tk.Button(frame8)
banance.configure(anchor='ne', text='banance',command=balance)
banance.pack(padx='5', pady='5', side='top')
balance_l = tk.Label(frame8)
balance_l.configure(font='TkDefaultFont', height='4', text='balance_l', width='50')
balance_l.pack(padx='5', pady='5', side='top')
frame8.configure(background='pink', height='130', width='480')
frame8.pack(padx='5', pady='5', side='right')
frame5.configure(background='lightgreen', height='130', width='600')
frame5.pack(padx='5', pady='5', side='top')
frame6 = tk.Frame(frame1)
log = tk.Label(frame6)
log.configure(compound='top', height='2', text='log', width='75')
log.pack(padx='5', pady='5', side='top')
frame6.configure(height='100', relief='ridge', width='600')
frame6.pack(side='top')
frame11 = tk.Frame(frame1)
STOP = tk.Button(frame11)
STOP.configure(height='5', overrelief='raised', text='Stop', width='65',command=stop)
STOP.pack(side='left')
E_stop = tk.Button(frame11)
E_stop.configure(height='5', text='emergencystop')
E_stop.pack(padx='5', side='top')
frame11.configure(background='lightgray', height='100', relief='ridge', width='600')
frame11.pack(padx='5', pady='5', side='left')
frame1.configure(background='darkgray', borderwidth='5', height='500', width='600')
frame1.pack(side='top')

# Main widget
# mainwindow = frame1
    

    

## EDITABLE
goal = ["EURUSD","USDJPY","EURJPY"] #ASSET
time_frame = 60 # pred only for 60
root.mainloop()