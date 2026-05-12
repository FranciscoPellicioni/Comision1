#Ejercicio 4: Venta de entradas de cine 
# Ingresar la edad de los clientes hasta que se ingrese una edad negativa. Determinar el precio de la
# entrada según la edad y calcular cuántas entradas infantiles, generales y jubilados se vendieron.

edad = 0
infantiles = 0
generales = 0
jubilados = 0

while edad >= 0:
    edad = int(input("Ingrese su edad: "))
    if edad < 18:
        infantiles += 1
        precio = 1000
    elif edad >= 18 and edad < 60:
        generales += 1
        precio = 5000

    else:
        jubilados += 1
        precio = 2000

print(f"Entradas infantiles vendidas: {infantiles}\nEntradas generales vendidas: {generales}\nEntradas jubilados vendidas: {jubilados}")