cantidad = int(input("Ingrese la cantidad de productos: "))

if cantidad % 100 == 0:
    resultado = cantidad
else:
    resultado = cantidad + (100 - (cantidad % 100))

print("La cantidad ajustada a la siguiente centena es:", resultado)