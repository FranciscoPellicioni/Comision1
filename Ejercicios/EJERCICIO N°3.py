edad = int(input("ingrese su edad:"))
asistencia = int(input("ingrese su porcentaje de asistencia"))
if edad >= 18 and asistencia >= 90:
   print("Mayor de edad\nAsistencia: excelente\nPromocion directa")
elif edad < 18 and asistencia >= 75:
    print("Menor de edad\nAsistencia: Buena\nRegulariza la materia")
elif 75 > asistencia >= 60:
    print("Asistencia: Regular\nRegulariza la materia")
else: 
 print("Asistencia: Baja\nLibre por inasistencias")