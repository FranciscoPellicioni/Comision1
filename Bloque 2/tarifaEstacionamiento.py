#Tarifa de Estacionamiento: Pedir las horas de permanencia. 
# La primera hora cuesta $1500. 
# A partir de la segunda, cada hora cuesta $1000. 
# Si se queda más de 12 horas, se cobra una tarifa plana de $10.000.
horas = float(input("ingrese las horas estacionadas:"))

if horas > 12:
    total_pagar = 10000
elif  horas <= 1:
    total_pagar = horas * 1500
else:
    total_pagar = 1500 + ((horas - 1)*1000)

print("El monto final es: $", total_pagar)