import math
from time import sleep
print("Este programa de medias te servira para calcular tu media de selectividad de cara al acceso universitario")


Nota1 = ""
Nota2 = ""

Lengua = ""
HoF = ""
Mates = ""
Idioma = ""

Op1 = ""
Op2 = ""

bach = ""
tronc = ""
opt = ""

Notaf = ""
while True:
    Nota1 = input("Inserte su media en 1ro de Bachillerato: ")
    Nota1 = float(Nota1)

    Nota2 = input("Inserte su media en 2do de Bachillerato: ")
    Nota2 = float(Nota2)
    delay = 1.5
    
    print("Calculando la media de Bachillerato de cara a la prueba...")
    
    bach = ((Nota1 + Nota2)/2)*0.6
    sleep(delay)

    Lengua = input("Introduzca su nota en Lengua y Literatura: ")
    HoF = input("Introduzca su nota en Historia de Espana o Filosofia: ")
    Mates = input("Introduzca su nota en Matematicas: ")
    Idioma = input("Introduzca su nota en el idioma escogido: ")
    Lengua = float(Lengua)
    HoF = float(HoF)
    Mates = float(Mates)
    Idioma = float(Idioma)

    print("Calculando la media de las asignaturas troncales...")
    sleep(delay)
    tronc = ((Lengua * 0.1)+(Mates * 0.1)+(Idioma * 0.1)+(HoF * 0.1))

    Op1 = input("Introduzca su nota en la primera optatividad, contando con que le pondere 0.2: ")
    Op2 = input("Introduzca su nota en la segunda optatividad, contando con que le pondere 0.2: ")
    Op1 = float(Op1)
    Op2 = float(Op2)
    print("Calculando la media de sus optativas evaluadas: ")
    sleep(delay)
    opt = (Op1 * 0.2) + (Op2 * 0.2)
    Notaf = (bach + tronc + opt)
    print(f"""La nota total en selectividad obteniendo calificaciones de {Nota1} en el primer curso de Bachillerato,
    con {Nota2} en el segundo curso del mismo, con una media de {bach} (aplicando el 0.6 de cara a la prueba), ademas contando con notas
    de {Lengua} en la troncal de lengua, de {HoF} en Historia de Espana o Filosofia, con {Idioma} en el idioma seleccionado y con
    {Mates} en matematicas, obtendra la media de {tronc} y por ultimo con las notas obtenidas en las optatividades {Op1} y {Op2} respectivamente
    el resultado final de la nota es {Notaf} """)
    break

