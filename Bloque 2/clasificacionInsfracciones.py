#Clasificación de Infracciones: Pedir la velocidad detectada (límite 110 km/h).
#Hasta 110: "Sin infracción"
#111 a 130: "Multa Leve"
#> 130: "Multa Grave y Retención"

velocidad = float(input("Ingrese la velocidad detectada: "))

if velocidad <= 110:
    infraccion = "Sin infracción"

elif velocidad > 110 and velocidad <= 130:
    infraccion = "Multa Leve"

else:
    infraccion = "Multa Grave y Retención"

print("Clasificación:", infraccion)
