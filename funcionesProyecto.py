#ListaMenu
MenuLista = [
    {"nombre": "1 pollo completo", "precio": 35000, "seccion": "Pollos", },
    {"nombre": "Medio pollo", "precio": 20000, "seccion": "Pollos"},
    {"nombre": "Cubeta de pollo S", "precio": 15000, "seccion": "Pollos"},
    {"nombre": "Cubeta de pollo M", "precio": 25000, "seccion": "Pollos"},
    {"nombre": "Cubeta de pollo L", "precio": 40000, "seccion": "Pollos"},
    {"nombre": "alitas de pollo", "precio": 20000, "seccion": "Pollos"},
    {"nombre": "nuggets de pollo", "precio": 18000, "seccion": "Pollos"},
    {"nombre": "pollo con pollo y con salsa de pollo", "precio": 35000, "seccion": "Pollos"},
    {"nombre": "porcion de papas a la francesa", "precio": 10000, "seccion": "Porciones Individuales"},
    {"nombre": "porcion de papas criollas", "precio": 12000, "seccion": "Porciones Individuales"},
    {"nombre": "porcion de yuca frita", "precio": 15000, "seccion": "Porciones Individuales"},
    {"nombre": "Cubeta de pollo Familiar", "precio": 60000, "seccion": "Combos"},
    {"nombre": "Super caja de pollo de los pollos hermanos", "precio": 70000, "seccion": "Combos"},
    {"nombre": "Pack de 2 pollos completos", "precio": 60000, "seccion": "Combos"},
    {"nombre": "jarra de limonada", "precio": 7000, "seccion": "Bebidas"},
    {"nombre": "gaseosa litro", "precio": 12000, "seccion": "Bebidas"},
    {"nombre": "gaseosa Personal", "precio": 4000, "seccion": "Bebidas"},
    {"nombre": "suntea", "precio": 5000, "seccion": "Bebidas"},
    {"nombre": "lata de cerveza", "precio": 3500, "seccion": "Bebidas"}
]

#Lista
carrito = []

#Mostrar menu
def VerMenu ():
    print("")
    print("")
    print("-------------------Este es el Menu de las productos que tenemos disponibles... -------------------")
    print("")
    print("")
    
    secciones = set(item["seccion"] for item in MenuLista)

    for seccion in secciones:
        print(f"\n======= {seccion} =======")
        print("-------------------------------------------------")    
        for item in MenuLista:
            if item["seccion"] == seccion:
                print(f"- {item['nombre']} (Precio: ${item['precio']})")
        print("-------------------------------------------------") 

#funcion hacer pedido
def Pedido():
    while True:
        # Solicitar al usuario el nombre del plato o bebida
        pedido = input("Ingresa el nombre de la comida o bebida que deseas ordenar (Si deseas finalizar escribe 'terminar'): ").strip().lower()
        
        # Verificar si el usuario desea terminar el pedido
        if pedido == "terminar":
            if carrito:  # Verificar si el carrito tiene elementos
                print(" Volviendo al menu principal.... ")
            else:
                print("\nEl carrito está vacío.")
            break  # Salir del bucle de pedidos

        # Buscar el pedido en el menú
        encontrado = False
        for i in MenuLista:
            if "nombre" in i and i["nombre"].lower() == pedido:
                precio = int(i["precio"])
                carrito.append({"nombre": i["nombre"], "precio": precio})
                print(f"\nProducto '{i['nombre']}' agregado a tu carrito.")
                encontrado = True
                break  # Salir del bucle for después de encontrar el artículo

        
        if not encontrado:
            print(f"El artículo '{pedido}' no está disponible en el menú.")

#funcion de mirar los pedidos
def MirarPedidos():
    print("")
    print("----- Este es su pedido actualmente -----")
    print("")
    if not carrito:  
        print("El carrito está vacío.")
    else:
        for item in carrito:
            print(f"- {item['nombre']} (Precio: ${item['precio']})")
    
#funcion para eliminar pedidos 
def EliminarPedido():
    if not carrito:
        print("El carrito está vacío. No hay nada que eliminar.")
        return

    while True:

        nombreEliminar = input("Ingresa el nombre del producto que deseas eliminar: ").strip().lower()
        encontrado = False  

        for item in carrito:
            if item['nombre'].lower() == nombreEliminar:
                carrito.remove(item)  
                print(f"El artículo '{item['nombre']}' ha sido eliminado del carrito.")
                encontrado = True   
        salida=int(input("presione 0 para salir, y cualquier otro numero para eliminar otro producto: "))
        if salida == 0:
            break
        else: 
            print("volviendo al menu de eliminacion nuevamente...")
            print("")


        if not encontrado:
            print(f"El artículo '{nombreEliminar}' no se encuentra en el carrito.")

#MenuPrincipal
def menu():
    while True:
        print("\n" + "="*87)
        print("|   ██╗      ██████╗ ███████╗    ██████╗  ██████╗ ██╗     ██╗      ██████╗ ███████╗   |")
        print("|   ██║     ██╔═══██╗██╔════╝    ██╔══██╗██╔═══██╗██║     ██║     ██╔═══██╗██╔════╝   |")
        print("|   ██║     ██║   ██║███████╗    ██████╔╝██║   ██║██║     ██║     ██║   ██║███████╗   |")
        print("|   ██║     ██║   ██║╚════██║    ██╔═══╝ ██║   ██║██║     ██║     ██║   ██║╚════██║   |")
        print("|   ███████╗╚██████╔╝███████║    ██║     ╚██████╔╝███████╗███████╗╚██████╔╝███████║   |")
        print("|   ╚══════╝ ╚═════╝ ╚══════╝    ╚═╝      ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚══════╝   |")
        print("|                                                                                     |")
        print("|       ██╗  ██╗███████╗██████╗ ███╗   ███╗ █████╗ ███╗   ██╗ ██████╗ ███████╗        |")
        print("|       ██║  ██║██╔════╝██╔══██╗████╗ ████║██╔══██╗████╗  ██║██╔═══██╗██╔════╝        |")
        print("|       ███████║█████╗  ██████╔╝██╔████╔██║███████║██╔██╗ ██║██║   ██║███████╗        |")
        print("|       ██╔══██║██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══██║██║╚██╗██║██║   ██║╚════██║        |")
        print("|       ██║  ██║███████╗██║  ██║██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╔╝███████║        |")
        print("|       ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝        |")
        print("="*87)
        print(""" 
                                ¿Que deseas ordenar?
                                1. Mirar Menu 
                                2. Hacer pedido
                                3. Eliminar pedido 
                                4. Mirar Pedidos
                                5. Salir Programa
        """)
      
        try:
            eleccion = int(input(" Escoge una opcion del (1-5)"))
        except ValueError:
            print(" Error: Ingresa un Valor numerico dentro del rango de (1-5). ")
            return menu()
        
        if eleccion == 1:
            print("Entrando a menu.... ")
            VerMenu()
        elif eleccion ==2:
            print("Entrando a hacer pedido.... ")
            Pedido()
        elif eleccion == 3:
            print(" Entrando a eliminar pedido.... ")
            EliminarPedido()
        elif eleccion == 4:
            print("Entrando a mirar pedido..... ")
            MirarPedidos()
        elif eleccion == 5:
            print(" !Gracias por visitarnos! ")
            break
        else:
            print(" Escoje una opcion valida ")

#con esto se llama a TODO el programa
menu()