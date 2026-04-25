#Pedir saldo actual y monto a extraer.
#Validar:
#• que el monto sea múltiplo de 1000,
#• que no supere el saldo,
#• y que no sea mayor a $100000 por operación.
#Mostrar si la extracción fue aprobada y el saldo restante, o indicar por qué fue rechazada.

saldo_actual = float(input("ingrese su saldo actual: "))
monto_extraer = float(input("ingrese el monto a extraer: "))
if monto_extraer % 1000 == 0 and monto_extraer < saldo_actual and monto_extraer < 100000:
    saldo_actual = saldo_actual - monto_extraer
elif monto_extraer % 1000 != 0: 
    print("La transaccion fue rechazada.\nMotivo: El monto no es multiplo de 1000")
elif monto_extraer > saldo_actual:
    print("La transaccion fue rechazada.\nMotivo: El monto a extraer es mayor que el saldo actual")
elif monto_extraer > 100000:
    print("La transaccion fue rechazada.\nMotivo: El monto a extraer no puede superar los $100000 por operacion")

print("Extraccion : Aprobada\nSaldo restante: ", saldo_actual)    