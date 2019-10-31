import pyHook, pythoncom, sys, datetime, time
from time import sleep
import sqlite3

conn = sqlite3.connect('c:\\users\\shengyu\\desktop\\stat.db')
c=conn.cursor()
c.execute('''CREATE TABLE kt(time int, freq real, seq text)''')
conn.commit()
conn.close()

l=0
n=0
du=[]
ts=[]
def OnKeyboardEvent(event):

     global l,n,se,mi,ho,du,ts
     l=l+1
     chr(event.Ascii)
     if event.KeyID==32:
          ts.append('space')
     elif event.KeyID==33:
          ts.append('esc')
     elif event.KeyID==13:
          ts.append('enter')
     elif event.KeyID==162:
          ts.append('ctrl')
     elif event.KeyID==38:
          ts.append('arrow_u')
     elif event.KeyID==40:
          ts.append('arrow_d')
     elif event.KeyID==37:
          ts.append('arrow_l')
     elif event.KeyID==39:
          ts.append('arrow_r')
     elif event.KeyID==9:
          ts.append('tab')
     elif event.KeyID==160:
          ts.append('shift')
     elif event.KeyID==8:
          ts.append('backspace')
     elif event.KeyID==116:
          ts.append('F5')
     else:
          ts.append(chr(event.Ascii))
     print ts
     if l==1+20*n:
          se=datetime.datetime.now().second
          mi=datetime.datetime.now().minute
          ho=datetime.datetime.now().hour
          
     elif l==1+20*(n+1):
          du_se=datetime.datetime.now().second-se
          du_mi=datetime.datetime.now().minute-mi
          du_ho=datetime.datetime.now().hour-ho
          du_to=du_ho*3600+du_mi*60+du_se
          du.append(du_to)
          if n==0:
               f=600/du[0]
          else:
               f=600/(du[n]-du[n-1])
          n=n+1
          conn = sqlite3.connect('c:\\users\\shengyu\\desktop\\stat.db')
          c=conn.cursor()
          current_time=int(time.strftime("%H%M"))
          sequence=''.join(ts)
          c.execute("INSERT INTO kt(time,freq,seq) VALUES (?,?,?)",
                    (current_time,f,sequence))
          conn.commit()
          conn.close()
          del ts[:]
          print f
     else:
          return True
     return True

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
hm.UnHookKeyboard

