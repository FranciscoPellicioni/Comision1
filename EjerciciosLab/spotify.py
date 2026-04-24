total = 0
total_canciones = 0
max_t = 0
max_cancion = ""

cancion = input("ingrese una cancion:")
tiempo = int(input("ingrese los minutos escuchados:"))

while tiempo > 0 :
    total += tiempo
    total_canciones += 1


    if tiempo > max_t :
     max_t = tiempo
     max_cancion = cancion

    cancion = input("ingrese una cancion:")
    tiempo = int(input("ingrese los minutos escuchados:"))

print("La canción que más escuchaste fué:", max_cancion)
print("Escuchaste esa canción por:", max_t, "minutos")
print("El total de minutos escuchados en la temporada es de:", total)
print("Esta temporada escuchaste:", total_canciones, "canciones")
 
