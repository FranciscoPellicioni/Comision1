
try:
 edad = int(input("ingrese su edad:"))
 cant_vac = int(input("ingrese las dosis aplicadas:"))
 if edad >= 18 and cant_vac >= 2:
  print("Mayor de edad\nEstado: completo\nPase sanitario habilitado")
 elif edad < 18 and cant_vac >= 2:
  print("Menor de edad\nEstado: completo\nApto para actividades")
 else:
    cant_vac < 2
    print("Debe completar esquema")
except ValueError:
     print("los datos ingresados son errones, porfavor volver a intentar")