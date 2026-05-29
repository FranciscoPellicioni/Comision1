#Calcular el número de elementos de negativos, cero y positivos de una matriz de 9x9 elementos.

def cargar(matriz,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = int(input(f"Ingrese el elemento[{i}][{j}] de la matriz: "))

def negativos(matriz,filas,columnas,negativo):
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] < 0:
                negativo += 1
    return negativo

def ceros(matriz,filas,columnas,cero):
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] == 0:
                cero += 1
    return cero

def positivos(matriz,filas,columnas,positivo):
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j] > 0:
                positivo += 1
    return positivo

def mostrar(matriz,filas,):
    print("\nMATRIZ")
    for i in range(filas):
        print(matriz[i])
    
def iniciar():
    filas = int(input("Ingrese el numero de filas de la matriz: "))
    columnas = int(input("Ingrese el numero de columnas de la matriz: "))
    matriz = [[0] * columnas for i in range(filas)]
    negativo = 0
    cero = 0
    positivo = 0
    cargar(matriz,filas,columnas)
    negativo = negativos(matriz,filas,columnas,negativo)
    cero = ceros(matriz,filas,columnas,cero)
    positivo = positivos(matriz,filas,columnas,positivo)
    mostrar(matriz,filas)
    print("\nCantidad Negativos:",negativo)
    print("Cantidad Ceros:",cero)
    print("Cantidad Positivos:",positivo)

iniciar()