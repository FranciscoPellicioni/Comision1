num_ganador = int(input())
num1 = int(input())
num2 = int(input())
 # Cálculo de diferencias
dif1 = abs(num_ganador - num1)
dif2 = abs(num_ganador - num2)
# Resultado
if dif1 < dif2:
    print("Ganador Jugador 1")
elif dif2 < dif1: 
    print("Ganador Jugador 2")