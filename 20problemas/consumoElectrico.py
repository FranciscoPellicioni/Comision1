#Ejercicio 3: Consumo eléctrico domiciliario
# Ingresar el consumo mensual de energía de 15 viviendas. Aplicar un descuento del 10% si el consumo es menor a 250 kWh
# y un recargo del 15% si supera los 900 kWh. Mostrar el importe final
# de cada vivienda y el promedio general.
precioKwh = 200
totalPrecio = 0
totalConsumo = 0
for i in range(15):
    consumo = int(input(f"Ingrese el consumo mensual de energia de su vivienda {i+1}:" ))
    if consumo < 250:
        descuento = (consumo * precioKwh) * 0.10
        precio = (consumo * precioKwh) - descuento
        totalPrecio = totalPrecio + precio
        totalConsumo = totalConsumo + consumo
    elif consumo > 900:
        recargo = (consumo * precioKwh) * 0.15
        precio =  (consumo * precioKwh) + recargo
        totalConsumo = totalConsumo + consumo
        totalPrecio = totalPrecio + precio
    else:
        precio =  (consumo * precioKwh)
        totalConsumo = totalConsumo + consumo
        totalPrecio = totalPrecio + precio
    print(f"Vivienda {i+1} - Importe final: ${precio}")


promedioConsumo = totalConsumo/15

promedioPrecio =  totalPrecio/15

print(f"""
Promedio de consumo: {promedioConsumo} kWh
Promedio de importe: ${promedioPrecio}
""")





