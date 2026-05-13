#Ejercicio 7: Estación meteorológica
# Cargar la cantidad de lluvia caída durante 30 días. Mostrar el día con mayor lluvia, el promedio
# mensual y cuántos días no llovió.
diaMayor = 0
sinLluvia = 0
cantLluvia = 0
for i in range(3):
    lluvia = int(input("Ingrese la cantidad de milimetros: "))

    if lluvia > 0:
        cantLluvia = cantLluvia + lluvia
        if lluvia > diaMayor:
            diaMayor = lluvia

    else:
        sinLluvia += 1
promedio = cantLluvia/3

print(f"El dia con mayor lluvia es:{diaMayor}\nEl promedio mensual es: {promedio}\nNo llovio en: {sinLluvia}")
