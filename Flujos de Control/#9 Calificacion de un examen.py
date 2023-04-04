"""
9. Calificación de un examen. Ingrese la puntuación de un examen.
Si es >= 90 La calificación es A, si es >= 80 La calificación es B,
si es >= 70 La calificación es C,
si >= 60 La calificación es D,
sino La calificación es F,
"""

calificacion = int(input( "Ingrese la calificacion del examen: "))


if calificacion >= 90:
    print(f"Su nota es de {calificacion} y su calificacion es : A")
elif calificacion >= 80:
    print(f"Su nota es de {calificacion} y su calificacion es : B")
elif calificacion >= 70:
    print(f"Su nota es de {calificacion} y su calificacion es : C")
elif calificacion >= 60:
    print(f"Su nota es de {calificacion} y su calificacion es : D")
else :
    print(f"Su nota es de {calificacion} y su calificacion es : f")