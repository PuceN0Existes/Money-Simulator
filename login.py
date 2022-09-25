import os;
import get;
u=f'{os.getcwd()}/PDE.txt';
def log() :
    if os.path.isfile(u) and os.stat(u).st_size == 0 :
         print("\x1b[1;35mHola, \x1b[33meres nuevo aqui, soy \x1b[35mPuce\x1b[33m y te presento \x1b[35mMoney Simulator\x1b[0;0m")
         print("\x1b[1;34mNombre:\x1b[1;31m",end='')
         get.w(input()+',')
         print("\n\x1b[1;35mTrabajo\x1b[1;32m\nElije Entre Policia Barbero y Cazador\nNotece mayúsculas\n\x1b[;33m",end='');
         q=input('Elije:\x1b[;36m');
         if q not in ['Barbero','Cazador','Policia'] :
             print('\x1b[;31mTrabajo a Barbero por no poner un trabajo valido\x1b[;34m');
             get.w('Barbero,');
         else :
             get.w(q+',');
             print('has escogido '+q);
         get.w(str(300)+',1no,2no');
             
    elif os.path.isfile(u) and 15>os.stat(u).st_size>1 :
        os.remove(u);
        print('Trabajo Invalido, tu perfil fue reiniciado');
        print('');
    elif os.path.isfile(u)!=True :
        print('');get.w('')
    else :
        print('Sección iniciada como:\x1b[1;35m'+get.r().split(',')[0]+'\x1b[0;0m')
