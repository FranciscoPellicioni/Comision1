#Ejercicio 2 — Suma de impares
# Pedi 10 numeros al usuario y suma solo los que sean impares. Mostrar la suma total al final.

impares= 0

for i in range(0,10):
    num = int(input("Ingrese un numero: "))
    if num % 2 != 0:
        impares += num
print("La suma de los numeros impares es:",impares)
