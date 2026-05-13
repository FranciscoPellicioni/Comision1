#Ejercicio 18: Aplicación de delivery
# Registrar la cantidad de pedidos entregados por 15 repartidores. Calcular el pago de cada
# repartidor considerando un bono si supera las 30 entregas.

precio_entrega = 2000
bono = 10000


for i in range(0,15):
    entrega = int(input(f"Ingrese la cantidad de pedidos del repartidor {i+1}: "))

    paga = (entrega * precio_entrega)
    
    if entrega > 30:
        paga += bono
        print(f"Repartidor {i+1}: Superó las 30 entregas, recibe bono.")
    
    print(f"Repartidor {i+1}: Total a cobrar = ${paga}\n")
     
        
  
        
       
