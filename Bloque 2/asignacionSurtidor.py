#Asignación de Surtidor: Según el tipo de combustible (1: Nafta, 2: Diesel, 3: GNC) 
# y si es cliente "VIP" o "Regular", 
# mostrar a qué sector debe dirigirse. Nafta = surtidor 1; Diesel = surtidor 2; GNC = surtidor 3 
tipoCombustible = input("Ingrese el tipo de combustible:\n[Nafta]\n[Diesel]\n[GNC]\n")
tipoCliente = input("Ingrese su tipo de cliente:\n[VIP]\n[Regular]\n")


if tipoCombustible == "Nafta" and tipoCliente == "VIP":
  sector = "Surtidor 1 VIP"
elif tipoCombustible == "Nafta" and tipoCliente == "Regular":
  sector = "Surtidor 1 Regular"

elif tipoCombustible == "Diesel" and tipoCliente == "VIP":
   sector = "Surtidor 2 VIP"
elif tipoCombustible == "Diesel" and tipoCliente == "Regular":
   sector = "Surtidor 2 Regular"

elif tipoCombustible == "GNC" and tipoCliente == "VIP":
   sector = "Surtidor 3 VIP"
else:
   sector = "Surtidor 3 Regular"

print("Dirigirse a:", sector)