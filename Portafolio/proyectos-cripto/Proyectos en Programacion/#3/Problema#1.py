class PatternSquare:
    def __init__(self, dimension):
        self.dimension = dimension
        self.square = [[0] * dimension for _ in range(dimension)]

    def generateValue(self, row, col):
        if row == 0 or col == 0:
            return 1
        if self.square[row][col] == 0:
            self.square[row][col] = self.generateValue(row - 1, col) + self.generateValue(row, col - 1)
        return self.square[row][col]

    def generatePattern(self):
        for row in range(self.dimension):
            for col in range(self.dimension):
                self.square[row][col] = self.generateValue(row, col)

    def displayPattern(self):
        for row in self.square:
            print(' '.join(map(str, row)))


# Ejemplo de uso
if __name__ == "__main__":
    while True:
        try:
            n = int(input("Ingrese la dimensión del cuadrado (n): "))
            if n > 0:
                break
            else:
                print("Por favor, ingrese un número entero positivo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

    square = PatternSquare(n)
    square.generatePattern()
    square.displayPattern()