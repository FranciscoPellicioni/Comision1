# Juego de piedra, papel o tijera Usuario ingresa opción y la computadora otra (podés simularla).
#Determinar: empate, gana usuario o gana computadora
usuario = input("ingrese su eleccion, piedra, papel o tijera:")
contador = 0

for i in range(1,3):
 contador = contador + 1
if  contador % 3 == 1:
   cpu = "piedra"

elif contador % 3 == 2:
 cpu = "papel"

else:
  cpu ="tijera"

print("La cpu eligio:", cpu)


if cpu == usuario:
 print("Empate")
elif (usuario == "piedra" and cpu == "tijera") or \
      (usuario == "papel" and cpu == "piedra") or \
      (usuario == "tijera" and cpu == "papel"):
  print("Ganaste")
else:
  print("perdiste")