#Crear un programa modular para gestionar las notas de N alumnos. Cada alumno tiene 3 notas.
#Usar funciones separadas para cada tarea del programa. 
# Funciones requeridas:
#• pedir_notas(alumno) → pide y retorna 3 notas
#• calcular_promedio(n1, n2, n3) → retorna el promedio
#• evaluar(promedio) → retorna 'Aprobado' o 'Desaprobado'
#• mostrar_resultado(alumno, promedio, condicion) → muestra los datos
#• mejor_promedio(promedios) → retorna el mayor promedio del curso

def pedir_notas(matriz,n,m):
    for i in range(n):
        for j in range(m):
            matriz[i][j] = float(input(f"ingrese la nota [{j}] del alumno [{i}]: "))
    print(matriz)

def calcular_promedio(matriz,i,promedio,m):
    total = 0
    for j in range(m):
        total += matriz[i][j]

    promedio = total/m
    return promedio

def evaluar(promedio):
    if promedio >= 6:
        estado = "Aprobado"
    else:
        estado = "Desaprobado"
    return estado
def mostrar_resultado(alumno,promedio,estado):
    
        print(f"El alumno [{alumno}] tiene un promedio de:",promedio,"condicion final:",estado)

def mejor_promedio(promedios):
    mayor = promedios[0]

    for i in range(len(promedios)):
        if promedios[i] > mayor:
            mayor = promedios[i]

    return mayor

def iniciar():
    n = int(input("Ingrese la cantidad de alumnos: "))
    m = int(input("Igrese la cnatidad de notas a cargar: "))
    matriz = [[0]* m for i in range(n)]
    promedios = []
    promedio = 0
    estado = ""
    pedir_notas(matriz,n,m)
    for i in range(n):
        promedio = calcular_promedio(matriz,i,promedio,m)
        estado = evaluar(promedio)
        mostrar_resultado(i+1,promedio,estado)
        promedios.append(promedio)

    mayor = mejor_promedio(promedios)

    print("\nEl mejor promedio del curso es:", round(mayor,2))

iniciar()
