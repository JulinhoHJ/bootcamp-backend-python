# Elabare un algoritmo que solicite 5 números
# e imprima la suma

suma = 0
for i in range(5):
  numero = int(input('Ingrese un numero: '))
  suma += numero
  
print('Suma total: ', suma)