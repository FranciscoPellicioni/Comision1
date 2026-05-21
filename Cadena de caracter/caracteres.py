#Ingresar una frase y mostrar cuantos caracteres tiene (sin contar los espacios)
#Ejemplo:
#Entrada: Hola Mundo
#Salida: 9


def contar(frase,contador):
    for i in range(len(frase)):
        if frase[i] != " ":
            contador += 1
    print(contador)




def iniciar():
    contador = 0
    frase = input("Ingrese una frase: ")
    contar(frase,contador)
    

iniciar()