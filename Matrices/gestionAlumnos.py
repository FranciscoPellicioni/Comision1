#Ejercicio 1: Gestión de Alumnos de una Academia
#Ingresar alumnos (Legajo, Nombre, Apellido, DNI, Curso, Estado). 
#Mostrar todos los alumnos registrados. 
#Modificar el curso de un alumno ingresando su Legajo. 
#Modificar el DNI de un alumno. 
#Dar de baja un alumno cambiando su Estado a "B" (Baja). 
#Mostrar los alumnos dados de baja. 
#Mostrar la cantidad de alumnos activos. 
def ingreso(alumnos):
    alumno = []
    legajo = int(input("Ingrese el legajo del alumno: "))
    for i in range(len(alumnos)):
        if alumnos[i][0] == legajo:
            print("ERROR, este alumno ya esta registrado")
            return
    nombre = input("ingrese el nombre y apellido del alumno: ")
    dni = int(input("Ingrese el DNI: "))
    curso =input("Ingrese el curso: ")
    estado = "A"
    alumno = [legajo,nombre,dni,curso,estado]

    alumnos.append(alumno)
    print("Alumno registrado correctamente")
    return alumnos
    
def mostrar(alumnos):
    print("LISTA ALUMNOS")
    for i in range(len(alumnos)):
        print(alumnos[i])
        
def modificar(alumnos):
    legajo_buscar = int(input("Ingrese el legajo del alumno a modificar: "))

    for i in range(len(alumnos)):
        if alumnos[i][0] == legajo_buscar:

            dato = input(f"Seleccione el dato a modificar\nCurso\nDNI\n-  ").lower()

            if dato == "curso":
                alumnos[i][3] = input("Ingrese el curso nuevo: ")

            elif dato == "dni":
                alumnos[i][2] = int(input("Ingrese el dni nuevo: "))
 
            else:
                print("El dato seleccionado es incorrecto")
                return

            
            print("Datos modificados correctamente")
            return

    print("No existe un alumno con ese legajo")
    
def darbaja(alumnos):
    baja = int(input("Ingrese el legajo del alumno a dar de baja: "))

    for i in range(len(alumnos)):
        if alumnos[i][0] == baja:
            alumnos[i][4] = "B"
            
            print("Alumno dado de baja correctamente")
            return

    print("No existe un alumno asociado a este legajo")

def mostrarbaja(alumnos):
    print("ALUMNOS DADOS DE BAJA")
    existe = False


    for i in range(len(alumnos)):
        if alumnos[i][4] == "B":
            print(alumnos[i])
            existe = True
        
    if existe == False:
        print("No hay alumnos dados de baja")

def mostrar_activos(alumnos):
    activos = 0
    for i in range(len(alumnos)):
        if alumnos[i][4] == "A":
            activos += 1
           
    
    print("La cantidad de alumnos activos es:",activos)   
    
def menu():
    print("\nMENÚ")
    print("1. Registrar alumno")
    print("2. Mostrar alumnos")
    print("3. Modificar datos de un alumno")
    print("4. Dar de baja")
    print("5. Mostrar bajas")
    print("6. Mostrar activos")
    print("7. Salir del sistema")
   
    
       
def iniciar():
    alumnos = []
    opcion = 0
    while opcion != 7:
        menu()
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            ingreso(alumnos)
        elif opcion == 2:
            mostrar(alumnos)
        elif opcion == 3:
            modificar(alumnos)
        elif opcion == 4:
            darbaja(alumnos)
        elif opcion == 5:
            mostrarbaja(alumnos)
        elif opcion == 6:
            mostrar_activos(alumnos)
        elif opcion == 7:
            print("Saliendo del sistema...")
        else:
            print("Opcion invalida")

iniciar()