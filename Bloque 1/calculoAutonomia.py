#Cálculo de Autonomía: Pedir los km que restan para el destino y los litros en el tanque. 
# Si la relación (km/litros) es mayor a 12, indicar "Combustible Suficiente", 
# de lo contrario "Cargar ahora".
km = float(input("Ingrese los kilometros restantes: "))
litros = float(input("ingrese los litros restantes: "))

if (km/litros) > 12:
    print("Combustible Suficiente")
else:
    print("Cargar ahora")