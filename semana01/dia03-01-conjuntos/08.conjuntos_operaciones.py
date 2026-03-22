deportesSet1 = {'futbol', 'tenis', 'voley', 'natación'}
deportesSet2 = {'futbol', 'voley', 'baloncesto', 'judo'}

print('----Intersección---')
print('& :', deportesSet1 & deportesSet2)
print('intersection(): ', deportesSet1.intersection(deportesSet2))

print('----Unión---')
print('| :', deportesSet1 | deportesSet2)
print('union(): ', deportesSet1.union(deportesSet2))

print('----Diferencia---')
print('- : ', deportesSet1 - deportesSet2)
print('difference(): ', deportesSet1.difference(deportesSet2))

print('----Symetria: Suma de diferencias---')
print('^ : ', deportesSet1 ^ deportesSet2)
print('symmetric_difference(): ', deportesSet1.symmetric_difference(deportesSet2))