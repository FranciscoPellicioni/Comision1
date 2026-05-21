#Ingresar una frase y mostrar la palabra mas larga. En caso de que existan dos palabras o mas que tengan el mismo largo,
# que la más larga, sin importar si son repetidas, mostrarlas en el orden en el que aparecen en el texto.
#Ejemplo 1: Entrada: Hola Mundo Salida: Mundo
# Ejemplo 2: Entrada: Hola todo bien por aca amor Salida:Hola todo bien amor


        

def maslarga(frase,palabra,mayor,resultado):
   
    for i in range(len(frase)): 
        if frase[i] != " ":
            palabra += frase[i]

        if frase[i] == " " or i == len(frase)-1:
            
            if len(palabra) > mayor:
                mayor = len(palabra)
                resultado = palabra
            
            elif len(palabra) == mayor:
                resultado += " " + palabra
            palabra = ""

    print("La/s palabra/s mas larga/s es/son:",resultado)
            


def iniciar():
    frase = input("Ingrese una frase: ")
    palabra = ""
    mayor = 0
    resultado = ""
    maslarga(frase,palabra,mayor,resultado)
    
    
    

iniciar()