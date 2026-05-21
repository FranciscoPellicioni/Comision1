#Ingresar una frase y mostrar cuantas vocales tiene
# Ejemplo:
# Entrada: Hola Mundo 
# Salida: 4
     
def contar(frase,vocales,contador):
    for i in range(len(frase)):
        if frase[i].upper() in vocales:
            contador += 1
    print(contador)


def iniciar():
    contador = 0
    frase = input("Ingrese una frase: ")
    vocales = ["A","E","I","O","U"]
    contar(frase,vocales,contador)

iniciar()