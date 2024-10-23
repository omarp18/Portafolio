class InversorDeNumeros:
    def __init__(self, numero):
        self.numero = numero

    def invertir_numero(self, numero=None, invertido=0):
        if numero is None:
            numero = self.numero

        if numero == 0:
            return invertido
        else:
            invertido = (invertido * 10) + (numero % 10)
            return self.invertir_numero(numero // 10, invertido)

# Función principal para interactuar con el usuario
def main():
    try:
        numero = int(input("Ingrese un número entero: "))
        inversor = InversorDeNumeros(numero)
        numero_invertido = inversor.invertir_numero()
        print(f"El número invertido es: {numero_invertido}")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
