import pythoncom, pyHook,time,os,datetime
import sqlite3

conn = sqlite3.connect('c:\\users\\shengyu\\desktop\\stat.db')
c=conn.cursor()
c.execute('''CREATE TABLE mw(time int, seq real)''')
conn.commit()
conn.close()

l=0
ws=[]

def OnMouseEvent(event):
     
     global l,ws
     #if the next name is the same as the one before
     #do not record this name
     if event.WindowName!=None:
          if 'outlook' in event.WindowName.lower():
               event.WindowName='Outlook'
          if 'facebook' in event.WindowName:
               event.WindowName=
          ws.append(event.WindowName+",")
          l=l+1
          if l!=1:
               m=len(ws)
               if ws[m-1]==ws[m-2]:
                    ws.pop()
          #print ws
     if len(ws)==5:
          l=0
          conn = sqlite3.connect('c:\\users\\shengyu\\desktop\\stat.db')
          c=conn.cursor()
          current_time=int(time.strftime("%H%M"))
          sequence=''.join(ws)
          print ws
          c.execute("INSERT INTO mw(time,seq) VALUES (?,?)",
                    (current_time,sequence))
          conn.commit()
          conn.close()
          ws=[]
                    
     return True


hm=pyHook.HookManager()
hm.MouseAll=OnMouseEvent
hm.HookMouse()
pythoncom.PumpMessages()
hm.UnhookMouse()

