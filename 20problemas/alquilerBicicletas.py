#Ejercicio 20: Sistema de alquiler de bicicletas
# Ingresar la cantidad de horas alquiladas por 25 clientes. Calcular el costo según las horas utilizadas
# y aplicar descuentos especiales si el alquiler supera las 5 horas.

costo_hora = 1500

for i in range(0,25):

    horas = float(input(f"Ingrese el total de las horas alquiladas del cliente {i+1}: "))

    costo_total = horas * costo_hora
    if horas > 5:
        descuento = costo_total * 0.15
        costo_total = costo_total - descuento
        print(f"cliente {i+1}: Superó las 5 horas, tiene descuento.")
            
    
    print(f"cliente {i+1}: Total a pagar = ${costo_total}\n")    
  
      

