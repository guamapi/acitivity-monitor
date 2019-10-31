import pythoncom, pyHook,time,os,datetime
from time import sleep
import sqlite3

conn = sqlite3.connect('c:\\users\\shengyu\\desktop\\stat.db')
c=conn.cursor()
c.execute('''CREATE TABLE ml(time int, freq real)''')
c.execute('''CREATE TABLE mr(time int, freq real)''')
c.execute('''CREATE TABLE ms(time int, freq real)''')
conn.commit()
conn.close()


l=0
r=0
s=0
n=0
o=0
p=0
dl=[]
dr=[]
ds=[]
dp=[]
#left click frequency
def leftclick(event):
    global l,n,se,mi,ho,dl,dp
    dp.append('l')
    l=l+1
    
    if l==1+10*n:
        se=datetime.datetime.now().second
        mi=datetime.datetime.now().minute
        ho=datetime.datetime.now().hour
    elif l==1+10*(n+1):
        du_se=datetime.datetime.now().second-se
        du_mi=datetime.datetime.now().minute-mi
        du_ho=datetime.datetime.now().hour-ho
        du_to=du_ho*3600+du_mi*60+du_se
        dl.append(du_to)
        if n==0:
            f=600/dl[0]
        else:
            f=600/(dl[n]-dl[n-1])
        n=n+1
        conn = sqlite3.connect('c:\\users\\shengyu\\desktop\\stat.db')
        c=conn.cursor()
        current_time=int(time.strftime("%H%M"))
        c.execute("INSERT INTO ml(time,freq) VALUES (?,?)",(current_time,f))
        conn.commit()
        conn.close()
    else:
        return True
    return True
#right
def rightclick(event):
    global r,o,se,mi,ho,dr,dp
    dp.append('r')
    r=r+1
    
    if r==1+10*o:
        se=datetime.datetime.now().second
        mi=datetime.datetime.now().minute
        ho=datetime.datetime.now().hour
    elif r==1+10*(o+1):
        du_se=datetime.datetime.now().second-se
        du_mi=datetime.datetime.now().minute-mi
        du_ho=datetime.datetime.now().hour-ho
        du_to=du_ho*3600+du_mi*60+du_se
        dr.append(du_to)
        if o==0:
            f=600/dr[0]
        else:
            f=600/(dr[o]-dr[o-1])
        o=o+1
        conn = sqlite3.connect('c:\\users\\shengyu\\desktop\\stat.db')
        c=conn.cursor()
        current_time=int(time.strftime("%H%M"))
        c.execute("INSERT INTO mr(time,freq) VALUES (?,?)",(current_time,f))
        conn.commit()
        conn.close()
    else:
        return True
    return True
#scroll
def scroll(event):
    global s,p,se,mi,ho,ds,dp
    dp.append('s')
    s=s+1
    
    if s==1+50*p:
        se=datetime.datetime.now().second
        mi=datetime.datetime.now().minute
        ho=datetime.datetime.now().hour
    elif s==1+50*(p+1):
        du_se=datetime.datetime.now().second-se
        du_mi=datetime.datetime.now().minute-mi
        du_ho=datetime.datetime.now().hour-ho
        du_to=du_ho*3600+du_mi*60+du_se
        ds.append(du_to)
        if p==0:
            f=600/ds[0]
        else:
            f=600/(ds[p]-ds[p-1])
        p=p+1
        conn = sqlite3.connect('c:\\users\\shengyu\\desktop\\stat.db')
        c=conn.cursor()
        current_time=int(time.strftime("%H%M"))
        c.execute("INSERT INTO ms(time,freq) VALUES (?,?)",(current_time,f))
        conn.commit()
        conn.close()
    else:
        return True
    return True
hm=pyHook.HookManager()
hm.MouseLeftDown=leftclick
hm.MouseRightDown=rightclick
hm.MouseWheel=scroll
hm.HookMouse()
pythoncom.PumpMessages()
hm.UnhookMouse()
