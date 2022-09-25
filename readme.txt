Uso y permiso de distribucion.
A.1:
    El Usuario (Usted o ustedes) Es libre de
    Modificar, sin concentimiento del creador,YO,
    Utilizar modificaciones no oficiales
    Cambiar distribucion del contenido en 
    cuestion.
A.2:
    Modificaciones no oficiales NO recibiran:
        1.Soporte
        2.Actualizaciones
        3.Correcion de errores
A.3:
    Las Modificaciones deberan informar que
    No es el juego original y no recibira
    Soporte del creador.
Uso:
    CM:
        Te da 300 monedas esperando 1 minuto.
    C3M: 
        Es como CM pero te da 1000 monedas cada 3 Minutos.
    CAM:
        Te da monedas entre 45 y 200.
    Datos:
        Te dice tus datos del juego como por ejemplo el nombre que le hayas puesto A tu personaje.
    AM: 
        Te dice la cantidad actual de dinero ( Del ingles Actual Money)
    chname:
        Cambia tu nombre , No usar comas .
    AddMoney :
        Añade el valor que sera preguntado después de ejecutarlo
    SetMoney :
        Pregunta Un valor para remplazar el valor actual con el dado
    
Datos de jugador :
    en el archivo PDE.txt se guarda la informacion del personaje
    1er valor : Nombre
    2do valor : Trabajo ( Aunque en el juego solo puede ser Policia , Pescador o Barbero puede ser cualquier valor fuera de comas)
    3er valor : Dinero , No puede ser mayor a 2147483647
    4to valor : se ha usado CM
    5to valor : se ha usado C3M
Herramientas del juego:
    Archivo gio.py:
        Tiene 3 comandos utiles
        r(): Lee el archivo y devuelve el resultado
        w(x): inserta x , x siendo cualquier valor , y lo escribe en el archivo PDE.txt
        e(x): elimina PDE.txt estando su contenido en x , ( Para no perder sus datos es recomendado usar e(r().replace(A , B)) siendo A el valor a remplazar y B el valor deseado)
    Archivo login.py:
        Si Existe PDE.txt y tiene contenido:
            Escribe 'Seccion iniciada como (Tu nombre)'
        Si Existe PDE.txt y 15>longitud>1
            Elimina tu archivo de datos
        Si No Existe PDE.txt
            Lo crea
        Si Existe PDE.txt y no tiene contenido
            Te pregunta nombre y trabajo y lo crea
    Archivo lo.py:
        Siendo i un numero de 0 A x, imprime que tan cerca esta x en comparacion A 100*x/i
    Archivo bucle.py
        El juego En si
