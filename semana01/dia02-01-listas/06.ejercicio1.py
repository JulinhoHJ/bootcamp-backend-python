# Desarrollar un programa para una discoteca
# que pregunte por la edad del cliente
# Verificar si es mayor de edad
# Validar si el cliente tiene suficiente dinero
# para pagar la entrada

entrada = 70

edad = int(input('Ingrese su edad: '))

if edad < 0:
  print('La edad no puede ser negativo')
elif edad >= 18:
  dinero = float(input('Ingrese su dinero para ingresar: '))
  if dinero >= entrada:
    print('Ingresa a la discoteca')
  else:
    print('No tienes suficiente dinero')
else:
  print('Debes ser mayor de edad para ingresar')