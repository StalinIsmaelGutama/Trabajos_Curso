"""
8.Escribí un programa que solicite al usuario una letra y, si es una vocal,
muestre el mensaje “Es vocal”. Verificar si el usuario ingresó un string de más de un carácter y,
en ese caso, informarle que no se puede procesar el dato.

"""
letra =  input("Ingrese una letra: ")

if len(letra) != 1 :
    print("No se puede procesar el dato.\nDebe ingresar una sola letra")
elif letra in "aeiouAEIOU":
    print("Es vocal")
else:
    print("No es una vocal")