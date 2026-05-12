#Ejercicio 12 — Potencia sin operador **
# Pedir una base y un exponente. Calcular la potencia usando solo multiplicaciones dentro de un
# bucle, sin usar el operador ** ni la funcion pow().

base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = 1
for i in range(exponente):
    resultado *= base
print("El resultado es:",resultado)