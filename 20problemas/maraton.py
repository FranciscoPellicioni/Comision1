#Ejercicio 12: Maratón solidaria
#Ingresar la distancia recorrida por 25 participantes. Determinar cuántos superaron los 10 km y
#calcular la distancia promedio recorrida.

mas10 = 0
distTotal = 0
for i in range(0,25):
    distancia = float(input(f"Ingrese la distancia recorrida: "))
    
    if  distancia > 10:
        mas10 += 1
    
    distTotal = distTotal + distancia
            


promedio = distTotal/25
   
       
        
    
print("La cantidad de participantes con mas de 10 km de carrera es:",mas10)
print("El promedio general es de:",promedio)