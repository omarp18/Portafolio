# Conjuntos
saiyajin = {'Goku', 'Vegeta', 'Gohan', 'Goten', 'Trunks', 'Pan', 'Bra'}
terricolas = {'Yamcha', 'Trunks', 'Gohan', 'Bra', 'Maestro Rochi'}
villanos = {'Vegeta', 'Freezer', 'Cell', 'Majin Boo', 'Black Goku', 'Piccolo'}

# Unión
union = saiyajin | terricolas | villanos
print("\nUnión de los conjuntos: ", union)

# Intersección Saiyajin con Villanos
interseccion = saiyajin & villanos
print("Intersección de Saiyajin con Villanos: ", interseccion)

# Diferencia Saiyajin y Terricolas
difAB = saiyajin - terricolas
print("Diferencia de Saiyajin y Terricolas: ", difAB)

# Diferencia Terricolas y Saiyajin
difBA = terricolas - saiyajin
print("Diferencia de Terricolas y Saiyajin", difBA)

# Diferencia simétrica de Terricolas, Saiyajin con Villanos
difSimetrica = saiyajin ^ terricolas ^ villanos
print("Diferencia simétrica de Terricolas, Saiyajin y Villanos", difSimetrica)