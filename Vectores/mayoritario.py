N = int(input("Ingrese el tamaño del arreglo: "))

vec = [0] * N

for i in range(N):
    vec[i] = int(input("Ingrese un numero: "))

mayoritario = False

for i in range(N):

    contador = 0

    for j in range(N):

        if vec[i] == vec[j]:
            contador += 1

    if contador > N // 2:
        print(vec[i])
        mayoritario = True
        break

if mayoritario == False:
    print("No hay mayoritario")