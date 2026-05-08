edadTotal = 0
cantEdadMayor = 0
vec1 = [0] * 2

for i in range(2):
    vec1[i] = int(input("Ingrese las edades: "))
    edadTotal += vec1[i]
    
promedio = edadTotal/2
print("Promedio General:",promedio)   
    
for i in range(2):
    if vec1[i] > promedio:
     cantEdadMayor += 1
print("Cantidad de Edades mayores al promedio:",cantEdadMayor) 