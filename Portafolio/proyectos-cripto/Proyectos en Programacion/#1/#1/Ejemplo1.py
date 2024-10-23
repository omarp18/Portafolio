#Solicitud de ingreso de datos
while True:
    entrada = input("Ingrese una cantidad de minutos: ")
    entrada = entrada.replace(',','.')
    if entrada.replace(',','.', 1).isdigit() or (entrada.count('.') == 1 and entrada.replace('.', '', 1).isdigit()):
        minutos = float(entrada)
        break
    else:
        print("Por favor, ingrese solo numeros enteros.")

#Calculo de minutos a horas
horas = int(minutos // 60)
minutos_restantes = int(round(minutos % 60, 2))

#Impresion
if horas == 1:
    hora_str = "hora"
else: 
    hora_str = "horas"
if minutos_restantes == 1:
    minutos_str = "minuto"
else: 
    minutos_str = "minutos"

print(f"{minutos} minutos equivalen a {horas} {hora_str} y {minutos_restantes} minutos")