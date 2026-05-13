#Ejercicio 2 guia vectores

vector1  = [0] * 3
vector2  = [0] * 3
vector3  = [0] * 3
for i in range(0,3):
    vector1[i] = int(input(f"Ingrese el elemento {i + 1} del vector 1: "))
    vector2[i] = int(input(f"Ingrese el elemento {i + 1} del vector 2: "))  
    vector3[i] = vector1[i] * vector2[i]  
print("\nVector 1:", vector1)
print("Vector 2:", vector2)
print("Vector resultante:", vector3)