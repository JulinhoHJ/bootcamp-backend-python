# Una tupla es una estructura de datos
# que puede almacenar una colección de elementos
# Es inmutable, no se puede modificar
# Los elementos tienen un orden definido, y no cambia
# Permite duplicados

tupla = ('lun', 'mar', 'mie', 'jue', 'vie')

# Mostrar el contenido de la tupla
print(tupla)

# Obtener el total de elementos de la tupla
total = len(tupla)
print(total)

# Acceder a un elemento
#print(tupla[10]) # -> IndexError
print(tupla[2]) # -> mar

# Es inmutable, no se puede modificar, añadir o eliminar elementos
#tupla[1] = 'sab' -> TypeError
#tupla.append('sab') -> AttributeError 
#del(tupla[2]) -> TypeError