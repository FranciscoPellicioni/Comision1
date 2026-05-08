#Ejercicio 1 — Contador de pares
#Pedi 10 numeros al usuario y conta cuantos son pares. Mostrar el resultado al final.

pares = 0

for i in range(0,10):
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        pares += 1
print("La cantidad de numeros pares es:",pares)
