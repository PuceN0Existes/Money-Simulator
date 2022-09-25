import os;
u=f'{os.getcwd()}/PDE.txt';
def r() :
    """
    Es lo que lee XD
    """
    a=open(u,'r');
    e=a.read()
    a.close();
    return e;
def w(x) :
    """
    Es lo que escribe XD
    """
    a=open(u,'a');
    a.write(str(x));
    a.close();
    return "escrito "+x+" a "+u;
def e(d) :
    os.remove(u);
    q=open(u,'a');
    q.write(d)
    q.close()