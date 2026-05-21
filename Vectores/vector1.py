#Cargar 5 números enteros en un array y mostrarlos en el mismo orden en que fueron ingresados.
vec = [0] * 5
for i in range(len(vec)):
    vec[i] = int(input("ingrese un numero: "))
    
print("El vector es:",vec)