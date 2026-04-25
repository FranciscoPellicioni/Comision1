
tipo_cliente = input("Es usted cliente premium?, responda con si o no:")
destino = input("es usted del interior?, esponda con si o no:")
peso = float(input("ingrese el peso del prodcto:"))
if peso <= 5:
 costo = peso * 2000
elif 5 < peso <=20:
    costo = peso * 5000
else:
    costo = peso * 10000
if destino == ("si"):
  recargo = float(costo * 0.15)
  costo_final1 = costo + recargo
  print(costo_final1)
elif tipo_cliente == ("si"):
    descuento = float(costo * 0.20)
    costo_final2 = costo - descuento
    print(costo_final2)
else: 
 print("El costo final es:", costo)