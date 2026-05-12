año = int(input("Ingrese el año:"))
mes = int(input("Ingrese el numero del mes: "))
bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0) 
if mes == 2:
      if bisiesto:
          print("El mes tiene 29 dias")
      else:
          print("El mes tiene 28 dias")
elif mes in ( 4, 6, 9, 11):
    print("El mes tiene 30 dias")
  
elif mes in (1, 3, 5, 7, 8, 10, 12):
     print("El mes tiene 31 dias")
else: 
    print("El mes ingresado es invalido")