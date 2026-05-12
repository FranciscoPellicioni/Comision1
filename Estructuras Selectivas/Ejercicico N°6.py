#Cobrar estacionamiento según estas reglas:
#• Hasta 2 horas: $1500 por hora.
#• Más de 2 y hasta 5 horas: $1200 por hora.
#• Más de 5 horas: $1000 por hora.
#Si el vehículo es de tipo "moto", tiene 30% de descuento. Si entra en horario nocturno (después de las 22), tiene además 10% de descuento extra.
#Mostrar total a pagar.

horas = int(input("ingrese las horas estacionadas:"))
tipo_vehiculo = input("Ingrese que vehiculo tiene:")
horario = int(input("ingrese el horario de entrada:"))

if horas <= 2:
    total_pagar = horas * 1500
elif 2 < horas <= 5:
    total_pagar = horas * 1200
else:
    total_pagar = horas * 1000


if tipo_vehiculo == "moto":
    descuento_vehiculo = float(total_pagar * 0.30)
    total_pagar = total_pagar - descuento_vehiculo 
    
if horario >= 22:
 descuento_horario = float(total_pagar * 0.10)
 total_pagar = total_pagar - descuento_horario 
 
print("El monto final es: $", total_pagar)