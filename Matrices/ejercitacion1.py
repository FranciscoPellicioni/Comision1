#Escribir un algoritmo que permita obtener el número de elementos positivos, negativos,
#nulos, mayores a 250, iguales a 19 e inferiores a 90 de una matriz de 50x50 componentes.

def cargar(matriz):
     for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = int(input(f"Ingrese el elemento [{i}][{j}] de la matriz: "))

def positivo(matriz,positivos):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] > 0:
                positivos += 1
    return positivos

def negativo(matriz,negativos):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] < 0:
                negativos += 1
    return negativos 

def nulo(matriz,nulos):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == 0:
                nulos += 1
    return nulos

def mayor(matriz,mayores):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] > 250:
                mayores += 1
    return mayores

def igual(matriz,iguales):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if 19 == matriz[i][j]:
                iguales += 1
    return iguales
            
def menor(matriz,menores):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] < 90:
                menores += 1
    return menores

def mostrar(positivos,negativos,nulos,mayores,iguales,menores):
    print(f"RESULTADOS\nPositivos: {positivos}\nNegativos: {negativos}\nNulos: {nulos}\nMayores: {mayores}\nIguales: {iguales}\nMenores: {menores}")


def iniciar():
    positivos = 0
    negativos = 0
    nulos = 0
    mayores = 0
    iguales = 0
    menores = 0
    matriz = [[0]*50 for i in range(50)]
    cargar(matriz)
    positivos = positivo(matriz,positivos)
    negativos = negativo(matriz,negativos)
    nulos = nulo(matriz,nulos)
    mayores = mayor(matriz,mayores)
    iguales = igual(matriz,iguales)
    menores = menor(matriz,menores)
    mostrar(positivos,negativos,nulos,mayores,iguales,menores)
    
iniciar()
