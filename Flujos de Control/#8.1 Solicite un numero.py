num = input("Ingrese un numero: ")
num = input("Ingrese un numero: ")

if len(num) != 1:
    print("No se puede procesar el dato.\nDebe ingresar una solo numeros del rango del 0 al 9")
elif num in ("0123456789"):
    print(f"El numero ingresado: {num} esta dentro del rango")
else:
    print(f"El numero ingresado: {num} esta fuera del rango")
