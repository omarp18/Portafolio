# Pide la lista de números enteros
lista = []
while True:
    try:
        num = input("Ingresa un número entero para la lista (o 'F' para terminar): ")
        if num.upper() == 'F':
            break
        lista.append(int(num))
    except ValueError:
        print("Por favor, asegúrate de ingresar solo números enteros.")

# Pide el número entero a buscar
while True:
    try:
        numBuscado = int(input("Ingresa el número entero que deseas buscar en la lista: "))
        break
    except ValueError:
        print("Por favor, asegúrate de ingresar solo un número entero.")

# Cuneta las repeticiones del número en la lista
cont = 0
for elem in lista:
    if elem == numBuscado:
        cont += 1

# Muetra el resultado
print(f"El número {numBuscado} se repite {cont} veces en la lista.")