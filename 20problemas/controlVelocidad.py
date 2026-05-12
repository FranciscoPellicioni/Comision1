#Ejercicio 19: Control de velocidad
# Ingresar la velocidad de 60 vehículos detectados por un radar. Informar cuántos excedieron el límite
# permitido de 80 km/h y cuál fue la velocidad máxima registrada.


limite = 0
maxVelocidad = 0 
maxVehiculo = 0

for i in range(0,60):
    velocidad = float(input(f"Ingrese la velocidad del vehiculo {i+1}: "))

    if velocidad > 80:
        limite += 1
    
    if velocidad > maxVelocidad:
        maxVelocidad = velocidad
        maxVehiculo = i + 1

print("Limite excedido por:",limite,"vehiculos")
print(f"La velocidad maxima fue: {maxVelocidad}KM/H por el vehiculo: {maxVehiculo}")