class VentaElectrodomesticos:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def calcular_ganancia(self):
        if self.precio < 5000:
            return self.precio * 0.15
        elif 5000 <= self.precio <= 12000:
            return self.precio * 0.20
        else:
            return self.precio * 0.30

def calcular_ganancias(ventas):
    ganancias_totales = 0
    for venta in ventas:
        ganancias_totales += venta.calcular_ganancia()
    return ganancias_totales

def main():
    cantidad_ventas = int(input("Ingrese la cantidad de ventas del mes: "))
    ventas = []

    for i in range(1, cantidad_ventas + 1):
        codigo = int(input(f"Ingrese el código del artículo {i}: "))
        nombre = input(f"Ingrese el nombre del artículo {i}: ")
        precio = float(input(f"Ingrese el precio del artículo {i}: "))
        venta = VentaElectrodomesticos(codigo, nombre, precio)
        ventas.append(venta)

    ganancias_totales = calcular_ganancias(ventas)
    print(f"\nLas ganancias totales del mes son: ${ganancias_totales:.2f}")

if __name__ == "__main__":
    main()
