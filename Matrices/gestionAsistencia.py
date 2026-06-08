#Ejercicio: Control de Asistencia en un Aula
#Una escuela desea registrar la asistencia de sus alumnos.
#La matriz tendrá:
#    • 30 filas (alumnos) 
#    • 5 columnas (días de la semana) 
#Cada posición contendrá:
#    • P = Presente 
#    • A = Ausente 
#Requerimientos
#    1. Generar asistencias aleatoriamente. 
#    2. Mostrar la matriz completa. 
#    3. Mostrar la cantidad de presentes por día. 
#    4. Mostrar la cantidad de ausencias por alumno. 
#    5. Determinar el alumno con mayor asistencia. 
#    6. Calcular el porcentaje general de asistencia.
import random
def generar(matriz):
    for i in range(30):
        for j in range(5):
            matriz[i][j] = random.choice(["P","A"])
    print("Asistencia generada")
    return matriz

def mostrar(matriz):
    print("LISTA ASISTENCIA")
    for i in range(len(matriz)):
        print("Alumno", i+1, matriz[i])

def por_dia(matriz):
    print("PRESENTES POR DIA")
    for j in range(5):
        presentes = 0
        for i in range(30):
            if matriz[i][j] == "P":
                presentes += 1
        print(f"Presentes dia {j + 1}:",presentes)
    

def por_alumno(matriz):
    print("AUSENCIAS POR ALUMNO")
    for i in range(30):
        ausencias = 0
        for j in range(5):
            if matriz[i][j] == "A":
                ausencias += 1

        print(f"Alumno {i + 1} tiene",ausencias,"ausencias")


def mayor_asistencia(matriz):
    alumno_mayor = 0
    mayor = 0
    for i in range(30):
        asistencia = 0
        for j in range(5):
            if matriz[i][j] == "P":
                asistencia += 1


        if asistencia > mayor:
            mayor = asistencia
            alumno_mayor = i
    print("El alumno",alumno_mayor + 1,"tiene la mayor asistencia con",mayor,"presentes")


def porcentaje(matriz):
    asistencia = 0
    for i in range(30):
        for j in range(5):
            if matriz[i][j] == "P":
                asistencia += 1

    porcentaje_general = (asistencia/150)*100
    print("El porcentaje de asistencia general es",porcentaje_general,"%")


def menu():
    print("\nMENÚ")
    print("1. Generar asistencia")
    print("2. Mostrar lista de asistencias")
    print("3. Mostrar la cantidad de presentes por día")
    print("4. Mostrar la cantidad de ausencias por alumno")
    print("5. Determinar el alumno con mayor asistencia")
    print("6. Calcular el porcentaje general de asistencia")
    print("7. Salir del sistema")


def iniciar():
    matriz = [["A"]* 5 for i in range(30)]

    opcion = 0

    while opcion != 7:
        menu()
        opcion = int(input("Seleccione una opcion: "))
        if opcion == 1:
            generar(matriz)
        elif opcion == 2:
            mostrar(matriz)
        elif opcion == 3:
            por_dia(matriz)
        elif opcion == 4:
            por_alumno(matriz)
        elif opcion == 5:
            mayor_asistencia(matriz)
        elif opcion == 6:
            porcentaje(matriz)
        elif opcion == 7:
            print("Saliendo del sistema...")
        else:
            print("La opcion ingresada es incorrecta")

iniciar()