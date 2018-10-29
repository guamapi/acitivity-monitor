import sqlite3

class readDB(object):
    def __init__(self,file_path):
        self.file_path = file_path
        self.conn = sqlite3.connect(self.file_path)
        self.c = self.conn.cursor()

    def getKeyboard():
        for row in c.execute('select * from kt'):
            return row

    def getMouse():
        for row in c.execute('select * from ml'):
            return row

    def getMousemap():
        for row in c.execute('select * from mousemap'):
            return row

    def getWindowname():
        for row in c.execute('select * from mw'):
            print row
