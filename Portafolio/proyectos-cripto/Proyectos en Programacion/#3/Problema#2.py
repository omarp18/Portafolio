class Cliente:
    def __init__(self, nombre, cedula, edad, tipoHabitacion, numHabitaciones):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.tipoHabitacion = tipoHabitacion
        self.numHabitaciones = numHabitaciones
        self.registro = cedula[-4:]

class Hotel:
    def __init__(self):
        self.habitacionesDisponibles = {
            'Sencilla': 10,
            'Doble': 10,
            'Suite': 3
        }
        self.tarifas = {
            'Sencilla': 40,
            'Doble': 60,
            'Suite': 80
        }
        self.clientes = []
        self.totalRecaudado = 0

    def registrarCliente(self, cliente):
        if cliente.edad < 18:
            print(f"\nNo se puede registrar al cliente {cliente.nombre}. Debe ser mayor de edad.")
            return False
        if self.habitacionesDisponibles[cliente.tipoHabitacion] >= cliente.numHabitaciones:
            self.habitacionesDisponibles[cliente.tipoHabitacion] -= cliente.numHabitaciones
            self.clientes.append(cliente)
            self.totalRecaudado += self.tarifas[cliente.tipoHabitacion] * cliente.numHabitaciones
            print(f"\nCliente {cliente.nombre} registrado exitosamente con número de registro {cliente.registro}.")
            return True
        else:
            print(f"\nNo hay suficientes habitaciones de tipo {cliente.tipoHabitacion} disponibles.")
            return False

    def reporteHabitaciones(self):
        print("\nReporte de habitaciones:")
        for tipo, disponibles in self.habitacionesDisponibles.items():
            print(f"{tipo}: {'Ocupada' if disponibles == 0 else 'Disponible'} ({disponibles} disponibles)")

    def reporteClientes(self):
        print("\nClientes registrados:")
        for cliente in self.clientes:
            print(f"Nombre: {cliente.nombre}, Registro: {cliente.registro}, Tipo de Habitación: {cliente.tipoHabitacion}, Número de Habitaciones: {cliente.numHabitaciones}")

    def reporteTotalRecaudado(self):
        print(f"\nTotal recaudado: ${self.totalRecaudado}")

def main():
    hotel = Hotel()
    
    while True:
        print("\n1. Registrar Cliente\n2. Ver Reporte de Habitaciones\n3. Ver Clientes Registrados\n4. Ver Total Recaudado\n5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("\nIngrese el nombre del cliente: ")
            cedula = input("Ingrese el número de cédula: ")
            edad = int(input("Ingrese la edad: "))
            tipoHabitacion = input("Ingrese el tipo de habitación (Sencilla, Doble, Suite): ")
            numHabitaciones = int(input("Ingrese el número de habitaciones que necesita: "))
            cliente = Cliente(nombre, cedula, edad, tipoHabitacion, numHabitaciones)
            hotel.registrarCliente(cliente)
        elif opcion == "2":
            hotel.reporteHabitaciones()
        elif opcion == "3":
            hotel.reporteClientes()
        elif opcion == "4":
            hotel.reporteTotalRecaudado()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción correcta.")

if __name__ == "__main__":
    main()