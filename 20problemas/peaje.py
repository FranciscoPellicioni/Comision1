#Ejercicio 11: Sistema de peaje
#Registrar el tipo de vehículo de 50 vehículos que pasan por un peaje (auto, moto o camión).
#Calcular el monto total recaudado y la cantidad de vehículos por categoría.
cantPrimera = 0
cantSegunda = 0
cantTercera = 0
total = 0
for i in range(0,2):

    categoria = input("Ingrese su vehiculo:\n[auto]\n[moto]\n[camion]\n")

    if categoria == "auto":
         total += 2000
         cantPrimera += 1
        
    elif categoria == "camion":
         total += 5000
         cantSegunda += 1
    
    elif categoria == "moto":
         total += 1000
         cantTercera += 1
    else:
         print("Categoría Inválida")
        

print(f"El total recaudado es de: {total}\n"f"cantidad de autos: {cantPrimera}\n"f"cantidad de camiones: {cantSegunda}\n"f"cantidad de motos: {cantTercera}")