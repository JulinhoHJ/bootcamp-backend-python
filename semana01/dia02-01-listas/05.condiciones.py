# Solicitamos el valor de tu sueldo
# Indicamos si tienes un sueldo superior
# El sueldo no puede ser negativo

basico = 1130
sueldo = int(input('Sueldo: '))

if sueldo < 0:
    print('El sueldo no puede ser negativo')
elif sueldo > basico:
    print('Sueldo superior al básico')
elif sueldo < basico:
    print('Sueldo inferior al básico')
else:
    print('Sueldo igual al básico')