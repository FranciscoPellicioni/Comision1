#Service de Aceite: Pedir los km actuales y los km del último service. 
# Si la diferencia es mayor a 10.000 km, mostrar "Cambio de aceite urgente".

km_actuales = float(input("Ingrese los km actuales:"))
km_ultimos = float(input("Ingrese los km del ultimo service:"))

if (km_actuales - km_ultimos) > 10000:
    print("Cambio de aceite urgente")