# Creamos un diccionario vacío para almacenar los sinónimos
sinonimos = {}

# Pedimos al usuario que ingrese palabras y sus sinónimos
while True:
    palabra = input("Ingresa una palabra (o 'F' para terminar): ").lower()
    if palabra == 'f':
        break
    else:
        sinonimos[palabra] = []
        while True:
            sinonimo = input("Ingresa un sinónimo de la palabra anterior (o 'F' para terminar): ").lower()
            if sinonimo == 'f':
                break
            sinonimos[palabra].append(sinonimo)

# Pedimos al usuario que ingrese una palabra para buscar sus sinónimos
palabraIngresada = input("Ingresa una palabra para encontrar sus sinónimos: ")

# Buscamos los sinónimos y los mostramos
resultado = sinonimos.get(palabraIngresada.lower(), ["No se encontraron sinónimos para esta palabra."])
print("Sinónimos de", palabraIngresada, ":", resultado)