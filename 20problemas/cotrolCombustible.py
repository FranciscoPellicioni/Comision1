#Ejercicio 13: Control de combustible
# Ingresar la cantidad de litros cargados por 40 vehículos en una estación de servicio. 
# Informar cuántos vehículos cargaron más de 40 litros y el total de litros vendidos.

mas40 = 0
litrosTotal = 0

for i in range(0,40):
    litros = float(input("Ingrese la cantidad de litros cargados: "))

    if litros > 40:
        mas40 += 1
        litrosTotal = litrosTotal + litros
    else:
        litrosTotal = litrosTotal + litros

print("El total de litros vendidos es:",litrosTotal)
print("La cantidad de vehiculos con mas de 40 lt cargados es:",mas40)