import win32gui
import win32process
import win32api
import time,os,datetime
from time import sleep
import sqlite3
import numpy as np
from array import array
from win32api import GetSystemMetrics

conn = sqlite3.connect('c:\\users\\shengyu\\desktop\\stat.db')
c=conn.cursor()
c.execute('''CREATE TABLE mousemap(time int, map text)''')
conn.commit()
conn.close()

x=[]
l=0
n=1

fg_win = win32gui.GetForegroundWindow()
fg_thread, fg_process = win32process.GetWindowThreadProcessId(fg_win)
current_thread = win32api.GetCurrentThreadId()
win32process.AttachThreadInput(current_thread, fg_thread, True)
m=np.ndarray(shape=(GetSystemMetrics (0),GetSystemMetrics (1)),dtype=int)
while True:    
    l=l+1
    sleep(0.2)
    m[win32gui.GetCursorPos()[0],win32gui.GetCursorPos()[1]]=m[win32gui.GetCursorPos()[0],win32gui.GetCursorPos()[1]]+1
    if l==3000*n:
        for x in range(0,m.shape[0]):
            for y in range(0,m.shape[1]):
                if m[x,y]==1:
                    m[x,y]==0
        n=n+1
        conn = sqlite3.connect('c:\\users\\shengyu\\desktop\\stat.db')
        c=conn.cursor()
        current_time=int(time.strftime("%H%M"))
        a="".join(str(e) for e in m)
        print type(a)
        c.execute("INSERT INTO mousemap(time,map) VALUES (?,?)",(current_time,a))
        conn.commit()
        conn.close()
        x=[]
