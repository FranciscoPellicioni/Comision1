# Lo primero que notó fue que las consonantes no interfieren en cómo la risa digital influye en el sentimiento de transmisión. 
# La segunda cosa que notó fue que las risas digitales más divertidas son aquellas en las que las secuencias de vocales son las mismas cuando se leen en el orden natural (de izquierda a derecha) o en orden inverso (de derecha a izquierda), 
# ignorando las consonantes. Por ejemplo, "hahaha" y "huaauhahhuahau" están entre las risas más divertidas, mientras que "riajkjdhhihhjak" y "huehuehue" no están entre las más divertidas.
#Claudia está muy ocupada con el análisis estadístico de la risa digital y te pide ayuda para escribir un programa que determina si una risa digital es la más divertida o no.
#Entrada
#La entrada comprende una línea que contiene una secuencia de hasta 50 caracteres, formada sólo por letras pequeñas sin acento. Las vocales son las letras 'a', 'e', ​​'i', 'o', 'u'. La secuencia contiene al menos una vocal.
#Salida
#El programa debe producir una línea que contenga un carácter, "S" si la risa es de las divertidas, o "N" si no lo es. "hahaha" y "huaauhahhuahau"



def verificarvocales(frase,vocales,solo_vocales):
    for i in range(len(frase)):
        if frase[i] in vocales:
            solo_vocales += frase[i]
        
    return solo_vocales


def risa(frase,solo_vocales,vocales):
    
    solo_vocales = verificarvocales(frase,vocales,solo_vocales)

    if solo_vocales == solo_vocales[::-1]:
        print("S")
    else:
        print("N")


            

def iniciar():
    solo_vocales = ""
    vocales = ["a","e","i","o","u"]
    frase = input("Ingrese una risa que tenga entre 2 y 50 caracteres: ")
    verificarvocales(frase,vocales,solo_vocales)
    risa(frase,solo_vocales,vocales)
    
    

iniciar()