# Crear un programa que solicite los
# catetos correspondientes
# para hallar la hipotenusa de un triángulo

cateto1 = float(input("Ingrese el cateto 1: "))
cateto2 = float(input("Ingrese el cateto 2: "))

hipotenusa = (cateto1**2 + cateto2**2) ** 0.5
print(f"La hipotenusa es: {hipotenusa}")