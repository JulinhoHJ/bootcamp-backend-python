""" 
El bucle while es un bucle que se ejecuta hasta que se cumple una condición.
No se puede determinar cuantas veces se ejecutará el bucle.
"""

condicion = True
cont = 0
while condicion:
  cont += 1
  numero = int(input('Ingrese un numero: '))
  if numero < 10:
    condicion = False

print('Repeticiones: ', cont)

