import csv
class Escuela:
    def __init__(self):
        self.notaMasAlta = 0
        self.cedulaEstudianteMasAlta = ""
        self.totalNotas = 0
        self.sumaNotas = 0
    def mayor_nota(self, archivo_csv):
        try:
            with open(archivo_csv, "r", newline="") as archivo:
                lector_csv = csv.reader(archivo, delimiter=";" or ",")
                next(lector_csv)
                for fila in lector_csv:
                    cedula, nota = fila[1], int(fila[3])
                    if nota > self.notaMasAlta:
                        self.notaMasAlta = nota
                        self.cedulaEstudianteMasAlta = cedula
                    self.totalNotas += 1
                    self.sumaNotas += nota
        except FileNotFoundError as e:
            print(f"Error: Archivo no encontrado: {e.filename}")
            raise
        except Exception as e:
            print(f"Error inesperado al procesar el archivo: {e}")
            raise
        return self.notaMasAlta, self.cedulaEstudianteMasAlta
    
    def promedioNotas(self):
        if self.totalNotas == 0:
            raise ZeroDivisionError("No hay notas para calcular el promedio")
        promedio = self.sumaNotas / self.totalNotas
        return promedio
    
obj_Escuela = Escuela()
archivo_estudiantes = "Estudiantes.csv"
try:
    nota_mas_alta, cedula_estudiante = obj_Escuela.mayor_nota(archivo_estudiantes)
    promedioNotas = obj_Escuela.promedioNotas()
    print(f"El estudiante con la nota más alta es: {cedula_estudiante} con {nota_mas_alta}")
    print(f"El promedio de notas es: {promedioNotas:.2f}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")