edad = int(input("Ingrese su edad: "))
if edad < 18:
    print("Es menor de edad")
elif 18 <= edad < 23:
    print("Es estudiante de la UTN")
elif 23 <= edad < 60:
    print("Es profesor")
else:
    print("Es jubilado")
     