#Validación de Turnos: Solicitar la hora de llegada del cliente (solo hora entera, 0-23). 
# Si la hora está entre las 8 y las 16, mostrar "Turno Mañana/Tarde", 
# de lo contrario "Guardia Nocturna".

hora = int(input("Ingrese la hora de llegada, 0-23: "))

if 8<= hora <= 16:
    print("Turno Mañana/Tarde") 
else:
    print("Guardia Nocturna")
