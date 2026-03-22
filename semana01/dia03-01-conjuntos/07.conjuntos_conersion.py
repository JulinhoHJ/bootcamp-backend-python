colorList = ['red', 'green', 'blue', 'yellow', 'blue', 'red']

# Obtener los colores únicos de la lista
coloresUnicos = []
for color in colorList:
  print(color)
  if color not in coloresUnicos:
    coloresUnicos.append(color)

print('coloresUnicos: ', coloresUnicos)

# Convertir un conjunto a una lista
colorSet = set(colorList)
print('colorSet: ', colorSet)