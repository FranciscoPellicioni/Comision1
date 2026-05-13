#Ejercicio 7 — Promedio con calificacion
# Pedir 5 notas al usuario. Calcular el promedio. Si el promedio es mayor o igual a 6 mostrar
# Aprobado, caso contrario Desaprobado.

totalNotas = 0

for i in range(0,5):
    nota = float(input(f"Ingrese su nota {i+1}: "))
    totalNotas += nota

promedio = totalNotas/5
if promedio >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

print("Su promedio es:",promedio)