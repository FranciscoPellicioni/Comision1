#Generar un código que solicite al usuario un numero entero 
# (se asume que el usuario ingresará siempre un entero, positivo e impar), y luego se dimensione una matriz nxn (donde n es el valor ingresado), 
# dicha matriz es inicializada en ceros y luego se le pide al usuario una opcion:

#1dentidad
#2Identidad inversa
#3Bordes laterales
#4Bordes superiores
#5Todos los bordes
#6Forma de suma (+)
#7Todas combinadas

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="")
        print()



def identidad(matriz):
       for i in range(len(matriz)):
        matriz[i][i] = 1

def identidad_inversa(matriz):
    n = len(matriz)
    for i in range(n):
        matriz[i][n - 1 - i] = 1


def bordes_laterales(matriz):
    n = len(matriz)
    for i in range(n):
        matriz[i][0] = 1
        matriz[i][n - 1] = 1


def bordes_superiores(matriz):
    n = len(matriz)
    for j in range(n):
        matriz[0][j] = 1
        matriz[n - 1][j] = 1


def todos_los_bordes(matriz):
    bordes_laterales(matriz)
    bordes_superiores(matriz)


def forma_suma(matriz):
    n = len(matriz)
    medio = n // 2

    for i in range(n):
        matriz[i][medio] = 1

    for j in range(n):
        matriz[medio][j] = 1


def todas_combinadas(matriz):
    identidad(matriz)
    identidad_inversa(matriz)
    todos_los_bordes(matriz)
    forma_suma(matriz)

def iniciar():
    n = int(input("Ingrese un numero entero positivo e impar: ")) 
    filas = n
    columnas = n
    matriz = [[0] * columnas for i in range(filas)]

    print("Opciones:")
    print("1. Identidad")
    print("2. Identidad inversa")
    print("3. Bordes laterales")
    print("4. Bordes superiores")
    print("5. Todos los bordes")
    print("6. Forma de suma (+)")
    print("7. Todas combinadas")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        identidad(matriz)
    elif opcion == 2:
        identidad_inversa(matriz)
    elif opcion == 3:
        bordes_laterales(matriz)
    elif opcion == 4:
        bordes_superiores(matriz)
    elif opcion == 5:
        todos_los_bordes(matriz)
    elif opcion == 6:
        forma_suma(matriz)
    elif opcion == 7:
        todas_combinadas(matriz)
    else:
        print("Opcion incorrecta")
        return

    mostrar_matriz(matriz)


iniciar()
