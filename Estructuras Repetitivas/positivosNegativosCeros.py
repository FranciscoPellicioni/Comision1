#Ejercicio 11 — Positivos, negativos y ceros
# Pedir N numeros al usuario y contar cuantos son positivos, cuantos negativos y cuantos son
# cero. Mostrar los tres contadores al final.

positivos = 0
negativos = 0
ceros = 0

n = int(input("¿Cuantos numeros quiere ingresar? "))

for i in range(n):
    num = int(input("Ingrese un numero: "))
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        ceros += 1
print("Positivos:",positivos,
      "\nNegativos:",negativos,
      "\nCeros:",ceros)
