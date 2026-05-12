#Diferencia de Velocidad: Un radar registra la velocidad de un auto. 
# Si la velocidad es distinta de 0, informar si está avanzando. 
# Si es 0, informar "Vehículo Detenido".
velocidad = float(input("Ingrese la velocidad del vahiculo al radar: "))
if velocidad > 0:
    print("Vehiculo avanzando")
else:
    print("Vehículo Detenido")