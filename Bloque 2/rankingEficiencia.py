#Ranking de Eficiencia: Pedir el consumo de combustible (litros cada 100km).
#< 5: "Excelente"
#5 a 8: "Normal"
#8: "Alto Consumo"

consumo = float(input("Ingrese el consumo de combustible(litros cada 100km): "))
if consumo < 5:
   eficiencia = "Excelente"

elif consumo >= 5 and consumo < 8:
   eficiencia = "Normal"

else:
   eficiencia ="Alto Consumo"

print("El consumo del vehiculo es:", eficiencia)