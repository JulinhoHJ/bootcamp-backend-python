productDict = {'marca': 'Akita', 'nombre': 'pilas', 'precio': 4}
print(productDict)

# Actualizar valores
productDict['nombre'] = 'Pilas A3'
print(productDict)

productDict.update({'precio': 3.7})
print(productDict)

# Añadir un nuevo elemento
productDict['categoria'] = 'herramientas'
productDict.update({'peso': '40gr'})
print(productDict)

# Eliminar un elemento
productDict.pop('peso')
print(productDict)

# Eliminar todos los elementos
productDict.clear()
print(productDict)