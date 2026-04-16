num = input()

# Eliminar espacios al inicio y al final
num = num.strip()

# Caso: no ingresa nada o solo espacios
if num == "":
    print("Error en el ingreso de los datos")

# Caso: no es un número
elif not (num.isdigit() or (num.startswith("-") and num[1:].isdigit())):
    print("Error en el ingreso de los datos")

else:
    num = int(num)

    # Caso 2: número negativo
    if num < 0:
        print("El numero debe ser mayor a 0")

    # Caso 3: no tiene 3 cifras
    elif num < 100 or num > 999:
        print("El numero de ser de 3 cifras")

    else:
        # Obtener centenas y unidades
        centena = num // 100
        unidad = num % 10

        # Verificar si es capicúa
        if centena == unidad:
            print("Es capicua")
        else:
            print("No es capicua")