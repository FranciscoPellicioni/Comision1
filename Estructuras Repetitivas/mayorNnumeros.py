#Ejercicio 3 — Mayor de N numeros
# El usuario decide cuantos numeros quiere ingresar. El programa debe mostrar el mayor de todos.

n = int(input("¿Cuantos numeros quiere ingresar? "))
numMayor = 0

for i in range(n):
    num = int(input("Ingrese un numero: "))
    if num > numMayor:
        numMayor = num

print("El numero mayor es:",numMayor)
