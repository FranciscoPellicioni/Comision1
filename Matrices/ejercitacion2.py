#Rellenar una matriz de identidad de 4 por 4.

def rellenar(matrizIdentidad):
       for i in range(len(matrizIdentidad)):
        matrizIdentidad[i][i] = 1

def mostrar(matrizIdentidad):
    for i in range(len(matrizIdentidad)):
        print(matrizIdentidad[i])




def iniciar():
    matrizIdentidad = [[0]*4 for i in range(4)]
    rellenar(matrizIdentidad)
    mostrar(matrizIdentidad)

iniciar()