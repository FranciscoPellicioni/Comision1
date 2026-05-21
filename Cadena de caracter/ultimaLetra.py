#Ingresar una cadena y mostrar cuántas veces aparece la última letra.
#Ejemplo:
#Entrada: Hola Mundo
#Salida: 2

def ultimaLetra(frase):
    return frase[-1]

def contar(frase,ultima,contador):
    for i in range(len(frase)):
        if frase[i] == ultima:
            contador += 1
    
    print("La ultima letra se repitio",contador,"veces")




def iniciar():
    contador = 0
    frase = input("Ingrese una frase: ")
    ultima = ultimaLetra(frase)
    contar(frase,ultima,contador)
   
   
iniciar()