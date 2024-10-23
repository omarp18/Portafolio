while True:
    nombre_medicamento = str(input("Ingrese el medicamento que desea comprar: "))
    if not any(char.isdigit() for char in nombre_medicamento):
        break
    print("El nombre del medicamento no debe contener numeros. Intente otra vez.")

while True:
    precio = input("Ingrese el precio que normalmente cuesta el medicamento: ")
    precio = precio.replace(',','.')
    if precio.replace(',','.', 1).isdigit() or (precio.count('.') == 1 and precio.replace('.', '', 1).isdigit()):
        precio = float(precio)
        break
    else:
        print("Por favor, ingrese un precio valido.")

descuento = round(precio * 0.35, 2)
precio_total = round(precio - descuento, 2)

print("")
print("Factura")
print(f"Nombre del medicamento:", nombre_medicamento)
print(f"Precio:", round(precio, 2))
print(f"Descuento del 35%:", descuento)
print(f"Precio total:", precio_total)