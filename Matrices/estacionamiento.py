def crear_estacionamiento():
    matriz = [
        ["L","L","L","L","L","L","L","L"],
        ["L","L","L","L","L","L","L","L"],
        ["L","L","L","L","L","L","L","L"],
        ["L","L","L","L","L","L","L","L"],
        ["L","L","L","L","L","L","L","L"]
    ]
    return matriz


def visualizar(matriz):
    print("\nESTACIONAMIENTO")
    print("L = Libre | O = Ocupado\n")

    print("Columna  1    2    3    4    5    6    7    8")
    for i in range(len(matriz)):
        print("Fila", i + 1, matriz[i])


def registrar_ingreso(matriz,ingreso_egreso):
    fila = int(input("Ingrese fila del 1 al 5: ")) - 1
    sector = int(input("Ingrese sector del 1 al 8: ")) - 1

    if fila < 0 or fila >= 5 or sector < 0 or sector >= 8:
        print("Fila o sector inválido")

    elif matriz[fila][sector] == "L":
         matriz[fila][sector] = "O"
         plaza = ""
         patente = ""
         hora_entrada = ""
         hora_salida = ""
         vehiculo = []
         
         patente = input("Ingrese la patente: ").lower()
         for i in range(len(ingreso_egreso)):
            if ingreso_egreso[i][0] == patente:
                print("ERROR, vehiculo ya registrado")
                return
         plaza = input("Ingrese la plaza: ")
         hora_entrada = input("Ingrese la hora de entrada: ")
         vehiculo = [patente,plaza,hora_entrada,hora_salida]
         ingreso_egreso.append(vehiculo)
         print("Ingreso registrado correctamente")
         
    else:
         print("Ese lugar ya está ocupado")


def registrar_salida(matriz,ingreso_egreso):
    fila = int(input("Ingrese fila del 1 al 5: ")) - 1
    sector = int(input("Ingrese sector del 1 al 8: ")) - 1

    if fila < 0 or fila >= 5 or sector < 0 or sector >= 8:
        
        print("Fila o sector inválido")

    elif matriz[fila][sector] == "O":
         matriz[fila][sector] = "L"
         hora_salida = input("Ingrese la hora de salida: ").lower()
         for i in range(len(ingreso_egreso)):
             for j in range(3): 
                ingreso_egreso[i][3] = hora_salida
         print("Salida registrada correctamente")
    else:
        
        print("Ese lugar ya está libre")
          
def contar_lugares(matriz):
    libres = 0
    ocupados = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == "L":
                libres += 1
            else:
                ocupados += 1

    return libres,ocupados
    
    

def informe(matriz,ingreso_egreso):
    libres, ocupados = contar_lugares(matriz)
    total = libres + ocupados
    porcentaje = ocupados * 100 / total

    print("\nINFORME FINAL")
    print("Total de lugares:", total)
    print("Lugares ocupados:", ocupados)
    print("Lugares libres:", libres)
    print("Porcentaje de ocupación:", porcentaje, "%")

    print("Vehiculos registrados:")
    for i in range(len(ingreso_egreso)):
             print(ingreso_egreso[i])

   
def menu():
    print("\nMENÚ")
    print("1. Visualizar estacionamiento")
    print("2. Registrar ingreso de un auto")
    print("3. Registrar salida de un auto")
    print("4. Imprimir informe")
    print("5. Salir del sistema")


def iniciar():
    estacionamiento = crear_estacionamiento()
    opcion = 0
    ingreso_egreso = []
    while opcion != 5:
        menu()
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            visualizar(estacionamiento)
        elif opcion == 2:
            registrar_ingreso(estacionamiento,ingreso_egreso)
        elif opcion == 3:
            registrar_salida(estacionamiento,ingreso_egreso)
        elif opcion == 4:
            informe(estacionamiento,ingreso_egreso)   
        elif opcion == 5:
            print("Saliendo del sistema")    
        else:
            print("Opción inválida")


iniciar()