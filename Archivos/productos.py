#Ejercicio 2
# • Registrar productos en productos.txt
# • Guardar: Código;Descripción;Precio

def registro():
    archivo = open("productos.txt","a")
    codigo = input("Ingrese el codigo del producto: ")
    descripcion = input("Ingrese la descripcion del producto: ")
    precio = input("Ingrese el precio del producto: ")

    archivo.write(codigo + "|" + descripcion + "|" + precio + "\n")
    print("Datos ingresados correctamente")
    archivo.close()
    

def mostrar():
    print("LISTA PRODUCTOS")

    archivo = open("productos.txt","r")
    for linea in archivo:
        print(linea.strip())

    archivo.close()

def borrar():
    codigo_buscado = input("Ingrese el codigo del producto a eliminar: ")

    archivo = open("productos.txt", "r")
    lineas = archivo.readlines()
    archivo.close()

    archivo = open("productos.txt", "w")

    encontrado = False

    for linea in lineas:
        datos = linea.strip().split("|")

        if datos[0] != codigo_buscado:
            archivo.write(linea)
        else:
            encontrado = True

    archivo.close()

    if encontrado:
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")



def menu():
    print("\nMENU")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Borrar producto")
    print("4. Salir del sistema")

def iniciar():
    opcion = 0

    while opcion != 4:
        menu()
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            registro()
        elif opcion == 2:
            mostrar()
        elif opcion == 3:
            borrar()
        elif opcion == 4:
            print("Saliendo del sistema...")
        else:
            print("Opcion invalida")
        
iniciar()