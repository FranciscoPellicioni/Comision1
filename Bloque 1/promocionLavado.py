#Promoción de Lavado: Si el monto de carga de combustible supera los $40.000, 
# informar que el cliente ha ganado un "Cupón de Lavado Gratis".

precioCarga = float(input("Ingrese el precio de la carga de combustible: "))

if precioCarga > 40000:
    print("Usted ha ganado un Cupón de Lavado Gratis")