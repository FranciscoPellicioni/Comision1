#Control de notas de un curso
# Un profesor necesita registrar las notas de sus alumnos. El programa debe:
# Pedir la cantidad de alumnos del curso
# Por cada alumno pedir su nombre y 3 notas
# Calcular el promedio de cada alumno
# Mostrar si el alumno aprobó (promedio >= 6) o desaprobó
# Al final mostrar:
# Cuántos alumnos aprobaron
# Cuántos desaprobaron
# El promedio general del curso

notas = 0
aprobados = 0
desaprobados = 0
notasGeneral = 0
notasIndividual = 0

cantAlumnos = int(input("Ingrese la cantidad de alumnos de su curso: "))

for i in range(cantAlumnos):
    nomAlumno = input(f"Ingrese el nombre del alumno {i+1}: ")
    notasIndividual = 0
    for j in range(0,3):
     nota = float(input(f"Ingrese la nota {j+1} del alumno {nomAlumno}: "))
     notasGeneral += nota
     notasIndividual += nota
     notas += 1
    promedioAlumno = notasIndividual/3
    if promedioAlumno >= 6:
        aprobados += 1
        print(f"El alumno {nomAlumno}, Aprobo con un promedio de {promedioAlumno}")

    else:
        print(f"El alumno {nomAlumno}, Desaprobo con un promedio de {promedioAlumno}")
        desaprobados += 1
promedioGeneral = notasGeneral/notas
print("---RESULTADOS FINALES---")
print("Aprobaron:",aprobados,
      "\nDesaprobaron:",desaprobados,
      "\nEl promedio general del curso es:",promedioGeneral)