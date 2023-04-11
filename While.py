###CURSO DE FUNDAMENTOS DE PYTHON
#Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menu en el que le permitira seleccionar al usuario que ejercicios ejecutar.

#1.Contador ascendente: # Escribe un programa en Python que pida al usuario un número entero positivo y, 
#  utilizando un bucle while, cuente desde cero hasta ese número, imprimiendo cada número en la pantalla.


def contador_ascendente (num):
    cont = 0
    while cont <= num:
        print(cont)
        cont += 1

#2.Contador descendente: Escribe un programa en Python que pida al usuario un número entero positivo y,
#  utilizando un bucle while, cuente desde ese número hasta cero, imprimiendo cada número en la pantalla.


def contador_descendente (num):
    cont = num
    while cont >= 0:
        print(cont)
        cont -= 1

#3.Suma de números: Escribe un programa en Python que pida al usuario un número entero positivo y, 
# utilizando un bucle while, calcule la suma de todos los números desde cero hasta ese número y lo imprima en la pantalla.

def suma_numeros (num):
    cont = 0
    suma = 0
    while cont <= num:
        cont += 1
        suma += cont
    return suma - (num + 1) 

#4.Factorial: Escribe un programa en Python que pida al usuario un número entero positivo y, 
# utilizando un bucle while, calcule el factorial de ese número y lo imprima en la pantalla. 
# El factorial de un número n se define como el producto de todos los números enteros desde 1 hasta n.

def factorial (num):
    cont = 1
    mul = 1
    while cont <= num: 
        mul = mul * cont
        cont += 1
    return mul      

#5.Adivinar un número: Escribe un programa en Python que genere un número aleatorio entre 1 y 100, 
# y pida al usuario que adivine ese número. Si el usuario ingresa un número mayor al número generado,
# el programa debe imprimir "El número que buscas es menor". Si el usuario ingresa un número menor al número generado, 
# el programa debe imprimir "El número que buscas es mayor". Si el usuario adivina el número, el programa debe imprimir 
# "¡Felicitaciones, adivinaste el número!" y terminar.


import random
def adivinar_num (num):
    numero = 0
    while numero != num:
        numero = int(input("Adivine el numero aleatorio: ")) 
        if numero > num:
            print("El numero que buscas es menor")
        elif numero < num:
            print("El numero que buscas en mayor")
        else:
            print("Adivinaste")

#6.Contador de vocales: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, 
# cuente la cantidad de vocales que tiene esa cadena. Para simplificar el problema, puedes considerar que la cadena solo contiene letras minúsculas.

def contador_vocales(letra):
    
    if letra in "aeiouAEIOU":
        print("Es vocal")
    else:
        print("No es una vocal")


#Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menu en el que le permitira seleccionar al usuario que ejercicios ejecutar.
########################### MENU DE OPCIONES #####################################

opcion =  1
while opcion >= 0 and opcion <=10 :

    print("############### MENU DE OPCIONES ######################")
    print(" 1.- Contador Ascendente")
    print(" 2.- Contador Descendente")
    print(" 3.- Suma de Numeros")
    print(" 4.- Factorial")
    print(" 5.- Adivinar el numero")
    print(" 6.- Contador de Vocales")
    print(" 7.- Suma de numeros pares")
    print(" 8.- Calculo de potencia")
    print(" 9.- Calculo de Promedio")
    print(" 10.- Contador de Palabras")
    print(" 0.- Salir")

    opcion = int(input("Digite la opcion, deseada: "))

    if opcion == 0:

        print("Ha seleccionado la opccion Salir \n\tQue tenga Buen Dia")
        break

    elif opcion == 1:

        print("Ha selecionado la opcion 1 : \n\tContador Ascendente")
        num = int(input("Ingrese el numero deseado: "))
        contador_ascendente(num)

    elif opcion == 2:

        print("Ha selecionado la opcion 2 : \n\tContador Descendente")
        num = int(input("Ingrese un numero: "))
        contador_descendente(num)

    elif opcion == 3:

        print("Ha selecionado la opcion 3 : \n\tSuma de Numeros")
        num = int(input("Ingrese un numero: "))
        print(suma_numeros(num))

    elif opcion == 4:

        print("Ha selecionado la opcion 4 : \n\tFactorial")
        num = int(input("Ingrese un numero: "))
        print(factorial(num))   

    elif opcion == 5:

        print("Ha selecionado la opcion 5 : \n\tAdivinar el numero")
        num = random.randint (1 ,10)
        adivinar_num(num)

    elif opcion == 6:

        print("Ha selecionado la opcion 6 : \n\tContador de Vocales")
        letra = input("ingrese una vocal: ")
        contador_vocales(letra)

    elif opcion == 7:

        print("Ha selecionado la opcion 7 : \n\tSuma de numeros pares")

    elif opcion == 8:

        print("Ha selecionado la opcion 8 : \n\tCalculo de potencia")

    elif opcion == 9:
        print("Ha selecionado la opcion 9 : \n\tCalculo de Promedio")
    elif opcion == 10:
        print("Ha selecionado la opcion 10 : \n\tContador de Palabras")



