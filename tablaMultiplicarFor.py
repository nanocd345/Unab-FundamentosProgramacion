def tablaMultiplicarFor():

    while True:

        numero = int(input("porfavor ingrese el numero que quiere multiplicar: "))

        limite = int(input("hasta que numero quiere multiplicar?= "))

        print("Tabla de multiplicar del " + str(numero))
        for i in range(1, (limite+1)): 
            resultado = numero * i
            print(numero , "*", i , "=", resultado)

        repetir = int(input("cualquier numero para repetir y 0 para salir = "))
        if repetir != 0:
            break
        else:
            print("redirigiendo al inicio nuevamente ...")
            