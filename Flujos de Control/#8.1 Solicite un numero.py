num = input("Ingrese un numero: ")

if len(num) != 1:
    print("No se puede procesar el dato.\nDebe ingresar una solo numeros del rango del 0 al 9")
elif num in ("0123456789"):
    print("El numero esta dentro del rango")
else:
    print("Esta fuera del rango")