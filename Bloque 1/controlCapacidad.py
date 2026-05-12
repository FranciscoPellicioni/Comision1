#Control de Capacidad: Una zona de espera tiene capacidad para 15 personas. 
# Pedir la cantidad de personas presentes. 
# Si supera el límite, indicar cuántas personas deben retirarse.
personas_presentes =int(input("Ingrese la cantidad de personas presentes: "))

if personas_presentes > 15:
    retiro = personas_presentes - 15
    print("La cantidad de personas que deben retirarse es:", retiro)