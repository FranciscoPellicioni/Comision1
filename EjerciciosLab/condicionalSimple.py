nombre= input("ingrese su nombre completo:")
edad= int(input("ingrese su edad:"))
sueldo= float(input("ingrese su sueldo:"))
porcentaje= float(input("ingrese el porcentaje del descuento:"))
if edad < 18 :
 print( "el usuario  es menor de edad")
else:
      print("el usuario es mayor de edad y tiene:", edad,"años") 
descuento= (sueldo * porcentaje)/100
sueldo_final= sueldo - descuento
print("el total del sueldo es:", sueldo_final)
  
