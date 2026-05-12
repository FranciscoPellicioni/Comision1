#Ejercicio 2: Torneo de pádel Ingresar la categoría de 20 jugadores (Primera, Segunda o Tercera). }
# Calcular el costo de inscripción según la categoría y mostrar el total recaudado y la cantidad de jugadores por categoría
cantPrimera = 0
cantSegunda = 0
cantTercera = 0
total = 0
for i in range(0, 4):

    categoria = input("Ingrese su categoria,\n[Primera]\n[Segunda]\n[Tercera]\n")

    if categoria == "Primera":
         total += 20000
         cantPrimera += 1
        
    elif categoria == "Segunda":
         total += 10000
         cantSegunda += 1
    
    elif categoria == "Tercera":
         total += 5000
         cantTercera += 1
    else:
         print("Categoría Inválida")
        

print(f"El total recaudado es de: {total}\n"f"La cantidad de jugadores en Primera es: {cantPrimera}\n"f"La cantidad de jugadores en Segunda es: {cantSegunda}\n"f"La cantidad de jugadores en Tercera es: {cantTercera}")