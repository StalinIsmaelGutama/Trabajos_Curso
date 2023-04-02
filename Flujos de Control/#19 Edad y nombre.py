"""
19. Escribir un programa que pida al usuario su nombre y edad, 
y muestre por pantalla un mensaje con dichos datos en la siguiente forma: "Hola, {nombre}, tienes {edad} años".
"""

nombre = input("igresar su nombre: ")

edad = int(input("ingresar su edad "))

if edad >= 18:
    print(nombre, "es mayor de edad")
else:
    edad < 18
    print(nombre, "es menor de edad")