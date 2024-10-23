while True:
    num = input(f"\nIngrese el número de personas: ")
    if num.isdigit():
        n = int(num)
        break
    else:
        print("Por favor, ingrese solo números.")
edades = []
sexos = []
nombres = []

for i in range(n):
    nombre = input(f"\nIngrese el nombre de la persona {i+1}: ")
    nombres.append(nombre)
    while True:
        e = input(f"Ingrese la edad de {nombre}: ")
        if e.isdigit():
            edad = int(e)
            break
        else:
            print("Por favor, ingrese solo números.")
    edades.append(edad)
    sexo = input(f"Ingrese el sexo de {nombre} (M/F): ").upper()
    sexos.append(sexo)

promedioEdades = sum(edades) / len(edades)
print(f"\nEl promedio de las edades es: {promedioEdades}")

edadMujeres = sum(1 for edad, sexo in zip(edades, sexos) if 20 <= edad <= 30 and sexo == 'F')
totalMujeres = sexos.count('F')
porcentajeMujeres = (edadMujeres / totalMujeres) * 100 if totalMujeres > 0 else 0
print(f"El porcentaje de mujeres entre 20 y 30 años es: {porcentajeMujeres}%")

totalPersonas = len(sexos)
totalHombres = sexos.count('M')
totalMujeres = sexos.count('F')
porcentajeHombres = (totalHombres / totalPersonas) * 100
porcentajeMujeres = (totalMujeres / totalPersonas) * 100
print(f"El porcentaje de hombres es: {porcentajeHombres}%")
print(f"El porcentaje de mujeres es: {porcentajeMujeres}%")

indiceEdad = edades.index(max(edades))
edadMayor = edades[indiceEdad]
sexoEdadMayor = sexos[indiceEdad]
nombreEdadMayor = nombres[indiceEdad]

genero = "mujer" if sexoEdadMayor == 'F' else "hombre"
print(f"La persona con la edad más alta es {nombreEdadMayor}, de {edadMayor} años, y es {genero}.")
