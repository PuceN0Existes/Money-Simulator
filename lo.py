import time as t;
def wt(x) :
    y=100/x
    for i in range(1,x+1) :
           print(str(y*i)[0:5]+'% de 100%',end='\r');
           t.sleep(1);
           if i==x:
               print('\r',end='')