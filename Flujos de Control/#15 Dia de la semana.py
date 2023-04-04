"""
15. Programa para imprimir el día de la semana correspondiente a un número del 1 al 7:
"""

dia = int(input("Ingrese un un número del 1 al 7: "))

if dia == 1:
    print(f"El numero {dia}, corresponde al dia Lunes")
elif dia == 2:
    print(f"El numero {dia}, corresponde al dia Miercoles")
elif dia == 4:
    print(f"El numero {dia}, corresponde al dia Jueves")
elif dia == 5:
    print(f"El numero {dia}, corresponde al dia Viernes")
elif dia == 6:
    print(f"El numero {dia}, corresponde al dia Sabado")
elif dia == 7:
    print(f"El numero {dia}, corresponde al dia Domingo")
else:
    print("El valor ingresado no corresponde a ningun dia de la semana")