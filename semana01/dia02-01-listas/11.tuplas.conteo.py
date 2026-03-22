notas = (9, 11, 16, 18, 17, 13, 10, 15, 16, 9, 13, 9, 13)

# Hallamos cuantas veces aparece el valor 13
print('Cuantas veces aparece el valor 13: ', notas.count(13))

# Hallar la maxima nota
print('La nota máxima es: ', max(notas))

# Hallar la nota mínima
print('La nota mínima es: ', min(notas))

# Hallar cuantas veces se repite la nota minima
print('Cuantas veces aparece la nota mínima: ', notas.count(min(notas)))

# Sumar las notas
total = sum(notas)
print('La nota total es: ', total)