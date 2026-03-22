mensaje = "Mi nuevo mensaje"
print(mensaje)
print("Primer caracter: ", mensaje[0])
print("Primer espacio en blanco: ", mensaje[2])
total = len(mensaje) # Obtenemos el total de caracteres
print("Total de caracteres: ", total)
print("Último caracter: ", mensaje[total-1])
print("Penúltimo caracter: ", mensaje[-2])

print("-------------------------")
mensaje = "Python Es CHevEre"
print(mensaje)
print(mensaje.upper()) # Convierte a mayúsculas
print(mensaje.lower()) # Convierte a minúsculas
# convierte mayus a minus y minus a mayus
print(mensaje.swapcase())
print(mensaje.capitalize()) # Convierte la primera letra a mayúscula
