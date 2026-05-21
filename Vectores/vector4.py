def cargar(vec1):
    for i in range(5):
        vec1[i] = int(input("Ingrese un numero: "))

def existe(vec1,n):
    
  n = int(input("Ingrese el numero a buscar: "))
  for i in range(5):
    if vec1[i] == n:
        print("Existe")
        print("Posicion:",i)
        break
  else:
      print("No existe")
        
    
        
        
def iniciar():
    vec1 = [0] * 5
    n = 0
    cargar(vec1)
    existe(vec1,n)
    

    

    


iniciar()