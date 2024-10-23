#El tiempo que tarda el profesor en calificar cada parcial para cada modelo
tiempo_A = 5
tiempo_B = 7
tiempo_C = 6

#Solicitud de ingreso de datos
while True:
    cantidad_A = input("Ingrese la cantidad de parciales del modelo A del grupo EGPH-01: ")
    if cantidad_A.isdigit():
        cantidad_A = int(cantidad_A)
        break
    else:
        print("Por favor, ingrese solo numeros enteros.")
while True:
    cantidad_B = input("Ingrese la cantidad de parciales del modelo A del grupo EGPH-02: ")
    if cantidad_B.isdigit():
        cantidad_B = int(cantidad_B)
        break
    else:
        print("Por favor, ingrese solo numeros enteros.")
while True:
    cantidad_C = input("Ingrese la cantidad de parciales del modelo A del grupo EGPH-03: ")
    if cantidad_C.isdigit():
        cantidad_C = int(cantidad_C)
        break
    else:
        print("Por favor, ingrese solo numeros enteros.")

#Calculo de tiempo por modelo
tiempo_grupoA = cantidad_A * tiempo_A
tiempo_grupoB = cantidad_B * tiempo_B
tiempo_grupoC = cantidad_C * tiempo_C
tiempo_total = tiempo_grupoA + tiempo_grupoB + tiempo_grupoC

#Impresion
if tiempo_total>60:
    horas = tiempo_total // 60
    minutos_restantes = tiempo_total % 60
    print(f"El profesor demorara ", horas," horas con ", minutos_restantes," minutos en revisar todos los parciales.")
else:
    print(f"El profesor demorara ", tiempo_total," minutos en revisar todos los parciales.")