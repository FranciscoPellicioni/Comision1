#Ejercicio 2: Gestión de Vehículos de una Concesionaria
#Ingresar vehículos (Patente, Marca, Modelo, Año, Color, Precio). 
#Mostrar todos los vehículos registrados. 
#Modificar el color de un vehículo. 
#Modificar el precio de un vehículo. 
#Mostrar los vehículos cuyo precio supere un valor ingresado por teclado. 
#Mostrar el vehículo más antiguo.

def ingreso(vehiculos):
    vehiculo = []
    patente = input("Ingrese la patente del vehiculo: ")
    for i in range(len(vehiculos)):
        if vehiculos[i][0] == patente:
            print("ERROR, ese vehiculo ya esta registrado")
            return
    marca = input("Ingrese la marca: ")
    modelo = input("Ingrese el modelo: ")
    año = int(input("Ingrese el año: "))
    color = input("Ingrese el color: ")
    precio = float(input("Ingrese el precio: "))
    vehiculo = [patente,marca,modelo,año,color,precio]
    vehiculos.append(vehiculo)
    print("Vehiculo registrado correctamente")
    return vehiculos,vehiculo


def mostrar(vehiculos):
    print("LISTA VEHICULOS")
    for i in range(len(vehiculos)):
        print(vehiculos[i])
    
def modificar(vehiculos):
    patente_buscar = input("Ingrese la patente del vehiculo a buscar: ")
    for i in range(len(vehiculos)):
        if vehiculos[i][0] == patente_buscar: 
           dato = input("Ingrese el dato a modificar\nColor\nPrecio\n- ").lower()

           
           if dato == "color":
                vehiculos[i][4] = input("Ingrese el color nuevo: ")
                print("dato modificado correctamente")
           elif dato == "precio":
                vehiculos[i][5] = float(input("Ingrese el precio nuevo de lista: ")) 
                print("dato modificado correctamente")
           else:
                print("El dato ingresado es incorrecto")    
           return
        
    print("No existe un vehiculo registrado con esa patente")
            

def caros(vehiculos):
    valor = float(input("Ingrese un precio: "))
    encontrados = False
    print("VEHICULOS MAS CAROS")
    for i in range(len(vehiculos)):
        if vehiculos[i][5] > valor:  
            print(vehiculos[i])
            encontrados = True
            
    if encontrados == False:
        print("No hay vehiculos de un precio mayor al ingresado")  
     
     
def mas_antiguo(vehiculos):
    if len(vehiculos) == 0:
        print("No hay vehiculos registrados")
        return
    antiguo = vehiculos[0]
    for i in range(1,len(vehiculos)):
        if vehiculos[i][3] < antiguo[3]:
            antiguo = vehiculos[i]
    print("El vehiculo mas antiguo es",antiguo)


def menu():
    print("\nMENÚ")
    print("1. Ingresar vehiculo")
    print("2. Mostrar vehiculos")
    print("3. Modificar datos de un vehiculo")
    print("4. Vehiculos caros")
    print("5. Vehiculo mas antiguo")
    print("6. Salir del sistema")




def iniciar():
    vehiculos = []
    
    opcion = 0
    
    while opcion != 6:
        menu()
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            ingreso(vehiculos)
        elif opcion == 2:
            mostrar(vehiculos)
        elif opcion == 3:
            modificar(vehiculos)
        elif opcion == 4:
            caros(vehiculos)
        elif opcion == 5:
            mas_antiguo(vehiculos)
        elif opcion == 6:
            print("Saliendo del sistema...")
        else:
            print("Opcion invalida")

iniciar()