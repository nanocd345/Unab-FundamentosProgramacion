import math
import random

def definirParImpar ():

    print("Bienvenido al programa de numeros pares e impares")
    print("")
    numero=(int(input("ingrese el numero que quiere saber si es par o impar: ")))
    if numero % 2 == 0:
        print ("ese numero es PAR")
    elif numero % 2 == 1:
        print (" ese numero es IMPAR")
    else:
        print("¿que?")

def definirRaiz ():

        print("Bienvenido al calculador de raices")
        print("")
        numero=(int(input("ingrese el numero que quiere saber la raiz cuadrada: ")))

        raizCuadrada= math.sqrt(numero)
        print(raizCuadrada)

def LoteriaDeBoyaca():
    print("")
    print("Mentí, esto no es la lotería, es el Casino")
    print("")

    plata01 = int(input("Ingrese la plata que va a apostar: "))

    while True:

        ruleta = random.randint(1, 36)
        eleccionApuesta = int(input("¿Quiere apostar a un número o a un color? (1. número) (2. color): "))

        if eleccionApuesta == 1:
            eleccion = int(input("¿A qué número quiere apostarle?: "))
            if ruleta == eleccion:
                ganado = plata01 * 2
                print("¡Ganó!", ganado)
            else:
                print("Perdiste, la ruleta cayó en", ruleta)

        elif eleccionApuesta == 2:
            seleccionColor = int(input("Seleccione un color (1. rojo) (2. negro): "))

            numeros_rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
            numeros_negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
            
            if seleccionColor == 1:
                if ruleta in numeros_rojos:
                    ganado = plata01 * 2
                    print("¡Ganó!", ganado)
                else:
                    print("Perdiste, la ruleta cayó en", ruleta)
            elif seleccionColor == 2:
                if ruleta in numeros_negros:
                    ganado = plata01 * 2
                    print("¡Ganó!", ganado)
                else:
                    print("Perdiste, la ruleta cayó en", ruleta)
        plata = plata01 + ganado
        print("usted actualmente tiene ", plata)

        opSalirCasino=int(input("desea apostar otra vez el total que tiene? o quiere salir y apostar a partir de un nuevo valor = "))

while True:

    print("")
    print("")
    print("██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗██████╗  ██████╗ ")
    print("██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║██╔══██╗██╔═══██╗")
    print("██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║██║  ██║██║   ██║")
    print("██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║██║  ██║██║   ██║")
    print("██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║██║██████╔╝╚██████╔╝")
    print("╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═╝╚═════╝  ╚═════╝ ")

    print("")
    print("")

    print("Seleccione lo que quiere realizar")
    print("")
    print("1. verificar PAR o IMPAR")
    print("2. calcular raiz cuadrada")
    print("3. apostar la pension")
    print("4. calculadora Aritmetica")
    print("5. tabla de multiplicar de un numero")
    print("6. sistema de votacion")
    print("7. sistema de votacion")
    print("0. Salir")

    seleccionMenu=(int(input("digite la opcion= ")))

    if seleccionMenu == 1:
        definirParImpar()
    elif seleccionMenu == 2:
        definirRaiz()
    elif seleccionMenu == 3:
        LoteriaDeBoyaca()
    elif seleccionMenu == 4:
        import calculadoraAritmetica
    elif seleccionMenu == 5:
        import tablaMultiplicarFor
    elif seleccionMenu == 6:
        import registroVotacion
    elif seleccionMenu == 0:
        break


