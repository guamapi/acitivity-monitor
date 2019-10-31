import numpy as np
import sqlite3
from sklearn import linear_model


#classifier: mouse_left(1,2,3), key_type(1,2,3), mouse_scroll(1,2)
#none(1), browse(2), online_chat(3), work(4)
def classifier(x):
    if x==[1,1,1]:
        y=1
     elif x==[1,2,1]:
         y=3
     elif x==[]
X = np.array([[1,1,1],[1,2,1],[1,2,1],[1,3,1],[1,3,1],[2,1,1],[2,2,1],[2,3,1],[3,1,1],[3,2,1],[3,3,1],[1,1,2],[1,2,2],[1,3,2],[2,1,2],[2,2,2],[2,3,2],[3,1,2]])
Y = np.array([1      ,3      ,4      ,3      ,4      ,4      ,4      ,4      ,4      ,4      ,4      ,2      ,4      ,4      ,2      ,4      ,4      ,2      ])
clf = linear_model.SGDClassifier()
clf.fit(X, Y)

conn=sqlite3.connect('c:\\users\\shengyu\\desktop\\stat.db')
c=conn.cursor()
c.execute('''create table none(time int, map text)''')
c.execute('''create table browse(time int, map text)''')
c.execute('''create table online(time int, map text)''')
c.execute('''create table work(time int, map text)''')

for i in range(0,23):
    time_s=100*i
    time_e=100*i+30
    nl=0
    ll=0
    for row in c.execute('select freq from ml where time<='+time_e+'and time >='+time_s):
        a=''.join(str(row)).replace('.0,','').replace('(','').replace(')','')
        nl=nl+int(a)
        ll=ll+1
    fl=nl/ll

    ns=0
    ls=0
    for row in c.execute('select freq from ms where time<='+time_e+'and time >='+time_s):
        a=''.join(str(row)).replace('.0,','').replace('(','').replace(')','')
        ns=ns+int(a)
        ls=ls+1
    fs=ns/ls

    nk=0
    lk=0
    for row in c.execute('select freq from kt where time<='+time_e+'and time >='+time_s'):
        a=''.join(str(row)).replace('.0,','').replace('(','').replace(')','')
        nk=nk+int(a)
        lk=lk+1
    fk=nk/lk

    p=clf.predict([[fl,fk,fs]])
    if p==1:
                         c.execute("insert into none select time, map from mousemap)
                                   
for row in c.execute('select map from mousemap'):
                                   

    elif p==2:
                         c.execute("insert into browse select time, map from mousemap)
    elif p==3:
                         c.execute("insert into online select time, map from mousemap)
    elif p==4:
                         c.execute("insert into work select time, map from mousemap)
