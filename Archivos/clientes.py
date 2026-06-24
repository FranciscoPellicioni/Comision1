#Ejercicio Integrador
#• Construir un menú:
#• 1. Agregar cliente
#• 2. Mostrar clientes
#• 3. Salir

def ingreso():
    try:
        archivo = open("clientes.txt", "r")
    except FileNotFoundError:
        archivo = open("clientes.txt", "a")
        archivo.close()
        archivo = open("clientes.txt", "r")

    lineas = archivo.readlines()
    archivo.close()

    dni = input("Ingrese el DNI: ")

    for linea in lineas:
        datos = linea.strip().split("|")
        if datos[0] == dni:
            print("ERROR, este cliente ya está registrado")
            return

    nombre = input("Ingrese el nombre y apellido del cliente: ")
    mail = input("Ingrese el mail: ")
    codigo = input("Ingrese el codigo de area: ")
    telefono = input("Ingrese el telefono: ")
    estado = "A"

    archivo = open("clientes.txt", "a")
    archivo.write(f"{dni}|{nombre}|{mail}|{codigo}|{telefono}|{estado}\n")
    archivo.close()

    print("Cliente registrado correctamente")


def mostrar():
    print("LISTA CLIENTES")
    archivo = open("clientes.txt","r")
    for linea in archivo:
        print(linea.strip())
    archivo.close()


def menu():
    print("\nMENÚ")
    print("1. Ingresar cliente")
    print("2. Mostrar clientes")
    print("3. Salir del sistema")


def iniciar():
    opcion = 0
    
    while opcion != 3:
        menu()
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            ingreso()
        elif opcion == 2:
            mostrar()
        elif opcion == 3:
            print("Saliendo del sistema")
        else:
            print("Opcion invalida")

iniciar()