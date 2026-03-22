# una lista es una estructura de datos
# que puede almacenar una colección de elementos

cesta = ['uva', 'piña', 'kiwi', 'coco']

# Mostrar el contenido de la lista
print(cesta)

# Obtener el total de elementos de la lista
total = len(cesta)
print(total)

# Acceder a un elemento
print(cesta[2]) # -> kiwi
# print(cesta[10]) # -> IndexError

# Modificar un elemento
cesta[1] = 'melón'
print(cesta)

# Añadir un nuevo elemento
cesta.append('manzana')
cesta.append('sandia')
print(cesta)

# Eliminar un elemento
del cesta[3]
print(cesta)