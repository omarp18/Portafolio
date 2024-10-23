totalCompradores = 0
totalAbonoRecaudar = 0

compradores = []

while True:
    num = input(f"\nIngrese el número de compradores: ")
    if num.isdigit():
        numCompradores = int(num)
        break
    else:
        print("Por favor, ingrese solo números.")

for i in range(numCompradores):
    nombre = input(f"Ingrese el nombre del comprador {i+1}: ")
    while True:
        s = input(f"Ingrese el salario de {nombre}: ")
        if s.isdigit():
            salario = float(s)
            break
        else:
            print("Por favor, ingrese solo números.")


    print(f"\nSeleccione el tipo de casa para {nombre}:")
    print("1. Valor de Casa: $150,000")
    print("2. Valor de Casa: $200,000")
    while True:
        o = input("Seleccione el tipo de casa (1 o 2): ")
        if o.isdigit():
            opcionCasa = int(o)
            break
        else:
            print("Por favor, ingrese una de las dos opciones")
    if opcionCasa == 1:
        valorCasa = 150000
    elif opcionCasa == 2:
        valorCasa = 200000
    else:
        print("Opción no válida. Seleccionando valor de casa por defecto: $150,000")
        valorCasa = 150000

    compradores.append({"nombre": nombre, "salario": salario, "valorCasa": valorCasa})

print("\nNombre\tValor de Casa\tCuota Mensual\tCuota Inicial")
print("-----------------------------------------------------")

for comprador in compradores:
    nombre = comprador["nombre"]
    salario = comprador["salario"]
    valorCasa = comprador["valorCasa"]

    if salario <= 5000:
        cuotaInicial = 0.15 * valorCasa
        plazo = 20
    else:
        cuotaInicial = 0.15 * valorCasa
        plazo = 15 

    montoPrestamo = valorCasa - cuotaInicial
    cuotaMensual = montoPrestamo / (plazo * 12)  
    
    totalCompradores += 1
    totalAbonoRecaudar += cuotaInicial

    print(f"{nombre}\t${valorCasa}\t\t${cuotaMensual:.2f}\t\t${cuotaInicial:.2f}")

print(f"\nTotal de compradores: {totalCompradores}")
print(f"Total de abono a recaudar: ${totalAbonoRecaudar:.2f}")
