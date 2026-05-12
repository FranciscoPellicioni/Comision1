#Ejercicio 15: Examen de manejo
# Ingresar el puntaje obtenido por 35 aspirantes. Si el puntaje es mayor o igual a 70, el aspirante
# aprueba. Informar cantidad de aprobados, desaprobados y promedio de puntajes

cantAprobados = 0
cantDesaprobados = 0
totalPuntajes = 0

for i in range(0,35):
    puntaje = float(input("Ingrese el puntaje obtenido: "))
    if puntaje >= 70:
        cantAprobados += 1
        totalPuntajes = totalPuntajes + puntaje
    else:
        cantDesaprobados += 1
        totalPuntajes = totalPuntajes + puntaje


promedio = totalPuntajes/4

print("Aprobados:",cantAprobados,
      "\nDesaprobados:",cantDesaprobados,
      "\nEl promedio es:",promedio)