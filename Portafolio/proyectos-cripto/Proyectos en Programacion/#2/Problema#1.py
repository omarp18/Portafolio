saiyajin = {'Goku', 'Vegeta', 'Gohan', 'Goten', 'Trunks', 'Pan', 'Bra'}
terricolas = {'Yamcha', 'Trunks', 'Gohan', 'Bra', 'Maestro Rochi'}
villanos = {'Vegeta', 'Freezer', 'Cell', 'Majin Boo', 'Black Goku', 'Piccolo'}

union = saiyajin | terricolas | villanos
print("\nUnión de los conjuntos: ", union)

interseccion = saiyajin & villanos
print("Intersección de Saiyajin con Villanos: ", interseccion)

difAB = saiyajin - terricolas
print("Diferencia de Saiyajin y Terricolas: ", difAB)

difBA = terricolas - saiyajin
print("Diferencia de Terricolas y Saiyajin", difBA)

difSimetrica = saiyajin ^ terricolas ^ villanos
print("Diferencia simétrica de Terricolas, Saiyajin y Villanos", difSimetrica)