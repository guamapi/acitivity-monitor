import win32gui
import win32process
import win32api
import numpy as np
from array import array
from time import sleep
from win32api import GetSystemMetrics
import sqlite3
import math

l=0
#take user input
x=[]
fg_win = win32gui.GetForegroundWindow()
fg_thread, fg_process = win32process.GetWindowThreadProcessId(fg_win)
current_thread = win32api.GetCurrentThreadId()
win32process.AttachThreadInput(current_thread, fg_thread, True)
m=np.ndarray(shape=(GetSystemMetrics (0),GetSystemMetrics (1)),dtype=int)
while True:    
    l=l+1
    sleep(1)
    m[win32gui.GetCursorPos()[0],win32gui.GetCursorPos()[1]]=m[win32gui.GetCursorPos()[0],win32gui.GetCursorPos()[1]]+1
    if l==60*n:        
    	for x in range(0, m.shape[0]):
        	for y in range(0, m.shape[1]):
                    	if m[x, y] ==1:
                            	m[x, y] = 0
                            	
conn = sqlite3.connect('c:\\users\shengyu\\desktop\\stat.db')
c = conn.cursor()
for row in c.execute('select map from mousemap'):
    if l==0:
        a=''.join(row)
        a=''.join(d for d in a if d.isdigit())
        a=list(a)
        a=np.array(a)
        b=[int(s) for s in a]
        b=np.asarray(b)
        #txt_file=open("c:\\users\\shengyu\\desktop\\1.txt","w")
        #txt_file.write(a)
        #txt_file.close()
        print b.reshape(1280,720),np.linalg.norm(b)
        l=l+1
    	#compare the user input with the database
    	z=max(np.count_nonzero(m),np.count_nonzero(b))
    	th=sqrt(2*z)
        th_m=abs(m-b)
    	if np.linalg.norm(th_m)<th:
       	print "ok"
    	else:
       	print "not ok"
