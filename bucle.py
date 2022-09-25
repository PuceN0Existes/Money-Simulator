import login as l;
import random as r;
import get as g;
import os , lo ;
l.log();
while True :
    j=r.randint(45,200)
    du=g.r().split(",")
    try :
        [name,work,am,CM,C3M]=du;
    except ValueError :
        os.remove(g.u);l.log();raise ValueError('\x1b[1;34mHa ocurrido un \x1b[;31mError\x1b[;34m al cargar el archivo de datos y se ha eliminado\x1b[0;0m');
    am=int(am) 
    nam=am+j
    print('\x1b[1;32mBanco:\x1b[0m',end='')
    AI=input();
    dp=du[0]+','+du[1]+','+du[2]+','+du[3]+','+du[4]
    if AI in ['Exit','exit','Salir','salir'] :
        break
    elif AI=='CM' and CM=='1no' :
        g.e(dp.replace('1no','1si').replace(str(am),str(am+300)))
        am+=300;
        print('\x1b[1  ganaste \x1b[32m300\x1b[32m monedas');
    elif AI=='CM' and CM=='1si' :
        o=input('\x1b[1;32mDesbloquear? (\x1b[1;33mTarda 1 minuto) \x1b[0;0m')
        if o in ['N','n','NO','No','nO','no','X','-'] :
            continue;
        elif o in ['Y','y','S','s','si','sI','Si','SI','Ok','ok','OK'] :
             lo.wt(60);
             print('\x1b[1;35mDesbloqueado exitosamente\x1b[0;0m\t');
             g.e(dp.replace('1si','1no'));
             continue;
    elif AI=='C3M' and C3M=='2no' :
        g.e(dp.replace('2no','2si').replace(str(am),str(am+1000)))
        am+=1000;
        print('\x1b[1 ganaste \x1b[32m1000\x1b[32m monedas');
    elif AI=='C3M' and C3M=='2si' :
        o=input('\x1b[1;32mDesbloquear? (\x1b[1;33mTarda 3 minutos) \x1b[0;0m')
        if o in ['N','n','NO','No','nO','no','X','-'] :
            continue;
        elif o in ['Y','y','S','s','si','sI','Si','SI','Ok','ok','OK'] :
             lo.wt(180);
             print('\x1b[1;35mDesbloqueado\x1b[0;0m');
             g.e(dp.replace('2si','2no'));
             continue;
    elif AI=='CAM' :
        g.e(dp.replace(str(am),str(nam)))
        print('Has Obtenido '+str(j)+' monedas');continue;
    elif AI=='Datos' :
        print(f'\x1b[1;36mNombre:\x1b[1;35m{name}')
        print(f'\x1b[1;36mTrabajo:\x1b[1;35m{work}')
        print(f'\x1b[1;36mDinero:\x1b[1;35m{am}')
    elif AI in ['Bal','dinero','am','Dinero','bal','AM'] :
        print(f'\x1b[0;34mtienes \x1b[1;32m{am} \x1b[0;34mMonedas\x1b[0;0m')
    elif AI in ['chname','CambiarNombre']:
        inp = input(f'\x1b[1;34mTu nombre es : \x1b[0;32m{name} , \x1b[1;34mquieres cambiarlo?')
        if inp in ['S','s','Si','si'] :
            g.e(dp.replace(name,input('\x1b[1;33mNuevo Nombre:\x1b[;35m')))
            print('\x1b[1;32mCambiado Exitosamente')
        elif inp in ['N','n','No','no']:
            print('\x1b[1;31;43mCancelado\x1b[0;0;0m')
    elif AI in ['H','h','Ayuda','ayuda','Uso','uso'] :
        print('\x1b[1;36mLa ayuda se encuentra en Uso.txt \nen este mismo directorio, no se\nincluye en el codigo\nAyuda Basica: Para salir escribir Exit\x1b[0;0m')
    elif AI == 'AddMoney' :
        ioam=input('\x1b[0;35mCuanto Dinero?') 
        g.e(dp.replace(str(am),str(am+int(ioam))))
        print(f'Se ha añadido {ioam} monedas')
        print(f'\x1b[1;32mactualmente tienes {am+int(ioam)} monedas')
    elif AI == 'SetMoney' :
        g.e(dp.replace(str(am),input('\x1b[1;34mCambiar Dinero A:')))
    elif AI in ['Ruleta','ruleta'] :
        dss=input('\x1b[1;36mNumero entre 5 y 155, error maximo de 5:')
        nap=input('\x1b[1;34mCantidad a Apostar( si\nPierde y no tiene el dinero , tendras\n dinero negativo):')
        try :
            int(nap)
        except ValueError :
            print(f'Error ,{nap} no es un numero')
        else :
            nap=int(nap)
        z=j-40
        
        tof=int(dss) in [z-5,z-4,z-3,z-2,z-1,z,z+1,z+2,z+3,z+4,z+5];
        if tof :
            print('\x1b[0;32mGanaste!! se te sumaran 900 puntos');
            g.e(dp.replace(str(am),str(am+900)))
        elif not 155>int(dss)>5 :
            raise ValueError('Valor No Valido')
        elif not tof :
            print(f'\x1b[1;35mHas apostado {nap} monedas, Pero perdiste y por lo tanto {nap} Monedas,Actualmente Tienes {am-nap} Monedas,El valor era {dss}, En un rango de [{int(dss)-5} y {int(dss)+5}]')
    elif AI in ['xd','xD','Xd','XD'] :
        print('\x1b[0;35mXD')
    elif AI == 'DumpData' :
        print(g.r())
    elif AI in ['DelAcc','RmAcc'] :
        if input('Seguro?') in ['s','si','S','si'] :
            os.remove(f'{os.getcwd()}/PDE.txt');l.log();l.log()
        else :
            print('Cancelado')
    elif AI == 'CMD' :
        print(['AM','AddMoney','Bal','CAM','CM','CMD','C3M','chname','DelAcc','Ruleta'])
