def capital_acumulado(capital_inicial, tasa_interes, años):
    if años == 0:
        return capital_inicial
    else:
        capital_acumulado_anterior = capital_acumulado(capital_inicial, tasa_interes, años - 1)
        return capital_acumulado_anterior * (1 + tasa_interes)

def main():
    try:
        capital_inicial = 24  # Dólares iniciales invertidos en 2020
        tasa_interes = 0.12   # Tasa de interés anual del 12%
        años = int(input("Ingrese el año para calcular el capital acumulado: "))
        
        capital = capital_acumulado(capital_inicial, tasa_interes, años - 2020)
        print(f"El capital acumulado en el año {años} sería de ${capital:.2f}")
    except ValueError:
        print("Por favor, ingrese un año válido.")

if __name__ == "__main__":
    main()