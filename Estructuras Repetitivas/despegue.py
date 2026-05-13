#Ejercicio 6 — Cuenta regresiva
# Pedir un numero N y mostrar una cuenta regresiva desde N hasta 1.
# Al finalizar mostrar Despegue!.

num = int(input("Ingrese un numero: "))
cuenta = 0
for i in range(num,-1,-1):
    cuenta = i
    print("cuenta regresiva:",cuenta)

print("Despegue!")