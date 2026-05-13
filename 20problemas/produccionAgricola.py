#Ejercicio 17: Producción agrícola
# Ingresar la cantidad de kilos cosechados por 10 campos durante una semana. Mostrar cuál obtuvo
# la mayor producción y el total cosechado.

mayorProdu = 0
totalCosecha = 0
campoMayor = 0
for i in range(0,10):
    kilos = float(input(f"Ingrese el total de KG cosechados del campo {i+1}: "))
    totalCosecha += kilos
    if kilos > mayorProdu:
        mayorProdu = kilos
        campoMayor = i + 1
    

print(f"El campo {campoMayor} es el que tiene la mayor produccion con:",mayorProdu,"KG")
print("El total cosechado es de:",totalCosecha,"KG")

