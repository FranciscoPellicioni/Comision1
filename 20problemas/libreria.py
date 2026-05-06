#Ejercicio 9: Control de stock de librería
#Registrar las ventas diarias de un producto durante 7 días. El stock inicial es de 120 unidades.
#Mostrar el stock restante y advertir si en algún momento el stock fue menor a 10 unidades.
stock = 120
dia = 0
for i in range(7):
    ventas = int(input("Ingrese cuantas unidades se vendieron del producto en el dia: "))
    stock = stock- ventas
    dia = i + 1
    print("El stock restante al final del dia es:",stock)
    if stock < 10:
     print("El stock  fue menor a 10 en el dia:",dia)




    
    
