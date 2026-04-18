N = int(input("Ingrese un número de 6 dígitos: "))

d1 = N // 100000
d2 = (N // 10000) % 10
d3 = (N // 1000) % 10
d4 = (N // 100) % 10
d5 = (N // 10) % 10
d6 = N % 10

suma = d1 + d2 + d3 + d4 + d5 + d6
cantidad = 6
R = suma / cantidad

print("El numero real R es=", R)