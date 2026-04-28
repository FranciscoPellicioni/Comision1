#Categoría de Vehículo: Solicitar el peso del vehículo en kg. 
# Si pesa más de 3500 kg, clasificarlo como "Vehículo Pesado", sino como "Vehículo Liviano".
peso = float(input("Ingrese el peso el vehiculo en kilogramos: "))

if peso > 3500:
    print("Vehículo Pesado")
else:
    print("Vehículo Liviano")