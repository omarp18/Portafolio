diaSemana={
            1:"Lunes",
            3:"Miercoles",
            2:"Martes",
            4:"Jueves",
            5:"Viernes",
            6:"Sabado",
            7:"Domingo"
}
dia=int(input("Ingrese un valor del 1 al 7 "))
if dia in diaSemana:
    print(f"{dia}:{diaSemana[dia]}")
else:
    print("Valor incorrecto ")