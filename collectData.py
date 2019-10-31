import pythoncom, pyHook, time, os, datetime
from time import sleep
import sqlite3
import win32gui
import win32process
import win32api
import numpy as np
from array import array
from win32api import GetSystemMetrics

class userData():
    def __init__(self,file_path):

        self.file_path = file_path
        self.conn = sqlite3.connect(self.file_path)
        self.c = self.conn.cursor()

        #table for mouse left click event
        self.c.execute('''CREATE TABLE ml(time int, freq real)''')
        #table for mouse right click event
        self.c.execute('''CREATE TABLE mr(time int, freq real)''')
        #table for mouse scroll event
        self.c.execute('''CREATE TABLE ms(time int, freq real)''')
        #table for mouse map
        self.c.execute('''CREATE TABLE mousemap(time int, map text)''')
        #table for window name
        self.c.execute('''CREATE TABLE mw(time int, seq real)''')
        #table for keyboard input id
        self.c.execute('''CREATE TABLE kt(time int, freq real, seq text)''')

        self.conn.commit()
        self.conn.close()

        self.left_cnt, self.right_cnt, self.scroll_cnt, self.key_count = 0, 0, 0, 0
        self.dl, self.dr, self.ds, self.dp = [], [], [], []

    def leftclick(event):
        self.dp.append('l')
        self.left_cnt += 1
        n = 0
        #elapsed time of 10 left click
        if self.left_cnt == 1 + 10 * n:
            se = datetime.datetime.now().second
            mi = datetime.datetime.now().minute
            ho = datetime.datetime.now().hour
        elif self.left_cnt == 1 + 10 * (n + 1):
            du_se = datetime.datetime.now().second - se
            du_mi = datetime.datetime.now().minute - mi
            du_ho = datetime.datetime.now().hour - ho
            du_to = du_ho * 3600 + du_mi * 60 + du_se
            self.dl.append(du_to)
            #f for frequency
            if n == 0:
                f = 600 / self.dl[0]
            else:
                f= 600 / (self.dl[n] - self.dl[n - 1])
            n = n + 1
            conn = sqlite3.connect(self.file_path)
            c=conn.cursor()
            current_time=int(time.strftime("%H%M"))
            c.execute("INSERT INTO ml(time,freq) VALUES (?,?)",(current_time,f))
            conn.commit()
            conn.close()
        else:
            return True
        return True

    def rightclick(event):
        self.dp.append('r')
        self.right_cnt += 1
        n = 0
        #elapsed time of 10 right click
        if self.right_cnt == 1 + 10 * o:
            se = datetime.datetime.now().second
            mi = datetime.datetime.now().minute
            ho = datetime.datetime.now().hour
        elif self.right_cnt == 1 + 10 * (o + 1):
            du_se = datetime.datetime.now().second - se
            du_mi = datetime.datetime.now().minute - mi
            du_ho = datetime.datetime.now().hour - ho
            du_to = du_ho * 3600 + du_mi * 60 + du_se
            self.dr.append(du_to)
            #f for frequency
            if o == 0:
                f = 600 / dr[0]
            else:
                f = 600 / (dr[o] - dr[o - 1])
            o = o + 1
            conn = sqlite3.connect(self.file_path)
            c = conn.cursor()
            current_time = int(time.strftime("%H%M"))
            c.execute("INSERT INTO mr(time,freq) VALUES (?,?)",(current_time,f))
            conn.commit()
            conn.close()
        else:
            return True
        return True

    def scroll(event):
        self.dp.append('s')
        self.scroll_cnt += 1
        n = 0
        #elapsed time of 10 scroll
        if self.scroll_cnt == 1 + 50 * p:
            se = datetime.datetime.now().second
            mi = datetime.datetime.now().minute
            ho = datetime.datetime.now().hour
        elif self.scroll_cnt == 1 + 50 * (p + 1):
            du_se = datetime.datetime.now().second - se
            du_mi = datetime.datetime.now().minute - mi
            du_ho = datetime.datetime.now().hour - ho
            du_to = du_ho * 3600 + du_mi * 60 + du_se
            self.ds.append(du_to)
            #f for frequency
            if p == 0:
                f = 600 / ds[0]
            else:
                f = 600 / (ds[p] - ds[p - 1])
            p = p + 1
            conn = sqlite3.connect(self.file_path)
            c = conn.cursor()
            current_time = int(time.strftime("%H%M"))
            c.execute("INSERT INTO ms(time,freq) VALUES (?,?)",(current_time,f))
            conn.commit()
            conn.close()
        else:
            return True
        return True

    def OnMouseEvent(event):
        n = 0
        #record unique window name
        if event.WindowName != None:
            ws.append(event.WindowName + ",")
            l = l + 1
            if l != 1:
                n = len(ws)
                if ws[n - 1] == ws[n - 2]:
                    ws.pop()
        #save a sequence of 10 window names to db
        if l == 1 + 10 * n:
            conn = sqlite3.connect(self.file_path)
            c = conn.cursor()
            current_time = int(time.strftime("%H%M"))
            sequence = ''.join(ws)
            c.execute("INSERT INTO mw(time,seq) VALUES (?,?)",(current_time,sequence))
            conn.commit()
            conn.close()
            return True

    def OnKeyboardEvent(event):

         self.key_count += 1
         n = 0
         chr(event.Ascii)
         if event.KeyID == 32:
              ts.append('SPACE')
         elif event.KeyID == 33:
              ts.append('ESC')
         elif event.KeyID == 162:
              ts.append('CTRL')
         elif event.KeyID == 38:
              ts.append('UP')
         elif event.KeyID == 40:
              ts.append('DOWN')
         elif event.KeyID == 37:
              ts.append('LEFT')
         elif event.KeyID == 39:
              ts.append('RIGHT')
         elif event.KeyID == 9:
              ts.append('TAB')
         else:
              ts.append(chr(event.Ascii))
         #elapsed time of 10 key input
         if self.key_count == 1 + 10 * n:
              se = datetime.datetime.now().second
              mi = datetime.datetime.now().minute
              ho = datetime.datetime.now().hour
         elif self.key_count == 1 + 10 * (n + 1):
              du_se = datetime.datetime.now().second - se
              du_mi = datetime.datetime.now().minute - mi
              du_ho = datetime.datetime.now().hour - ho
              du_to = du_ho * 3600 + du_mi * 60 + du_se
              du.append(du_to)
              #f for frequency
              if n == 0:
                   f = 600 / du[0]
              else:
                   f = 600 / (du[n] - du[n - 1])
              n = n + 1
              conn = sqlite3.connect(self.file_path)
              c = conn.cursor()
              current_time = int(time.strftime("%H%M"))
              sequence = ''.join(ts)
              c.execute("INSERT INTO kt(time,freq,seq) VALUES (?,?,?)",(current_time,f,sequence))
              conn.commit()
              conn.close()
              del ts[:]
         else:
              return True
         return True

if __name__ == '__main__':

    ud = userData('c:\\users\\shengyu\\desktop\\stat.db')
    hm = pyHook.HookManager()
    hm.MouseLeftDown = ud.leftclick
    hm.MouseRightDown = ud.rightclick
    hm.MouseWheel = ud.scroll
    hm.KeyDown = OnKeyboardEvent
    hm.HookMouse()
    hm.HookKeyboard()
    pythoncom.PumpMessages()
    hm.UnhookMouse()
