#Ejercicio 4: Gestión de Productos de un Supermercado
#Ingresar productos (Código, Descripción, Marca, Precio, Stock). 
#Mostrar todos los productos registrados. 
#Modificar el precio de un producto. 
#Modificar el stock de un producto. 
#Mostrar los productos con stock menor a 10 unidades. 
#Mostrar el producto con mayor stock. 
#ostrar la cantidad total de unidades almacenadas. 

def ingreso(productos):
    producto = []
    codigo = int(input("Ingrese el codigo del producto: "))
    for i in range(len(productos)):
        if productos[i][0] == codigo:
            print("ERROR, producto ya registrado")
            return
    descripcion = input("Ingrese la descripcion del producto: ")
    marca = input("Ingrese la marca del producto: ")
    precio = float(input("Ingrese el precio del prodcuto: "))
    stock = int(input("Ingrese el stock del producto: "))   
    producto = [codigo,descripcion,marca,precio,stock]
    productos.append(producto)
    print("Producto registrado con exito")
    return productos

def mostrar(productos):
    print("LISTA PRODUCTOS")
    for i in range(len(productos)):
        print(productos[i])

def modificar(productos):
    codigo_buscar = int(input("Ingrese el codigo del prodcuto a buscar: "))

    for i in range(len(productos)):
        if productos[i][0] == codigo_buscar:
            dato = input("Seleccione el dato a modificar\nPrecio\nStock\n - ")
            if dato == "precio":
                productos[i][3] = float(input("Ingrese el precio nuevo del producto: "))
                print("Dato modificado con exito")
            
            elif dato == "stock":
                productos[i][4] = int(input("Ingrese el nuevo stock del producto: "))
                print("Dato modificado con exito")

            else:
                print("El dato ingresado es incorrecto")
            return
    print("No existe un producto con ese codigo")


def stock_menor(productos):
    print("PRODUCTOS CON STOCK MENOR A 10")
    for i in range(len(productos)):
        if productos[i][4] < 10:
            print(productos[i])

def stock_mayor(productos):
    mayor = productos[0]
    for i in range(1,len(productos)):
        if productos[i][4] > mayor[4]:
            mayor = productos[i]
    print("El producto con el stock mayor es",mayor)


def unidades_total(productos):
    total = 0
    for i in range(len(productos)):
        total += productos[i][4]
    print("La cantidad total de unidades almacenadas es",total)


def menu():
    print("\nMENÚ")
    print("1. Registrar producto")
    print("2. Mostrar productos")
    print("3. Modificar datos de un producto")
    print("4. Prodcutos con menor stock")
    print("5. Stock mayor")
    print("6. Stock total")
    print("7. Salir del sistema")

def iniciar():
        productos = []
        opcion = 0
        while opcion != 7:
            menu()
            opcion = int(input("Ingrese una opción: "))
            if opcion == 1:
                ingreso(productos)
            elif opcion == 2:
                mostrar(productos)
            elif opcion == 3:
                modificar(productos)
            elif opcion == 4:
                stock_menor(productos)
            elif opcion == 5:
                stock_mayor(productos)
            elif opcion == 6:
                unidades_total(productos)
            elif opcion == 7:
                print("Saliendo del sistema...")
            else:
                print("Opcion invalida")

iniciar()