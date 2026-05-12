num = int(input("Ingrese el numero ISBN (10 digitos)\n"))

div = 1
s = 0
verif = 0

for i in range(1, 11, 1):

    d = num // div % 10

    if i == 1:
        verif = d
        div = div * 10

    else:
        s = s + ((11 - i) * d)
        div = div * 10

verificador = s % 11

if num >= 10000000000:
    print("Error -> Número no válido.")

if num <= 9999999999 and verificador == verif:
    print("El calculo de S, del numero ISBN es ", s, ".")
    print("El verificador ingresado:", verif,
          ", coincide con el verificador calculado", verificador, ".")
    print("El numero ingresado es correcto.")

if num <= 9999999999 and verificador != verif:
    print("El calculo de S, del numero ISBN es ", s, ".")
    print("El verificador ingresado:", verif,
          ", no coincide con el verificador calculado", verificador, ".")
    print("El numero ingresado es incorrecto.")