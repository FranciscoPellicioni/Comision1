def cargar(total, vec1):

    for i in range(5):
        vec1[i] = int(input("Ingrese 5 numeros: "))
        total += vec1[i]

    return total


def calcular(total):
    promedio = total / 5

    print("Total:", total)
    print("Promedio:", promedio)


def iniciar():
    total = 0
    vec1 = [0] * 5

    total = cargar(total, vec1)

    calcular(total)


iniciar()