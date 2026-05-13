#Ejercicio 8 — Numero positivo obligatorio
# El programa debe pedir un numero positivo. Si el usuario ingresa un numero negativo o cero,
# debe volver a pedirlo hasta que ingrese uno valido. Al finalizar mostrar el numero aceptado.

num = int(input("Ingrese un numero: "))
    
while num <= 0:
    print("Porfavor ingrese otro numero")
    
    num = int(input("Ingrese un numero: "))

else:
    print("Numero valido:",num)