#ingrese las edades de 10 alumnos e indicar cuál es la edad promedio y muestre las edades que están sobre el promedio calculado.
edadTotal = 0
vec1 = [0] * 10
for i in range(10):
    vec1[i] = int(input("Ingrese las edades: "))
    edadTotal += vec1[i]
    
promedio = edadTotal/10
print("La edad promedio es:",promedio)
print("Las edades por encima del promedio son:")
for i in range(10):
 if vec1[i] > promedio:
     print(vec1[i])
     
