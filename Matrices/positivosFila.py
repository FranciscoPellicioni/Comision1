#Contar positivos por fila

#Ingresar una matriz de 4x4 y mostrar cuántos positivos tiene cada fila.

columnas = 4
filas = 4
matriz = [[0]* columnas for i in range(filas)]
positivos = 0

for i in range(filas):
    positivos = 0
    for j in range(columnas): 
        matriz[i][j] = int(input("Ingrese los elemntos de una matriz 4x4: "))

        if matriz[i][j] > 0:
           positivos += 1
    print("en la fila:",i,"hay",positivos,"elemento/s positivo/s")