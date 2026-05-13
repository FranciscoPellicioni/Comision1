#Ejercicio 10: Encuesta de satisfacción
# Ingresar la puntuación otorgada por clientes de un restaurante (1 a 5). Finalizar el ingreso cuando
# se ingrese 0. Mostrar porcentaje de cada puntuación y promedio general.
cantPuntuaciones = 0
totalPuntuaciones = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
puntuacion = float(input("Que puntuacion le otorga al servicio prestado (1 a 5, 0 para terminar): "))
while  puntuacion != 0:
    
    if 1 <= puntuacion <= 5:
       totalPuntuaciones = totalPuntuaciones + puntuacion
       cantPuntuaciones += 1
       if puntuacion == 1:
           p1 += 1
       elif puntuacion == 2:
           p2 += 1
       elif puntuacion == 3:
           p3 += 1
       elif puntuacion == 4:
           p4 += 1
       elif puntuacion == 5:
           p5 += 1
    else:
        print("puntuacion invalida")
             
    puntuacion = float(input("Que puntuacion le otorga al servicio prestado (1 a 5, 0 para terminar): "))


if cantPuntuaciones > 0:
    print("Porcentaje de cada puntuación:")
    print("1:", (p1 / cantPuntuaciones) * 100, "%")
    print("2:", (p2 / cantPuntuaciones) * 100, "%")
    print("3:", (p3 / cantPuntuaciones) * 100, "%")
    print("4:", (p4 / cantPuntuaciones) * 100, "%")
    print("5:", (p5 / cantPuntuaciones) * 100, "%")

    promedio = totalPuntuaciones/cantPuntuaciones
    print("El promedio general de puntuaciones es:", promedio)
else:
    print("No se ingresaron puntuaciones")
