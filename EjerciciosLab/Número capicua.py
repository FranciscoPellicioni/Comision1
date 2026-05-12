try:
    numero = int(input (""))
    if numero < 1:
        print ("El numero debe ser mayor a 0")
    else:
        if numero < 100 or numero > 999:
          print ("El numero de ser de 3 cifras")
        else:
            centena = numero // 100 % 10
            decena = numero //10 % 10
            unidad = numero % 10
            if centena == unidad:
             print ("Es capicua")  
            else:
                print ("No es capicua")  
except ValueError:
   print ("Error en el ingreso de los datos")