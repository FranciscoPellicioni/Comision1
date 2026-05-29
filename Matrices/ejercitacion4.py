#Calcular la suma de todos los elementos de una matriz 5x5, así como la media aritmética de
#los mismos.


def cargar(matriz,cont):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = int(input(f"Ingrese el elemento[{i}][{j}] de la matriz: "))
            cont += 1
    return cont
    for i in range(len(matriz)):
        print(matriz)

def sumar(matriz,suma):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            suma += matriz[i][j]
    return suma
def media(promedio,suma,cont):
    promedio = suma/cont
    return promedio

def mostrar(suma,promedio):
    print("La suma de todos los elementos es:",suma)
    print("La media aritmetica es:",promedio)






def iniciar():
    n = int(input("Ingrese un numero entero y positivo: "))
    columnas = n
    filas = n
    matriz = [[0]*columnas for i in range(filas)]
    cont = 0
    suma = 0
    promedio = 0
    cont = cargar(matriz,cont)
    suma = sumar(matriz,suma)
    promedio = media(promedio,suma,cont)
    mostrar(suma,promedio)
   
    
iniciar()