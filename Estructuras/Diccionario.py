#Crear un programa que permita almacenar palabras en español y su traducción al inglés.
#El programa debe permitir ingresar 3 pares de palabras, y luego pedir una palabra en español para mostrar su traducción.
#Si la palabra no está registrada, debe mostrar el mensaje "Palabra no encontrada"

#Ejemplo:

#Entrada:
#sol sun
#luna moon
#estrella star
#cielo
#Salida:
#Palabra no encontrada
def ingreso(diccionario):
    for i in range(3):
        español = input("Ingrese una palabra en español: ")
        if español in diccionario:
            print("Error, esa palabra ya existe en el diccionario")
            return
        ingles = input("Ingrese la traduccion en ingles: ")
        diccionario[español] = ingles
    return diccionario

def mostrar(diccionario):
    print(diccionario)

def traducir(diccionario):
    
    palabra  = input("Ingrese una palabra en español a traducir: ")
    if palabra in diccionario:
        print(diccionario[palabra])

    else:
        print("Palabra no encontrada")
        
    
def iniciar():
    diccionario = {}
    ingreso(diccionario)
    mostrar(diccionario)
    traducir(diccionario)

iniciar()