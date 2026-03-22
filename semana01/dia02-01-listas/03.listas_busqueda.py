cesta = ['uva', 'piña', 'kiwi', 'coco']

posicion = cesta.index('kiwi')
print(posicion)

# index(), devuelve la posición del elemento
# si el elemento no existe, devuelve error
# posicion = cesta.index('manzana') -> ValueError
posicion = cesta.index('uva')
print(posicion)

existe_fruta1 = "fresa" in cesta
existe_fruta2 = "coco" in cesta

print('Consulta fresa: ', existe_fruta1)
print('Consulta coco: ', existe_fruta2)