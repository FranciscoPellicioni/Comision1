#Sistema de Frenado: Pedir la eficiencia de frenado de los dos ejes del vehículo (0-100%). 
# El vehículo aprueba solo si ambos ejes superan el 50% y el promedio es superior al 60%.

eficiencia1 = float(input("Ingrese la eficiencia de frenado del eje 1: "))
eficiencia2 = float(input("Ingrese la eficiencia de frenado del eje 2: "))
promedio = (eficiencia1 + eficiencia2) /2
if eficiencia1 > 50 and eficiencia2 > 50 and promedio > 60:
    print("Vehiculo Aprobado")
else:
    print("Vehiculo Desaprobado")

