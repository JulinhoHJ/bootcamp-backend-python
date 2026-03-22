# Solicitar 2 frases, y mostrar las palabras que no se repiten.
# Input1: python es chevere
# Input2: python es bacán
# Output: chevere, bacán
# Input1: La casa de mi primo es muy bonita
# Input2: La piscina es muy bonita
# Output: casa,de,mi,primo,piscina

frase1 = input('Ingrese la primera frase: ').lower()
frase2 = input('Ingrese la segunda frase: ').lower()

frase1Set = set(frase1.split(' '))
frase2Set = set(frase2.split(' '))
print(frase1Set ^ frase2Set)