#En una empresa de servicios en línea, se necesita un programa que verifique si el correo electrónico ingresado por el usuarios es válido. 
# Un correo electrónico válido debe contener al menos un carácter antes del símbolo '@', un '@', 
# y al menos un punto ('.') que separa el dominio de nivel superior (TLD, por sus siglas en inglés) 
# del dominio de nivel inferior (SLD, por sus siglas en inglés).
# Además, se permite que haya un subdominio opcional, que también se separa por un punto.

def validarCorreo(correo):
    arroba = 0
    posicionArroba = -1
    puntoDespues = False

    for i in range(len(correo)):
        if correo[i] == "@":
            arroba += 1
            posicionArroba = i

    if arroba == 1 and posicionArroba > 0:
        for i in range(posicionArroba + 1, len(correo)):
            if correo[i] == ".":
                puntoDespues = True

    if arroba == 1 and posicionArroba > 0 and puntoDespues:
        print("Correo valido")
    else:
        print("Correo invalido")


def iniciar():
    correo = input("Ingrese un correo: ")
    validarCorreo(correo)


iniciar()