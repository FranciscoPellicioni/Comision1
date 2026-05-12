#Carga de Combustible: El sistema debe solicitar los litros cargados y el precio por litro. 
# Calcular el total. Si el cliente paga con efectivo, aplicar un 5% de descuento. 
# Mostrar el monto final

litros_cargados = int(input("Ingrese los litros: "))
precio_litro = float(input("Ingrese el precio: "))
pago = input("Seleccione el metodo de pago: \n[Efectivo]\n[Tarjeta]\n")
total = litros_cargados * precio_litro

if pago == "Efectivo":
    descuento = total * 0.05
    total_final = total - descuento
    print("El monto final es:$", total_final)
else:
    print("El monto final es:$", total)