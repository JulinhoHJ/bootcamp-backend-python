# Ingresar el monto de ganancias por año
# Si el monto no supera los 10000, se paga 5% de impuesto
# Si el monto va entre 10001 y 20000, se paga 15% de impuesto
# Si el monto va entre 20001 y 35000, se paga 20% de impuesto
# Si el monto supera los 35000, se paga el 30% de impuesto
# indicar el porcentaje de impuesto a pagar

monto = int(input('Ingrese el monto de ganancias por año: '))

if monto < 0:
  print('El monto no puede ser negativo')
elif monto <= 10000:
  print('Paga 5% de impuesto')
elif monto > 10000 and monto <= 20000:
  print('Paga 15% de impuesto')
elif monto > 20000 and monto <= 35000:
  print('Paga 20% de impuesto')
else:
  print('Paga 30% de impuesto')