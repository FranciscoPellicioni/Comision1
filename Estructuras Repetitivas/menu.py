#Ejercicio 13 — Menu interactivo
# Crear un menu con 4 opciones: 1) Saludar, 2) Despedirse, 3) Mostrar un mensaje
# personalizado, 4) Salir. El menu debe repetirse hasta que el usuario elija la opcion Salir


opcion = input("Seleccione una opcion del menu:\n1) Saludar\n2) Despedirse\n3) Mostrar un mensaje personalizado\n4) Salir\n")

while opcion != "4":
    if opcion == "1":
        print("HOLA!")

    elif opcion == "2":
        print("CHAU!")
    
    elif opcion == "3":
        mensaje = input("Escriba un mensaje personalizado: ")
        print("Mensaje:",mensaje)
    opcion = input("Seleccione una opcion del menu:\n1) Saludar\n2) Despedirse\n3) Mostrar un mensaje personalizado\n4) Salir\n")
print("Gracias por usar el menu, hasta luego")
