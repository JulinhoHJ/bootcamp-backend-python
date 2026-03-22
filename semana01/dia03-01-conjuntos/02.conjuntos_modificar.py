colorSet = {'red', 'green', 'blue', 'yellow', 'blue', 'red'}

print('colorSet', colorSet)

# Añadir un elemento a un conjunto
colorSet.add('purple')
print('colorSet', colorSet)

# No se puede Modificar un elemento de un conjunto
# colorSet[2] = 'black' --> TypeError

# Eliminar un elemento de un conjunto
colorSet.remove('blue')
# colorSet.remove('sky blue') # KeyError
print('colorSet', colorSet)

# Discard elimina un elemento si encuentra el elemento, de lo contrario no hace nada, ni da error
colorSet.discard('blue')
print('colorSet', colorSet)

# Eliminar todos los elementos de un conjunto
colorSet.clear()
print('colorSet', colorSet)

# Comprobar si un elemento esta en un conjunto
if 'blue' in colorSet:
    print('blue esta en el conjunto')