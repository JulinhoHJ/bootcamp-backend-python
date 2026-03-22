# Crear una aplicación que solicite al usuario una palabra,
# y muestre la cantidad de vocales diferentes
# Input: murciélago
# Output: 5
# Input: casa
# Output: 1

palabra = input('Ingrese una palabra: ').lower()
palabraSet = set(palabra)
vocalesSet = {'a', 'e', 'i', 'o', 'u'}

interseccion = vocalesSet & palabraSet
print('Cantidad de vocales: ', len(interseccion))