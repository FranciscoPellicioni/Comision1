mes = int(input("Ingrese el numero del mes: "))
meses = ["Enero",
"Febrero",
"Marzo",
"Abril",
"Mayo",
"Junio",
"Julio",
"Agosto",
"Septiembre",
"Octubre",
"Noviembre",
"Diciembre"]
if 1 <= mes <= 12:
    print("Mes:", meses[mes- 1])
else:
    print("Numero invalido")