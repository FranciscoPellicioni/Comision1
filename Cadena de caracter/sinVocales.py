#ingresar una cadena y mostrarla sin vocales.

#Ejemplo:
#Entrada:
#Si lo puedes programar, lo puedes imaginar
#Salida:
#S l pds prgrmr, l pds mgnr

def sinVocales(frase,vocales,frase2):
    for i in range(len(frase)):
        if frase[i].upper() not in vocales:
            frase2 += (frase[i])
    print(frase2)







def iniciar():
    frase = input("Ingrese una frase: ")
    frase2 = ""
    vocales = ["A","E","I","O","U"]
    sinVocales(frase,vocales,frase2)
   
iniciar()



