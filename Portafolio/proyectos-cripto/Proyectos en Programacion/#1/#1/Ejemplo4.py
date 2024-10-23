# Solicitar al usuario la cantidad de litros de leche producida en un día
while True:
    litros_producidos = input("Ingrese la cantidad de litros producidos: ")
    litros_producidos = litros_producidos.replace(',','.')
    if litros_producidos.replace(',','.', 1).isdigit() or (litros_producidos.count('.') == 1 and litros_producidos.replace('.', '', 1).isdigit()):
        litros_producidos = float(litros_producidos)
        break
    else:
        print("Por favor, ingrese un precio valido.")

# Convertir litros a galones
galones = litros_producidos / 3.785

# Precio por galón
precio_galon = 3.00

# Calcular el pago total
pago_total = galones * precio_galon

# Mostrar el resultado al usuario
print("")
print(f"La cantidad de litros producidos es de:", litros_producidos)
print(f"Esto equivale a", round(galones, 2), "galones.")
print(f"El pago total por la entrega de la producción de un día es de B/.",round(pago_total, 2))