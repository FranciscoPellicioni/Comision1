#Mostrar un menú:
#1. Hamburguesa
#2. Pizza
#3. Ensalada
#4. Empanadas
#Luego pedir bebida: • agua • gaseosa
#Aplicar reglas:
#• Si elige ensalada + agua, descuento del 20%.
#• Si elige pizza + gaseosa, recargo del 10%.
#• En los demás casos, precio normal.
#Mostrar total final.
precio = 20000
comida = input("Seleccione su comida: \n1.Hamburguesa\n2.Pizza\n3.Ensalada\n4.Empanadas\nSeleccion: ")
bebida = input("Seleccione una bebida: \n• Agua\n• Gaseosa\nSeleccion: ")

if comida == "Ensalada" and bebida == "Agua":
    descuento = precio * 0.20
    totaal_final = precio - descuento
    print("El total final es: $", totaal_final)
elif comida == "Pizza" and bebida == "Gaseosa":
    recargo = precio * 0.10
    totaal_final = precio + recargo
    print("El total final es: $", totaal_final)
else:
    print("El total final es: $", precio)

