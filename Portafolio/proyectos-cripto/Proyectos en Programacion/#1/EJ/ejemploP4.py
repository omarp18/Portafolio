nombre=input("Ingrese el nombre ")
sueldoMensual=float(input("Ingrese el sueldo mensual "))
edad=int(input("Ingrese la edad "))
sexo=input("Ingrese M para Masculino y F para femenino ").upper()
repuesta="No esta en ninguna categoria "
if sexo == "M":
    if sueldoMensual<500:
        repuesta="Hombre pobre"
elif sexo == "F":
    if sueldoMensual>6000:
        repuesta="Mujer Rica"
    elif (sueldoMensual>=1200 and sueldoMensual<=2000) and (edad>=20 and edad<=30):
        repuesta="Joven clase media"
print(repuesta)