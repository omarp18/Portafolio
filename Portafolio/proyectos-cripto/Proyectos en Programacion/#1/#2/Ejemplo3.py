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

# Pide el numero por cual se va a sumar cada valor
while True:
    n = input("Ingrese un número por el cual se va a sumar a cada valor de la lista: ")
    if n.isdigit():
        num = int(n)
        break
    else:
        print("Por favor, ingrese solo números.")
        
# Pide el número entero a buscar
while True:
    try:
        numBuscado = int(input("Ingresa el número entero que deseas buscar en la lista: "))
        break
    except ValueError:
        print("Por favor, asegúrate de ingresar solo un número entero.")

# Sumar cada celda de la lista por el valor num
listaSumada = [x + num for x in lista]

# Determinar las veces que se encuentra el número en la lista
cont = lista.count(numBuscado)

# Determinar cuántos números pares hay en la lista
cantidadPares = sum(1 for x in lista if x % 2 == 0)

# Calcular la sumatoria de la lista
sumatoria = sum(lista)

# Imprimir resultados
print("Lista sumada por", num, ":", listaSumada)
print("Veces que se encuentra el número", numBuscado, "en la lista:", cont)
print("Cantidad de números pares en la lista:", cantidadPares)
print("Sumatoria de la lista:", sumatoria)