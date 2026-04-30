n = int(input("cuantos numeros vas a ingresar:"))
suma = 0 
for i in range(n):
    num = int(input("Ingrese un numero:"))
    suma = suma + num
        
print("La suma de estos numeros es:",suma)