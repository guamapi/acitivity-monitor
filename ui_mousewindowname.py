import pythoncom, pyHook,time,os,datetime
import sqlite3

conn = sqlite3.connect('c:\\users\\shengyu\\desktop\\stat_temp.db')
c=conn.cursor()
c.execute('''CREATE TABLE mw(time int, seq real)''')

conn.commit()
conn.close()

l=0

n=0
ws=[]

def OnMouseEvent(event):
     
     global l,ws,n
     if event.WindowName!=None:
          ws.append(event.WindowName+",")
          l=l+1
          if l!=1:
               n=len(ws)
               if ws[n-1]==ws[n-2]:
                    ws.pop()               
     if l==1+10*n:
          
          conn = sqlite3.connect('c:\\users\\shengyu\\desktop\\stat.db')
          c=conn.cursor()
          current_time=int(time.strftime("%H%M"))
          sequence=''.join(ws)
          c.execute("INSERT INTO mw(time,seq) VALUES (?,?)",
                    (current_time,sequence))
          conn.commit()
          conn.close()
          n=n+1
     return True


hm=pyHook.HookManager()
hm.MouseAll=OnMouseEvent
hm.HookMouse()
pythoncom.PumpMessages()
hm.UnhookMouse()

