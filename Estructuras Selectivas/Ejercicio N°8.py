#ingresar día, mes y año, y determinar si la fecha es válida.
#Tener en cuenta:
# meses de 30 días,
# meses de 31 días,
# febrero con 28 o 29 según corresponda. 
dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el numero del mes: "))
año = int(input("Ingrese el año: "))

bisiesto = (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)
fecha_valida = True
if 1 > mes > 12:
    fecha_valida = False
else:
    if mes == 2:
        if bisiesto:
            dias_mes = 29
        
        else:
            dias_mes = 28
    elif mes in ( 4, 6, 9, 11):
        dias_mes = 30
    else:
        dias_mes = 31
    if dia < 1 or dia > dias_mes:
        fecha_valida = False
if fecha_valida == True:
    print("La fecha es valida")
else:
    print("La fecha es invalida")
