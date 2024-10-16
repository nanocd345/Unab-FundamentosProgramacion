def votaciones():
    print("Bienvenido a las Votaciones de Colombia ")
    print("son TOTALMENTE legales y justas 100% ")
    nacionalidad=str(input("ingrese su nacionalidad= (ejemplo:colombiano, brazileño, etc...) (empieze con mayusculas)= "))
    if nacionalidad == "Colombiano":
        edad=int(input("perfecto, ahora digame su edad= "))
        if edad >= 18:
            print("bien, usted cumple los requisitos para votar")
        else:
            print("no eres mayor de edad, no puedes votar")
    else:
        print("ey, no puedes votar si no eres colombiano ")


