#Una empresa paga una bonificación según antigüedad y sueldo:
# Si tiene más de 10 años de antigüedad, bono del 10%.
# Si no, pero tiene más de 5 años, bono del 7%.
# Si no, bono del 5%.
# Además, si el sueldo es menor a $500000, se agrega un extra del 3%. Mostrar sueldo final.

sueldo = float(input("Ingrese su sueldo:"))
antiguedad = int(input("Ingrese su antiguedad:"))

if antiguedad > 10:
    bono = sueldo * 0.10
elif 10 >= antiguedad > 5:
    bono = sueldo * 0.07
else:
 bono = sueldo * 0.05

extra = 0
if sueldo < 500000:
    extra = sueldo * 0.03
     
print("El sueldo final es:", sueldo + bono + extra)
