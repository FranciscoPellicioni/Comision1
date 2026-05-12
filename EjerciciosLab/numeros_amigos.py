num1 = int(input("ingrese u numero:"))
num2 = int(input("ingrese otro numero:"))
suma_divisores_num1 = 0
suma_divisores_num2 = 0
for i in range(1,num1):
    if num1 % i == 0:
     suma_divisores_num1 += i

for i in range(1,num2):
    if num2 % i == 0:
     suma_divisores_num2 += i

if suma_divisores_num1 == num2 and suma_divisores_num2 == num1:
 print("los numeros son amigos")

else:
  print("los numeros no son amigos")