#ejercicio 9 — Tabla de multiplicar con filtro
# Pedir un numero N y mostrar su tabla de multiplicar del 1 al 10, pero solo mostrar los resultados
# que esten entre 20 y 60


num = int(input("Ingrese un numero: "))
for i in range(1,11):
 multiplicar = num * i
 if multiplicar > 20 and multiplicar < 60:
  print(num, "*",i, "=",num * i )
