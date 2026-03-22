"""
range(inicio, fin, paso)
genera una secuencia de enteros desde inicio hasta fin, paso a paso
Inicio: el primer elemento de la secuencia, es 0 si no se especifica
"""
print(range(10))

print('---- Iteración con range ----')
for i in range(10):
    print(i)

print('---- Iteración de bloque ----')
for i in range(3, 8):
    print(i)

print('---- Iteración de bloque con paso----')
for i in range(3, 11, 2):
    print(i)