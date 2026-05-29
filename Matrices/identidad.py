#Ingresar una matriz de nxn, donde n no supera la decena y determinar si se trata de una matriz identidad.

#La entrada son los valores de la matriz cargando fila 1 columna 1, fila 1 columna 2, fila 1 columna n, y luego fila 2 columna 1, fila 2 columna 2, fila 2 columna n, 
# y asi sucesivamente hasta fila n columna 1, fila n columna 2, fila n columna n

#La salida debe ser un texto que indique "Es Matriz Identidad", "No Es Matriz Identidad"

def cargar(filas,columnas,matriz):
    for i in range(filas):
        for j in range(columnas):
            matriz[i][j] = int(input(f"Ingrese el elemento [{i}][{j}] de la matriz: "))
            
def mostrar(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
      

def identidad(matrizIdentidad):
       for i in range(len(matrizIdentidad)):
        matrizIdentidad[i][i] = 1

def verificar(matriz,matrizIdentidad):
    
    if matriz == matrizIdentidad:
        print("Es Matriz Identidad")
    else:
        print("No Es Matriz Identidad")
       
          
def iniciar():
    n = int(input("Ingrese un numero mayor que cero pero menor que 10: "))
    filas = n
    columnas = n
    matriz = [[0]*columnas for i in range(filas)]
    matrizIdentidad = [[0]*columnas for i in range(filas)]

    cargar(filas,columnas,matriz)
    mostrar(matriz)
    identidad(matrizIdentidad)
    verificar(matriz,matrizIdentidad)

iniciar()