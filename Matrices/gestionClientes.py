#Nos piden realizar un programa para gestionar los clientes de una tienda de ropa.
#    1- Ingresar Clientes (Nombre, apellido, DNI, Mail, Codigoarea, Telefono)
#    2- Mostrar los Clientes registrados
#    3- Modificar los datos de un cliente: 
#Preguntar el dato a modificar y luego cambiar ese dato del mismo, GUARDAR FECHA MODIFICACION= ‘3/5/2026’
#    4- Permitir la baja de un Cliente cambiando  su estado (A=ACTIVO, B=BAJA) y fecha de Baja “2/10/2026”
#    5- Mostrar los Clientes que se dieron de BAJA

def ingreso(clientes):
    cliente = []

    nombre = input("ingrese el nombre y apellido del cliente: ")
    dni = int(input("Ingrese el DNI: "))
    for i in range(len(clientes)):
        if clientes[i][1] == dni:
            print("ERROR, este cliente ya esta registrado")
            return
    mail =input("Ingrese el mail: ")
    codigo = int(input("Ingrese el codigo de area: "))
    telefono = int(input("Ingrese el telefono: "))
    estado = "A"
    fechamod = ""
    fechabaja = ""
    cliente = [nombre,dni,mail,codigo,telefono,estado,fechamod,fechabaja]

    clientes.append(cliente)
    print("Cliente registrado correctamente")
    return clientes

def mostrar(clientes):
    print("LISTA CLIENTES")
    for i in range(len(clientes)):
        print(clientes[i])

def modificar(clientes):
    dni_buscar = int(input("Ingrese el DNI del cliente a modificar: "))

    for i in range(len(clientes)):
        if clientes[i][1] == dni_buscar:

            dato = input("Seleccione el dato a modificar\nNombre\nDNI\nMail\nCodigo Postal\nTelefono\n: ").lower()

            if dato == "nombre":
                clientes[i][0] = input("Ingrese el nombre y apellido nuevo: ")

            elif dato == "dni":
                clientes[i][1] = int(input("Ingrese el DNI nuevo: "))

            elif dato == "mail":
                clientes[i][2] = input("Ingrese el mail nuevo: ")

            elif dato == "codigo de area":
                clientes[i][3] = int(input("Ingrese el codigo postal nuevo: "))

            elif dato == "telefono":
                clientes[i][4] = int(input("Ingrese el telefono nuevo: "))

            else:
                print("El dato seleccionado es incorrecto")
                return

            clientes[i][6] = "3/5/2026"
            print("Cliente modificado correctamente")
            return

    print("No existe un cliente con ese DNI")
    
def darbaja(clientes):
    baja = int(input("Ingrese el DNI del cliente a dar de baja: "))

    for i in range(len(clientes)):
        if clientes[i][1] == baja:
            clientes[i][5] = "B"
            clientes[i][7] = "2/10/2026"
            print("Cliente dado de baja correctamente")
            return

    print("No existe un cliente asociado a este DNI")


def mostrarbaja(clientes):
    print("CLIENTES DADOS DE BAJA")
    existe = False


    for i in range(len(clientes)):
        if clientes[i][5] == "B":
            print(clientes[i])
            existe = True
        
    if existe == False:
        print("No hay clientes dados de baja")



def menu():
    print("\nMENÚ")
    print("1. Ingresar cliente")
    print("2. Mostrar clientes")
    print("3. Modificar datos de un cliente")
    print("4. Dar de baja")
    print("5. Mostrar bajas dadas")
    print("6. Salir del sistema")


def iniciar():
    opcion = 0
    clientes = []
    while opcion != 6:
        menu()
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            ingreso(clientes)
        elif opcion == 2:
            mostrar(clientes)
        elif opcion == 3:
            modificar(clientes)
        elif opcion == 4:
            darbaja(clientes)
        elif opcion == 5:
            mostrarbaja(clientes)
        elif opcion == 6:
            print("Saliendo del sistema")
        else:
            print("Opcion invalida")

iniciar()