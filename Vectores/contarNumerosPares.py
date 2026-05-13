#Realice un programa que ingresando 10 numeros,  
# se indique la cantidad total de numero pares ingresados, mostrando la posición de carga de cada uno.
numPares = 0
vec1 = [0] * 10
for i in range(10):
    vec1[i] = int(input("Ingrese las numeros: "))

    if vec1[i] % 2 == 0:
      numPares += 1
print("La cantidad de numeros pares es:",numPares)
print("Numeros:")
for i in range(0,10):
 if vec1[i] % 2 == 0:
      numPares += 1
      print(i)




