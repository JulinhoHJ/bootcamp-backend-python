# Tenemos una lista de invitados para una fiesta
# Para ingresar cada invitado brindirá su nombre
# y el programa deberá indicar si esta o no

invitados = ['Juan', 'Pedro', 'Marcos', 'Juana']
nombre = input('Ingrese su nombre: ')
existe = nombre in invitados
print('Permitir ingreso? ', existe)