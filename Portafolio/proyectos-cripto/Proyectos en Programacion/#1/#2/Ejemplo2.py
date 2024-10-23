# Pide el numero para generar su multiplo
while True:
    n = input("Ingrese un número para generar sus multiplos: ")
    if n.isdigit():
        num = int(n)
        break
    else:
        print("Por favor, ingrese solo números.")

# Pide el tamaño del arreglo
while True:
    s = input("Ingrese el tamaño del arreglo: ")
    if s.isdigit():
        size = int(s)
        break
    else:
        print("Por favor, ingrese solo números.")

# Agrega los multiplos a la lista
lista = []

for i in range(1, size + 1):
    lista.append(num * i)

# Muestra el resultado
print(f"Los multiplos de", num, "son:", lista)