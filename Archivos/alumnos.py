#Ejercicio 1
# • Registrar alumnos en alumnos.txt
# • Guardar: Legajo;Nombre;Carrera

def registrar():
    archivo = open("alumnos.txt","a")
    print("Ingrese los datos del alumno")
    legajo = input("Ingrese el legajo: ")
    nombre = input("Ingrese el nombre: ")
    carrera = input("Ingrese la carrera: ")
    archivo.write(legajo+ "|" +nombre+ "|" +carrera+ "\n")
    print("Datos ingresados correctamente")
    archivo.close()
    return archivo

def mostrar():
    print("LISTA ALUMNOS")
    archivo = open("alumnos.txt","r")
    linea = archivo.read()
    print(linea)
    archivo.close()


def borrar():
    legajo_buscado = input("Ingrese el legajo del alumno a dar de baja: ")
    archivo = open("alumnos.txt","r")
    lineas = archivo.readlines()
    archivo.close()

    archivo = open("alumnos.txt","w")
    encontrado = False  

    for linea in lineas:
        datos = linea.strip().split("|")

        if datos[0] != legajo_buscado:
            archivo.write(linea)
        else:
            encontrado = True
    archivo.close()

    if encontrado:
        print("Alumno dado de baja.")
    else:
        print("Alumno no encontrado.")






def menu():
    print("\nMENU")
    print("1. Registrar alumno")
    print("2. Mostrar alumnos")
    print("3. Dar de baja a un alumno")
    print("4. Salir del sistema")

def iniciar():
    opcion = 0
    while opcion != 4:
        menu()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            registrar()
        elif opcion == 2:
            mostrar()
        elif opcion == 3:
            borrar()
        elif opcion == 4:
            print("saliendo del sistema...")

        else:
            print("Opcion invalida")
        
iniciar()

