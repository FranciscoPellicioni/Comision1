valTotal = 0
cantMayores = 0
fila = 3
columna = 3
matriz=[[0]*columna for i in range(fila)]

for i in range(fila):
    for j in range(columna):
        matriz[i][j]=int(input("Ingrese los valores:"))
        valTotal += matriz[i][j]
promedio =valTotal/(fila*columna)
for i in range(fila):
    for j in range(columna):
        if matriz[i][j] > promedio:
            cantMayores += 1
print(cantMayores)