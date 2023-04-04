"""
6. Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta.
"""

n1 = int(input("Ingrese el primer valor: "))
n2 = int(input("Ingrese el segundo valor: "))

r = 0

print("Presione 1 para sumar: ")
print("Presione 2 pra restar:")
print("Presione 3 para multiplicar: ")

comando = int(input("Digite una opcion: "))

if comando == 1:
    print("La suma es: ", r)
    r = n1 + n2 
elif comando == 2:
    print("La resta es: ", r)
    r = n1 - n2 
elif comando == 3:
    print("La multiplicacion es: ", r)
    r = n1 * n2 
else:
    print("Comando no valido")
