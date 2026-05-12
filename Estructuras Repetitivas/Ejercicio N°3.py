
n = int(input("cuantos numeros vas a ingresar:"))
menor = int(input("Ingrese un numero:"))
for i in range(n - 1):
    num = int(input("Ingrese un numero:"))
    if num < menor:
        menor = num
        
print("El numero menor es:",menor)