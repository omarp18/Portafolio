import platform

class SistemaOperativoDetector:
    def __init__(self):
        self.sistemaOperativo = None

    def detectarSistemaOperativo(self):
        self.sistemaOperativo = platform.system()
        # Mapeo de nombres de sistemas operativos
        if self.sistemaOperativo == "Darwin":
            self.sistemaOperativo = "macOS"

    def mostrarSistemaOperativo(self):
        if self.sistemaOperativo:
            print(f"El sistema operativo detectado es: {self.sistemaOperativo}")
        else:
            print("No se ha detectado el sistema operativo. Primero ejecute el método 'detectarSistemaOperativo'.")

# Crear una instancia de la clase
detector = SistemaOperativoDetector()

# Detectar el sistema operativo
detector.detectarSistemaOperativo()

# Mostrar el sistema operativo detectado
detector.mostrarSistemaOperativo()