#Ejercicio 6: Cálculo de sueldo semanal
# Ingresar las horas trabajadas de 12 empleados. Si supera las 48 horas semanales, 
# las horas excedentes se pagan dobles. Mostrar sueldo individual y total abonado por la empresa.
precio = 6000
totalAbonado = 0
for i in range(12):
    horas = int(input(f"ingrese las horas del empleado {i+1}:"))
    
    if horas <= 48:
      sueldo = horas * precio
      totalAbonado = totalAbonado + sueldo
    else:
        horasExtra = horas - 48
        sueldo = (48 * 6000) + (horasExtra * 12000)
        totalAbonado = totalAbonado + sueldo
    print("El sueldo del empleado", {i+1}, "es:",sueldo)    


print("El total abonado por la empresa es:",totalAbonado)