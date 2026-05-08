edadTotal = 0
cantEdadMayor = 0
vec1 = [0] * 10

for i in range(10):
    vec1[i] = int(input("Ingrese las edades: "))
    edadTotal += vec1[i]
    
promedio = edadTotal/10
print("Promedio General:",promedio)   
    
for i in range(10):
    if vec1[i] > promedio:
     cantEdadMayor += 1
print("Cantidad de Edades mayores al promedio:",cantEdadMayor) 