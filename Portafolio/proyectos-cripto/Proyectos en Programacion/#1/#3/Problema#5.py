def encontrar_divisores(numero):
    divisores = []
    for i in range(1, numero):
        if numero % i == 0:
            divisores.append(i)
    return divisores

def es_perfecto(numero):
    divisores = encontrar_divisores(numero)
    sumaDivisores = sum(divisores)
    return sumaDivisores == numero

def main():
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero <= 0:
            print("Por favor, ingrese un número entero positivo.")
        else:
            if es_perfecto(numero):
                print(f"El número {numero} es perfecto.")
            else:
                print(f"El número {numero} no es perfecto.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
