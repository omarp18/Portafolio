class AlmacenNumeros:
    def __init__(self):
        self.numeros = []

    def agregar_numero(self, numero):
        if numero in self.numeros:
            return False
        else:
            self.numeros.append(numero)
            return True

    def mostrar_numeros(self):
        for numero in self.numeros:
            print(numero)

def main():
    almacen = AlmacenNumeros()
    cantidad_numeros = 10
    while len(almacen.numeros) < cantidad_numeros:
        try:
            numero = int(input(f"Ingrese un número entero distinto ({len(almacen.numeros) + 1}/{cantidad_numeros}): "))
            if not almacen.agregar_numero(numero):
                print("Número repetido. Intente nuevamente.")
            else:
                print("Número agregado correctamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

    print("\nLos números ingresados son:")
    almacen.mostrar_numeros()

if __name__ == "__main__":
    main()