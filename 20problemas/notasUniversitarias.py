#Ejercicio 5: Control de notas universitarias
# Ingresar las notas de 30 alumnos. Informar cantidad de aprobados, desaprobados, promedio del
# curso y nota más alta.
desaprobados = 0
aprobados = 0
notaAlta = 0
totalnotas = 0
for i in range(30):
    nota = float(input("Ingrese la nota: "))
    if nota < 6:
        desaprobados += 1
        totalnotas = totalnotas + nota
    else:
        aprobados += 1
        totalnotas = totalnotas + nota
    if nota > notaAlta:
        notaAlta = nota
promedio = totalnotas/30

print(f"Alumnos aprobados: {aprobados}\nAlumnos desaprobados: {desaprobados}\nEl promedio del curso es: {promedio}\nLa nota mas alta es: {notaAlta}")

