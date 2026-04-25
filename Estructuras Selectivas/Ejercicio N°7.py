#Ingresar precio y cantidad de cuotas:
# 1 cuota → sin interés
# 3 cuotas → 10% interés
# 6 cuotas → 20% interés
# 12 cuotas → 40% interés
#Calcular valor final y valor por cuota
try:
 precio = float(input("Ingrese el precio: "))
 cuotas = int(input("Seleccione las cuotas, 1, 3, 6, o 12: "))

 if cuotas == 1:
    print("El precio final es: $", precio)

 elif cuotas == 3:
    interes = precio * 0.10
    precio_final = precio + interes
    valor_cuota = precio_final / cuotas

 elif cuotas == 6:
     interes = precio * 0.20
     precio_final = precio + interes
     valor_cuota = precio_final / cuotas

 elif cuotas == 12:
     interes = precio * 0.40
     precio_final = precio + interes
     valor_cuota = float(precio_final / cuotas)
except ValueError:
  print("Los datos ingresados son incorrectos")

print("El valor final es: $", precio_final, "y las cuotas quedan en: $", valor_cuota, "cada una")
