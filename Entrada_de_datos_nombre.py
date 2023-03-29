"""
Escribir un programa que pregunte el nombre del usuario en la consola y 
después de que el usuario lo introduzca muestre por pantalla la cadena 
¡Hola "nombre"!, donde "nombre" es el nombre que el usuario haya introducido.
"""

nombre = input("Ingrese su nombre por favor: ")

# Opcion 1
print("Hola " + nombre + " gusto en conocerte")

# Opcion 2
print(f"Hola {nombre} gusto en conocerte")

# Opcion 3
print("Hola {} gusto en conocerte".format(nombre))

# Opcion 4
print("Hola",nombre,"gusto en conocerte")