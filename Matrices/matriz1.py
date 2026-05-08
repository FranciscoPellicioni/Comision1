fila=5
columnas=4
#definición de una matriz
matriz=[[0]*columnas for i in range(fila)]

#Cargo los datos de la matriz
for i in range(fila):
    for j in range(columnas):
        matriz[i][j]=int(input())

#Recorro una matriz evaluando una condición en sus elemento
for i in range(fila):
    for j in range(columnas):
        if matriz[i][j]>0:
            print("El elemento de la fila ",i," y columna ",j, "es positivo")
        else:
            print("El elemento de la fila ", i, " y columna ", j, "es negativo")

#Visualizacion de los datos de la matriz
for i in range(fila):
    for j in range(columnas):
        print(matriz[i][j],end=" ") #Con el end le elimino el entre que incorpora el print
    print("") #Realizo el enter para que comience a imprimir la proxima fila de la matriz