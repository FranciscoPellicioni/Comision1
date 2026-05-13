#Ejercicio 10 — Suma hasta ingresar 0
# Pedir numeros al usuario y sumarlos. El programa debe detenerse cuando el usuario ingrese 0.
# Mostrar la suma total al final.

suma = 0
num = int(input("Ingrese un numero, para finalizar ingrese cero: "))
while num != 0:
    suma += num
    num = int(input("Ingrese un numero, para finalizar ingrese cero: "))
print("La suma de estos numeros es:",suma)