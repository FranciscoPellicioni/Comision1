anagramas = {}
palabras = ["caos", "cosa", "coser", "paloma", "taco", "cota", "saco"]
for p in palabras:
  ordenada = str(sorted(p))
  if ordenada not in anagramas:
    anagramas[ordenada] = [p]
  else:
    anagramas[ordenada].append(p)
print(list(anagramas.values()))