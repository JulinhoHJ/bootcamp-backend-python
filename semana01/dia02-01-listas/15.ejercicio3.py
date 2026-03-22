# Indicar el nombre de la fruta a eliminar
# Validar que la fruta exista
# Devolver el contenido de la cesta

cesta = ['uva', 'kiwi', 'coco', 'fresa', 'melón']
fruta = input('Ingrese la fruta a eliminar: ')

# Aqui agregas la logica
if fruta in cesta:
  # Mostramos la cesta sin la fruta a eliminar
  del cesta[cesta.index(fruta)]
  print(cesta)
else:
  print('La fruta no existe')