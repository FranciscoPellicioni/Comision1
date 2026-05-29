#Leer una matriz de 3 por 3 elementos y calcular la suma de cada una de sus filas y
#columnas, dejando dichos resultados en dos vectores, uno de la suma de filas y otro de las columnas.

def cargar(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = int(input(f"Ingrese el elemento [{i}][{j}] de la matriz: "))

def sumaFilas(matriz,sumaf,vec1):
    for i in range(len(matriz)):
        sumaf = 0
        for j in range(len(matriz)):
            sumaf += matriz[i][j]
        vec1.append(sumaf) 
    return sumaf

def sumaColumnas(matriz,sumaC,vec2):
    for j in range(len(matriz)):
        sumaC = 0
        for i in range(len(matriz)):
            sumaC += matriz[i][j]
        vec2.append(sumaC)
    return sumaC
def mostrar(vec1,vec2):
    print("La suma de todas las filas es:",vec1)
    print("La suma de todas las columnas es:",vec2)


def iniciar():
    vec1 = []
    vec2 = []
    sumaf = 0
    sumaC = 0
    matriz = [[0]*3 for i in range(3)]
    cargar(matriz)
    sumaf = sumaFilas(matriz,sumaf,vec1)
    sumaC = sumaColumnas(matriz,sumaC,vec2)
    mostrar(vec1,vec2)

iniciar()