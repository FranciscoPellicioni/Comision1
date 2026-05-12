#Apto para Circular: Pedir el año de fabricación del auto. 
# Si tiene más de 20 años de antigüedad, informar que requiere una "Inspección Especial".

añoFabricacion = int(input("Ingrese el año de fabrcacion del vhiculo: "))
año =  2026
antiguedad = (año - añoFabricacion)

if antiguedad > 20:
 print("El vehiculo requiere una Inspección Especial")

