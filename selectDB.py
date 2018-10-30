import sqlite3
class selectDB(object):

    def __init__(self,file_path):
        self.file_path = file_path
        self.conn = sqlite3.connect(self.file_path).cursor()

    #return keyboard input
    def getKey():
        for row in conn.execute('select * from kt'):
            return row

    #return mouse frequency
    def getMouseFreq():
        for row in c.execute('select * from ml'):
            return row
    #return mouse map
    def getMousemap():
        for row in c.execute('select * from mousemap'):
            return row

    #return window name
    def getWindowname():
        for row in c.execute('select * from mw'):
            return row
