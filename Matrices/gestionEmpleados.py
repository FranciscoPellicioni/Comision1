#Ejercicio 3: Gestión de Empleados
#Ingresar empleados (Legajo, Nombre, Apellido, Cargo, Sector, Sueldo). 
#Mostrar todos los empleados registrados. 
#Modificar el cargo de un empleado. 
#Modificar el sueldo de un empleado. 
#Mostrar el empleado con mayor sueldo. 
#Mostrar el sueldo promedio de la empresa. 


def ingreso(empleados):
    empleado = []
    legajo = int(input("Ingrese el legajo del empleado: "))
    for i in range(len(empleados)):
        if empleados[i][0] == legajo:
            print("ERROR, este empleado ya esta registrado")
            return
    nombre = input("ingrese el nombre y apellido del empleado: ")
    cargo = input("Ingrese el cargo: ")
    sector = input("Ingrese el sector: ")
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    empleado = [legajo,nombre,cargo,sector,sueldo]
    empleados.append(empleado)
    print("Empleado registrado con exito")
    return empleados
    
def mostrar(empleados):
    print("LISTA EMPLEADOS")
    for i in range(len(empleados)):
        print(empleados[i])



def modificar(empleados):
    legajo_buscar = int(input("Ingrese el legajo del empleado a buscar: "))
    for i in range(len(empleados)):
        if empleados[i][0] == legajo_buscar:
            dato = input("Seleccione el dato a modificar\nCargo\nSueldo\n-").lower()

            if dato == "cargo":
                empleados[i][2] = input("Ingrese el cargo nuevo: ")
                print("dato modificado correctamente")
            elif dato == "sueldo":
                empleados[i][4] = float(input("Ingrese el sueldo nuevo: "))
                print("dato modificado correctamente")
            else:
                print("El dato ingresado es incorrecto")
            return
    print("No existe un empleado con ese legajo")

def sueldo_mayor(empleados):
    mayor = empleados[0]

    for i in range(1,len(empleados)):
        if empleados[i][4] > mayor[4]:
            mayor = empleados[i]

    print("El empleado con el sueldo mas alto es",mayor)


def sueldo_promedio(empleados):
    total_sueldos = 0
    total_empleados = 0
    promedio = 0
    for i in range(len(empleados)):
        total_sueldos += empleados[i][4]
        total_empleados += 1
    promedio = total_sueldos/total_empleados
    print("El sueldo promedio de la empresa es",promedio)

def menu():
    print("\nMENÚ")
    print("1. Ingresar empleado")
    print("2. Mostrar empleados")
    print("3. Modificar datos de un empleado")
    print("4. Mostrar empleado con el mayor sueldo")
    print("5. Mostar el sueldo promedio de la empresa")
    print("6. Salir del sistema")


def iniciar():
    empleados = []
    opcion = 0
    while opcion != 6:
        menu()
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            ingreso(empleados)
        elif opcion == 2:
            mostrar(empleados)
        elif opcion == 3:
            modificar(empleados)
        elif opcion == 4:
            sueldo_mayor(empleados)
        elif opcion == 5:
            sueldo_promedio(empleados)
        elif opcion == 6:
            print("Saliendo del sistema...")
        else:
            print("Opcion invalida")

iniciar()