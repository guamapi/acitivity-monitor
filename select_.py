import sqlite3
conn = sqlite3.connect('C:\\Users\\shengyu\\Desktop\\FYP\\chaos\\database\\stat1.db')
c = conn.cursor()
for row in c.execute('select * from mw'):    
    	print row
