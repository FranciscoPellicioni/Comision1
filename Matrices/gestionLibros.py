#Ejercicio 5: Gestión de Libros de una Biblioteca
#Ingresar libros (Código, Título, Autor, Editorial, Año). 
#Mostrar todos los libros registrados. 
#Modificar la editorial de un libro. 
#Modificar el año de publicación de un libro. 
#ostrar los libros publicados después de 2020. 
#Mostrar la cantidad de libros por editorial. 
#Buscar un libro por título y mostrar todos sus datos.

def ingreso(libros):
    libro = []
    codigo = int(input("Ingrese el codigo del libro: "))
    for i in range(len(libros)):
        if libros[i][0] == codigo:
            print("ERROR, este libro ya esta registrado")
            return
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")
    editorial = input("Ingrese la editorial del libro: ")
    año = int(input("Ingrese el año de la publicacion del libro: "))
    libro = [codigo,titulo,autor,editorial,año]
    libros.append(libro)
    print("Libro registrado con exito")
    return libros

def mostrar(libros):
    print("LISTA LIBROS")
    for i in range(len(libros)):
        print(libros[i])


def modificar(libros):
    codigo_buscar = int(input("Ingrese el codigo del libro a buscar: "))
    for i in range(len(libros)):
        if libros[i][0] == codigo_buscar:
            dato = input("Seleccione el dato a modificar\nEditorial\nAño publicacion\n- ")
            if dato == "editorial":
                libros[i][3] = input("Ingrese la editorial nueva: ")
                print("Dato modificado con exito")
            
            elif dato == "año publicacion":
                libros[i][4] = int(input("Ingrese el año nuevo: "))
                print("Dato modificado con exito")

            else:
                print("El dato seleccionado es incorrecto")
            return
    print("No existe un libro registrado con ese codigo")


def libros_2020(libros):
    print("LIBROS PUBLICADOS DESPUES DEL 2020")
    for i in range(len(libros)):
        if libros[i][4] > 2020:
            print(libros[i])
        
def editoriales(libros):
    total = 0
    editorial_buscar = input("Ingrese una editorial: ")
    for i in range(len(libros)):
        if libros[i][3] == editorial_buscar:
            total += 1

    print("Existe/n",total,"libro/s con la editorial",editorial_buscar)

def buscar_titulo(libros):
    titulo_buscar = input("Ingrese el titulo del libro a buscar: ")
    existe = False
    for i in range(len(libros)):
        if libros[i][1] == titulo_buscar:
            print(libros[i])
            existe = True
    if existe == False:
        print("No existe ningun libro con ese titulo")

def menu():
    print("\nMENÚ")
    print("1. Registrar libro")
    print("2. Mostrar libros")
    print("3. Modificar datos de un libro")
    print("4. Libros publicados despues del 2020")
    print("5. Cantidad de libros por editorial")
    print("6. Buscar datos de un libro")
    print("7. Salir del sistema")

def iniciar():
        libros = []
        opcion = 0
        while opcion != 7:
            menu()
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1:
                ingreso(libros)
            elif opcion == 2:
                mostrar(libros)
            elif opcion == 3:
                modificar(libros)
            elif opcion == 4:
                libros_2020(libros)
            elif opcion == 5:
                editoriales(libros)
            elif opcion == 6:
                buscar_titulo(libros)
            elif opcion == 7:
                print("Saliendo del sistema...")
            else:
                print("Opcion invalida")

iniciar()



