#Ejercicio 14: Tienda de celulares
#Registrar las ventas de 20 celulares indicando marca y precio. Aplicar descuentos según la marca y
#mostrar el total facturado y la cantidad de equipos vendidos por marca.

totalFacturado = 0
cantSamsung = 0
cantIphone = 0
cantXiaomi = 0

for i in range(0,20):
     celular = input("Ingrese la marca del celular:\n[Samsung]\n[Iphone]\n[Xiaomi]\n").lower()

     if celular == "samsung":
        precio = 20000
        cantSamsung += 1
        totalFacturado = totalFacturado + precio

     elif celular == "iphone":
        precio = 50000
        cantIphone += 1
        totalFacturado = totalFacturado + precio

     elif celular == "xiaomi":
        precio = 15000
        cantXiaomi += 1
        totalFacturado = totalFacturado + precio
     else:
        print("Marca incorrecta, intente de nuevo")
print("El total fcturado es de:",totalFacturado)
print("La cantidad de samsung vendidos es:", cantSamsung,
      "\nLa cantidad de iphone vendidos es:", cantIphone,
      "\nLa cantidad de xiaomi vendidos es:", cantXiaomi)

