#Registro de Asistencia de Alumnos
#Enunciado
#Una institución educativa desea desarrollar un sistema para registrar la asistencia de sus alumnos durante un curso.

#Se utilizará una matriz donde:
#- La primera columna almacenará el Nombre y Apellido del alumno.
#- Las siguientes 15 columnas representarán las 15 clases del curso.

#Para cada clase se podrá registrar:
#P = Presente
#A = Ausente
#F = Feriado
#X = Clase suspendida por festividad o evento especial

#Requerimientos:
#1. Registrar alumnos (máximo 20).
#2. Registrar asistencia de una clase.
#3. Registrar feriado o festividad para una clase completa.
#4. Mostrar planilla completa.
#5. Mostrar asistencia de un alumno.
#6. Mostrar porcentaje de asistencia de todos los alumnos.
#7. Mostrar el alumno con mayor asistencia.
#8. Salir.

from datetime import datetime

def registro_alumnos(lista):
    for i in range(20):
        repetido = True
        while repetido:
            nombre = input(f"Ingrese el nombre y apellido del alumno {i+1}: ")

            repetido = False

            for alumno in lista:
                if alumno[0] == nombre:
                    repetido = True
                    print("Ya existe un alumno con ese nombre registrado")
                    break
                    
        alumno = [nombre]

        for j in range(20):
            alumno.append("")

        lista.append(alumno)

    print("Alumnos registrados")
    return lista

def registro_asistencia(lista):
    try:
        clase = int(input("¿Que numero de clase es? (1-15): "))
        if clase < 1 or clase > 15:
            print("Numero de clase invalido")
            guardar_error("Se ingreso un numero de clase invalido (registro_asistencia)")
        for i in range(len(lista)):

            asistencia = input(f"{lista[i][0]} (P/A): ").upper()

            while asistencia not in ["P", "A"]:
                print("Asistencia inválida")
                guardar_error("Se ingreso una asistencia invalida (registro_asistencia)")
                asistencia = input(f"{lista[i][0]} (P/A): ").upper()

            lista[i][clase] = asistencia
        print("Asistencia registrada")
    except ValueError:
        print("ERROR, debe ingresar un valor numerico")
        guardar_error("No se ingreso un valor numerico (registro_asistencia)")


def registro_feriado(lista):
    try:
        clase = int(input("Ingrese el numero de clase: "))
        if clase < 1 or clase > 15:
            print("Numero de clase invalido")
            guardar_error("Se ingreso un numero de clase invalido (registro_feriado)")
        asistencia = input("Ingrese la asistencia especial,(X/F): ").upper()
        while asistencia not in ["X", "F"]:
            print("Opción inválida")
            guardar_error("Se ingreso una asistencia invalida (registro_feriado)")
            asistencia = input("Ingrese la asistencia especial (X/F): ").upper()
        if asistencia == "X":
            for i in range(len(lista)):
                lista[i][clase] = "X"
        
        elif asistencia == "F":
            for i in range(len(lista)):
                lista[i][clase] = "F"
        print("Asistencia registrada")
    except ValueError:
        print("ERROR, debe ingresar un valor numerico")
        guardar_error("No se ingreso un valor numerico (registro_feriado)")


def mostrar(lista):
    print("\nLISTA ASISTENCIA")
    for i in range(len(lista)):
        print(lista[i])

def mostrar_porcentaje(lista):
    try:
        for i in range(len(lista)):
            presentes = 0
            for j in range(1,len(lista[i])):
                if lista[i][j] == "P":
                    presentes += 1
            porcentaje = (presentes / (len(lista[i])-1)) * 100
            print(lista[i][0], ":", porcentaje, "%")
        return lista,porcentaje,presentes
    except ZeroDivisionError:
        print("No hubo presentes en la clase")

def asist_alumno(lista):
    encontrado = False
    buscar = input("Ingrese el nombre y apellido del alumno a buscar: ")
    for i in range(len(lista)):
        if buscar == lista[i][0]:
            print(f"Asistencia {buscar}:",lista[i])
            encontrado = True
    if encontrado == False:
        print("No existe alumno registrado con ese nombre")


def mayor_asistencia(lista):
    alumnos_mayor = []
    mayor = 0
    for i in range(len(lista)):
        asistencias = 0
        for j in range(1,len(lista[i])):
            if lista[i][j] == "P":
                asistencias += 1


        if asistencias > mayor:
            mayor = asistencias
            alumnos_mayor = lista[i][0]
        elif asistencias == mayor:
            alumnos_mayor.append(lista[i][0])

    print("Mayor cantidad de presentes:", mayor)
    print("Alumno/s con mayor asistencia:")
    for nombre in alumnos_mayor:
        print(nombre)


def guardar_error(mensaje):
    archivo = open("Asistencia_alumnos_trazas.txt", "a")
    archivo.write(mensaje + datetime.now().strftime(f"%d/%m/%Y %H:%M:%S") + "\n")
    archivo.close()

def menu():
    print("\nMENU")
    print("1. Cargar alumnos")
    print("2. Cargar asistencia por clase")
    print("3. Registrar feriado por clase")
    print("4. Mostrar planilla")
    print("5. Mostrar asistencia de un alumno")
    print("6. Porcentaje de asistencia general")
    print("7. Alumno con mayor asistencia")
    print("8. Salir del sistema")





def iniciar():
    lista = []
    opcion = 0
    while opcion != 8:
        menu()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            registro_alumnos(lista)
        elif opcion == 2:
            registro_asistencia(lista)
        elif opcion == 3:
            registro_feriado(lista)
        elif opcion == 4:
            mostrar(lista)
        elif opcion == 5:
            asist_alumno(lista)
        elif opcion == 6:
            mostrar_porcentaje(lista)
        elif opcion == 7:
            mayor_asistencia(lista)
        elif opcion == 8:
            print("Saliendo del sistema...")
        else:
            print("Opcion invalida")
iniciar()