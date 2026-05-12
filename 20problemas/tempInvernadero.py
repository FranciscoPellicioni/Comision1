#Ejercicio 1: Control de temperatura en un invernadero.
# Ingresar la temperatura registrada cada hora durante 24 horas. Informar cuántas mediciones
# estuvieron por debajo de 10°C, cuántas superaron los 30°C y calcular el promedio general.

tempTotal = 0
tempSuperior = 0
tempInferior = 0
for i in range(0,24):
    temp  = float(input("Ingrese la temperatura actual: "))
    tempTotal = tempTotal + temp
   
    if temp > 30:
        tempSuperior += 1
    elif temp < 10:
        tempInferior += 1
 


promedio = tempTotal/24

print(f"""
Resultados:
- Mediciones < 10°C: {tempInferior}
- Mediciones > 30°C: {tempSuperior}
- Promedio general: {promedio}
""")

  