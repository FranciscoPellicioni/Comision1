#Ejercicio 14 — Divisores de un numero
# Pedir un numero N al usuario y mostrar todos sus divisores. Un divisor es un numero que divide a N sin dejar resto
num = int(input("Ingrese un numero: "))
for i in range(1,num + 1):
    if num % i == 0:
        print("Los divisores de este numero son:",i)