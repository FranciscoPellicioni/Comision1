def cargar(vec1):

    for i in range(5):
        vec1[i] = int(input("Ingrese 5 numeros: "))

def mayorOmenor(vec1,mayor,menor):
    for i in range(5):
     if vec1[i] > mayor:
         mayor = vec1[i]
     elif vec1[i] < menor:
         menor = vec1[i]
    print("El mayor es:",mayor)
    print("El menor es:",menor)     
def iniciar():
    vec1 = [0] * 5
    cargar(vec1)
    mayor = vec1[0]
    menor = vec1[0]
    mayorOmenor(vec1,mayor,menor)

    

    


iniciar()