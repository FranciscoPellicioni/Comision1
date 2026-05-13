#Ejercicio 15 — Cajero automatico
# El usuario ingresa un saldo inicial. Puede realizar extracciones de dinero repetidas veces. El
# programa debe verificar que tenga saldo suficiente, no aceptar montos negativos, y terminar
# cuando el usuario ingrese 0 o el saldo llegue a 0. Mostrar el saldo final.


saldo = int(input("Ingrese su saldo inicial: "))
monto = int(input("Ingrese el monto a extraer: "))


while saldo > 0 and monto != 0:
    if monto > 0 and monto <= saldo:
      saldo -= monto
      print("Saldo restante:", saldo)
    elif monto < 0:
       print("El monto no puede ser negativo,intente otra vez")
    else:
       print("Saldo insuficiente")
    
    monto = int(input("Ingrese el monto a extraer: "))

print("El saldo final es:",saldo)

  
