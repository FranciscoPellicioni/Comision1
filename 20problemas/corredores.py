#Ejercicio 8: Competencia de ciclismo
# Ingresar los tiempos de 18 corredores. Determinar quién obtuvo el menor tiempo y cuántos
# corredores superaron las 2 horas de carrera.

corredores = 0
menorTiempo = 40
ciclistaMenor = 0
for i in range(0,18):
    tiempo = float(input(f"Ingrese el tiempo del ciclista {i+1}:"))
    
    if  tiempo > 2:
        corredores += 1
    if tiempo < menorTiempo:
        menorTiempo = tiempo
        ciclistaMenor = i + 1
       
        
    
print(f"El menor tiempo fue el ciclista {ciclistaMenor} con {menorTiempo}\nLa cantidad de ciclistas con mas de 2 horas de carrera es {corredores}:")