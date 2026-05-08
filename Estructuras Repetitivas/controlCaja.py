#Control de caja de un negocio
# Un negocio quiere controlar las ventas del día. El programa debe:
# Pedir el monto de cada venta una por una hasta que el vendedor ingrese 0 para cerrar la caja
# Por cada venta aplicar el descuento correspondiente:
# Si el monto es menor a $1000 ? sin descuento
# Si el monto es entre $1000 y $5000 ? 10% de descuento
# Si el monto es mayor a $5000 ? 20% de descuento
# Al final mostrar:
# Cantidad de ventas realizadas
# Total recaudado (con descuentos aplicados)
# El monto de la venta mas alta del dia
# Si el total recaudado supera los $50000 mostrar "Buen dia de ventas!", sino
# mostrar "Dia regular"
totalRecaudado = 0
ventTotales = 0
masAlto = 0
monto = float(input("Ingrese el monto de la venta o ingrese 0 para cerrar la caja: "))
              
while monto > 0:
   if monto >= 1000 and monto <= 5000:
      descuento = monto * 0.10
      monto_final = monto - descuento
      totalRecaudado += monto_final
      ventTotales += 1
      
   elif monto > 5000:
      descuento = monto * 0.20
      monto_final = monto - descuento
      totalRecaudado += monto_final
      ventTotales += 1
   if monto > masAlto:
       masAlto = monto
   
   monto = float(input("Ingrese el monto de la venta o ingrese 0 para cerrar la caja: "))
print("---AL CIERRE DE CAJA---")      
print("Ventas totales:",ventTotales,
      "\nTotal recaudado:",totalRecaudado,
      "\nVenta mas alta:",masAlto)
if totalRecaudado > 50000:
      print("Buen dia de ventas!")
else:
      print("Dia regular")  