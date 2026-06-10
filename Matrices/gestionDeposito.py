#Ejercicio: Gestión de Depósito de Mercadería
#Una empresa almacena cajas en un depósito organizado en una matriz de 8 filas por 8 columnas.
#Cada posición puede contener:
#    0 → espacio vacío o 1 → caja almacenada 
#Requerimientos
#    1. Inicializar el depósito vacío. 
#    2. Generar automáticamente 25 cajas en posiciones aleatorias. ( Usar la función random.randint)
#    3. Mostrar el mapa del depósito. 
#    4. Permitir almacenar una nueva caja. 
#    5. Permitir retirar una caja. 
#    6. Mostrar cuántas cajas hay almacenadas. 
#    7. Mostrar qué fila tiene mayor cantidad de cajas. 
#    8. Mostrar qué columna tiene menor cantidad de cajas.
import random
def generar_cajas(deposito):
    cajas = 0
    while cajas < 25:
        posicionF = random.randint(0,7)
        posicionC = random.randint(0,7)
        if deposito[posicionF][posicionC] == 0:
            deposito[posicionF][posicionC] = 1
            cajas += 1
    print("Cajas generadas correctamente")   
    return deposito

def mostrar(deposito):
    print("DEPOSITO")
    for i in range(len(deposito)):
        print(deposito[i])


def almacenar(deposito):
    fila = int(input("Ingrese una fila del 1 al 8: ")) -1
    columna = int(input("Ingrese una columna del 1 al 8: ")) -1
    if fila < 0 or fila >= 8 or columna < 0 or columna >= 8:
        print("Posicion invalida")
    
    elif deposito[fila][columna] == 0:
        deposito[fila][columna] = 1
        print("Caja almacenada")
    
    else:
        print("Esa posicion ya esta ocupada")


def retirar(deposito):
    fila = int(input("Ingrese una fila del 1 al 8: ")) -1
    columna = int(input("Ingrese una columna del 1 al 8: ")) -1
    if fila < 0 or fila >= 8 or columna < 0 or columna >= 8:
        print("Posicion invalida")
    
    elif deposito[fila][columna] == 1:
        deposito[fila][columna] = 0
        print("Caja retirada")
    
    else:
        print("Esa posicion ya esta libre")
    
            
def mostrar_cajas(deposito):
    cajas_almacenadas = 0
    for i in range(len(deposito)):
        for j in range(len(deposito)):
            if deposito[i][j] == 1:
                cajas_almacenadas += 1
    print("Hay",cajas_almacenadas,"cajas almacenadas en total")
    
def fila(deposito):
    fila_mayor = 0
    mayor = 0
    for i in range(len(deposito)):
        cajas = 0
        for j in range(len(deposito)):
            if deposito[i][j] == 1:
                cajas += 1
    if cajas > mayor:
        mayor = cajas
        fila_mayor = i
    print("La fila con mayor cantidad de cajas es",fila_mayor,"con",mayor)

def columna(deposito):
    menor = 1000000000
    columnaMenor= 0

    for j in range(len(deposito)):  
        cajas = 0

        for i in range(len(deposito)):  
            if deposito[i][j] == 1:
                cajas += 1

        if cajas < menor:
            menor = cajas
            columnaMenor = j

    print("La columna con la menor cantidad de cajas es:", columnaMenor + 1,"con",menor)
    

            

def menu():
    print("\nMENÚ")
    print("1. Generar cajas")
    print("2. Mostrar deposito")
    print("3. Almacenar caja")
    print("4. Retirar caja")
    print("5. Mostrar cantidad de cajas en total")
    print("6. Fila con mas cajas")
    print("7. Columna con menos cajas")
    print("8. Salir del sistema")


def iniciar():
    filas = 8
    columnas = 8
    deposito = [[0]* columnas for i in range(filas)]
    opcion = 0
    while opcion != 8:
       
        menu()
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            generar_cajas(deposito)
        elif opcion == 2:
            mostrar(deposito)
        elif opcion == 3:
            almacenar(deposito)
        elif opcion == 4:
            retirar(deposito)
        elif opcion == 5:
            mostrar_cajas(deposito)
        elif opcion == 6:
            fila(deposito)
        elif opcion == 7:
            columna(deposito)
        elif opcion == 8:
            print("Saliendo del sistema...")
        else:
            print("Opcion invalida")


iniciar()

