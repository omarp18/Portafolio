agenda = {}

while True:
    print("\n--- Agenda de Contactos ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")
        correo = input("Ingrese el correo electrónico: ")
        agenda[nombre] = [telefono, correo]
        print("Contacto agregado correctamente.")
    elif opcion == "2":
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        if nombre in agenda:
            print(f"Nombre:", nombre)
            print(f"Teléfono:", agenda[nombre][0])
            print(f"Correo electrónico:", agenda[nombre][1])
        else:
            print("El contacto no existe en la agenda.")
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
