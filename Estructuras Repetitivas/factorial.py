#Ejercicio 5 — Factorial
# Pedir un numero N al usuario y calcular su factorial usando un bucle. No usar la funcion
# math.factorial().

factorial = 1

num = int(input("Ingrese un numero para calcular su factorial: "))

for i in range(1,num + 1):
    factorial *= i
print("El resultado es:",factorial)