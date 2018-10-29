import sqlite3

class readDB(object):
    def __init__(self,file_path):
        self.file_path = file_path
        self.conn = sqlite3.connect(self.file_path)
        self.c = self.conn.cursor()
    #return keyboard input
    def getKeyboard():
        for row in c.execute('select * from kt'):
            return row
    #return mouse click
    def getMouse():
        for row in c.execute('select * from ml'):
            return row
    #return mouse map
    def getMousemap():
        for row in c.execute('select * from mousemap'):
            return row
    #return window name
    def getWindowname():
        for row in c.execute('select * from mw'):
            print row
