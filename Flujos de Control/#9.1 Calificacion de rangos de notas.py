"""
9.1. Realizar un ejercicio que ingrese la nota final,
valide si esta dentro del rango de las calificaciones,
evaluar con respecto al metodo de calificacion
"""
calificacion  = float(input("Ingrese su calificacion: "))

if 0 <= calificacion <= 10:
    if calificacion >= 0 and calificacion < 4:
            print(f"Su nota de: {calificacion} \nTiene una equivalencia de DEFICIENTE")
    elif calificacion >= 4 and  calificacion < 7:
            print(f"Su nota de: {calificacion} \nTiene una equivalencia de REGULAR")
    elif calificacion >= 7 and calificacion < 8.5:
            print(f"Su nota de: {calificacion} \nTiene una equivalencia de BUENO")
    elif calificacion >= 8.5 and calificacion < 9.5:
            print(f"Su nota de: {calificacion} \nTiene una equivalencia de MUY BUENO")
    else:
        calificacion >= 9.5
        print(f"Su nota de: {calificacion} \ntiene una equivalencia de EXCELENTE ")
else:
       print(f"Su nota de: {calificacion} \nno esta dentro del rango de las CALIFICACIONES")
