class PolizaSeguros:
    def __init__(self, tipo_poliza):
        self.tipo_poliza = tipo_poliza
        if tipo_poliza == 'A':
            self.cuota_base = 1200
        elif tipo_poliza == 'B':
            self.cuota_base = 950
        else:
            raise ValueError("Tipo de póliza no válido")

    def calcular_costo(self, bebe_alcohol=False, usa_lentes=False, padece_enfermedad=False, edad=0):
        costo_total = self.cuota_base
        if bebe_alcohol:
            costo_total += self.cuota_base * 0.1
        if usa_lentes:
            costo_total += self.cuota_base * 0.05
        if padece_enfermedad:
            costo_total += self.cuota_base * 0.05
        if edad > 40:
            costo_total += self.cuota_base * 0.2
        else:
            costo_total += self.cuota_base * 0.1
        return costo_total

def main():
    personas_compraron = 0
    recaudacion_total = 0

    while True:
        try:
            tipo_poliza = input("Ingrese el tipo de póliza (A/B): ").upper()
            if tipo_poliza not in ['A', 'B']:
                raise ValueError("Tipo de póliza no válido")
            
            bebe_alcohol = input("¿Bebe alcohol? (Sí/No): ").lower() == 'si'
            usa_lentes = input("¿Usa lentes? (Sí/No): ").lower() == 'si'
            padece_enfermedad = input("¿Padece alguna enfermedad? (Sí/No): ").lower() == 'si'
            edad = int(input("Ingrese su edad: "))

            poliza = PolizaSeguros(tipo_poliza)
            costo_poliza = poliza.calcular_costo(bebe_alcohol, usa_lentes, padece_enfermedad, edad)
            print(f"El costo de la póliza es: ${costo_poliza:.2f}")
            
            personas_compraron += 1
            recaudacion_total += costo_poliza

            continuar = input("¿Desea continuar? (Sí/No): ").lower()
            if continuar != 'si':
                break
        except ValueError as e:
            print(e)

    print(f"Total de personas que compraron una póliza: {personas_compraron}")
    print(f"Recaudación total del día: ${recaudacion_total:.2f}")

if __name__ == "__main__":
    main()