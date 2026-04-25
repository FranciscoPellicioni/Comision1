
edad = int(input("ingrese su edad"))
monto = float(input("ingrese el monto de la compra"))
if edad >= 18 and monto >= 10000:
    print("Mayor de edad\nCompra: Alta\nDescuento: 15%" )
elif edad < 18 and 10000 > monto  >= 5000:
    print("menor de edad\nCompra: Media\nDescuento 10%")
else:
    print("Compra: Baja\nSin descuento")