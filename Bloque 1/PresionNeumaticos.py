#Presión de Neumáticos: Pedir la presión actual de un neumático en PSI. 
# Si es menor a 28, mostrar un mensaje de "Alerta: Presión Baja".

presion = float(input("Ingrese la presionde los neumaticos en PSI:"))

if presion < 28:
    print("Alerta: Presión Baja")
