# Inicializar un diccionario para almacenar el número de alumnos para cada peso
pesos = {peso: 0 for peso in range(10, 101)}

# Leer los pesos de los alumnos
while True:
    entrada = input("Ingrese el peso del alumno (10-100 kg, o 'F' para terminar): ")

    # Verifica si el usuario quiere dejar de ingresar pesos
    if entrada.upper() == 'F':
        break

    # Valida si la entrada es un número
    if not entrada.isdigit():
        print("Por favor, solo ingrese números o 'F' para terminar.")
        continue

    peso = int(entrada)
    
    # Valida el parametro de los pesos entre 10kg a 100kg
    if peso < 10 or peso > 100:
        print("El peso debe estar entre 10kg a 100 kg.")
    else:
        pesos[peso] += 1

# Imprimir el histograma solo para los pesos con estudiantes
print("\nPeso    Número de alumnos")
print("-"*25)
for peso, cantidad in pesos.items():
    if cantidad > 0:
        print(f"{peso:2d} kg | {'*' * cantidad}")