import sqlite3
import numpy as np
from operator import itemgetter
conn = sqlite3.connect('C:\\Users\\shengyu\\Desktop\\FYP\\chaos\\database\\stat3.db')
c = conn.cursor()

x=[]
y=[]
myarray=[]
for row in c.execute('select seq from mw'):
    a=''.join(row).split('.')
    m=np.array(a)
    m=np.asarray(m)
    myarray=np.concatenate((myarray,m),axis=0)
    print type(','.join(myarray))
for e in myarray:    
    x=[i for i, x in enumerate(myarray) if x==e]
    #print e+":"+str(len(x))
    y.append((e,len(x)))
y=list(set(y))
new=sorted(y,key=itemgetter(1) )
print new
