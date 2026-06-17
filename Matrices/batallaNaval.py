import random


def generar(campo):
    barcos = 0
    while barcos < 5:
        posicionF = random.randint(0,9)
        posicionC = random.randint(0,9)
        if campo[posicionF][posicionC] == "~":
            campo[posicionF][posicionC] = "1"
            barcos += 1   
    return campo

def mostrar(campo):
    print("TABLERO")
    for i in range(len(campo)):
        for j in range(len(campo)):
            if campo[i][j] == "1":
                print("~", end=" ")
            else:
                print(campo[i][j], end=" ")
        print()
def disparo(campo,total_disparos,total_impactos,total_fallos,barcos_hundidos,final):
    
    print("DISPARAR")
    try:
        fila = int(input("Ingrese una fila del 1 al 10: "))-1
        columna = int(input("ingrese una columna del 1 al 10: "))-1
    except ValueError:
        print("Debe ingresar numeros")
        guardar_error("Error: fila o columna no numerica")
        
    if fila > 9 or fila < 0 or columna > 9  or columna < 0:
       print("Posicion invalida")
       guardar_error("Error: posicion invalida ingresada")

    elif campo[fila][columna] == "X" or campo[fila][columna] == "0":
        print("No se puede disparar dos veces a la misma posicion")
        guardar_error(f"Error: intento de disparo repetido en ({fila+1},{columna+1})")
 
    elif campo[fila][columna] == "~":
        campo[fila][columna] = "0"
        print("Agua")
        total_disparos += 1
        total_fallos += 1
    
    elif campo[fila][columna] == "1":
        campo[fila][columna] = "X"
        print("Impacto")
        barcos_hundidos += 1
        total_disparos += 1
        total_impactos += 1
        final -= 1
        
    return campo, total_disparos, total_impactos,total_fallos, barcos_hundidos, final

def estadisticas(total_disparos,total_impactos,total_fallos,barcos_hundidos):
    efectividad = 0
    if total_disparos != 0:
        efectividad = (total_impactos/total_disparos) * 100
    else:
        efectividad = 0
    print("Cantidad total de disparos:",total_disparos)
    print("Cantidad de impactos:",total_impactos)
    print("Cantidad disparos fallidos:",total_fallos)
    print("Cantidad de barcos hundidos:",barcos_hundidos)
    print("La efectividad es de",efectividad,"%")

def guardar_error(mensaje):
    archivo = open("errores.txt", "a")
    archivo.write(mensaje + "\n")
    archivo.close()

def menu():
    print("\nMENU")
    print("1. Mostrar tablero")
    print("2. Realizar un disparo")
    print("3. Mostrar estadisticas")
    print("4. Salir del juego")


def iniciar():
    final = 5
    total_disparos = 0
    total_impactos = 0
    total_fallos = 0
    barcos_hundidos = 0
    campo = [["~"] * 10 for i in range(10)]
    opcion = 0
    generar(campo)
    
    while final != 0:
        menu()
        try:
            opcion = int(input("Ingrese una opcion: "))
        except ValueError:
            print("Debe ingresar un numero")
            guardar_error("Error: se ingreso un valor no numerico en el menu")
            continue    
        if opcion == 1:
            mostrar(campo)
        elif opcion == 2:
            campo,total_disparos,total_impactos,total_fallos,barcos_hundidos,final = disparo(campo,total_disparos,total_impactos,total_fallos,barcos_hundidos,final)
        elif opcion == 3:
            estadisticas(total_disparos,total_impactos,total_fallos,barcos_hundidos)
        elif opcion == 4:
            for i in range(len(campo)):
                print(campo[i])
            print("Saliendo del sistema")
            break
        else:
            print("opcion invalida")
            guardar_error(f"Error: opcion invalida ({opcion})")
    print("Felicidades ganaste el juego")
iniciar()
