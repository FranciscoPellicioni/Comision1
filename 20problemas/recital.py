#Ejercicio 16: Control de acceso a un recital
#Registrar las edades de las personas hasta que se ingrese 0. Informar cuántos son menores de
#edad, cuántos mayores y la edad promedio.

contMayores = 0
contMenores = 0
edadTotal = 0
contador = 0
edad = int(input("Ingrese la edad: "))

while edad != 0:
  
  if edad >= 18:
    contMayores += 1
    edadTotal = edadTotal + edad
    contador += 1
  else:
    contMenores += 1
    edadTotal = edadTotal + edad
    contador += 1
  edad = int(input("Ingrese la edad: "))
promedio = int(edadTotal/contador)

print("Menores:",contMenores,
      "\nMayores:",contMayores,
      "\nLa edad promedio es:",promedio)

   