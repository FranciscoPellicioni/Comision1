#Ejercicio 4 — Adivina el numero
# El programa tiene un numero fijo secreto. El usuario debe adivinarlo. Si ingresa un numero
# menor mostrar Es mayor, si ingresa uno mayor mostrar Es menor. Repetir hasta que adivine.

n = 555
num = 0
while num != n:
    num = int(input("Ingrese un numero del 1 al 1000: "))
    if num > n:
        print("Es menor")
    elif num < n:
        print("Es mayor")
    else:
        print("Adivinaste, ganaste una coca")