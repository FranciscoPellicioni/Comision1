
entrada = input("Ingrese números separados por espacios: ")


numeros = list(map(int, entrada.split()))


unicos = set(numeros)


print("Cantidad de números únicos:", len(unicos))