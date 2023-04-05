#CURSO DE FUNDAMENTOS DE PYTHON 

#EJERCICIOS DE LISTAS A RESOLVER

#Crea una lista vacía llamada numeros e introduce los números del 1 al 5. Luego, muestra la lista por pantalla.

"""
numeros = []

for e in range(5):
    numeros.append(int(input("Introduce los numeros del 1 al 5: ")))    

print(f"Los numeros de la lista son: \n\t{numeros}")
"""

#Crea una lista con los nombres de tus amigos y muestra por pantalla el primer elemento de la lista.

"""
nombres = ['Sandro', 'Sebastian', 'Ariel', 'Paul', 'Bruce', 'Jhonnathan', 'Emily', 'Adriana']

print("El primer elemento de la lista es:",nombres[0])
"""

#Crea una lista con los números del 1 al 10 y muestra por pantalla los números pares.

"""
numeros = [1,2,3,4,5,6,7,8,9,10]

for e in numeros:
    if e % 2 == 0:
        print(f"El numero es par: {e} ")
"""


#Crea una lista con los nombres de tus amigos y muestra por pantalla el último elemento de la lista.

"""
nombres = ['Sandro', 'Sebastian', 'Ariel', 'Paul', 'Bruce', 'Jhonnathan', 'Emily', 'Adriana']

print("El ultimo elemento de la lista es:",nombres[-1])
"""

#Crea una lista con los números del 1 al 10 y muestra por pantalla el último elemento de la lista.

"""
numeros = [1,2,3,4,5,6,7,8,9,10]

print("El ultimo elemento de la lista es:",numeros[-1])
"""

#Crea una lista con los números del 1 al 10 y muestra por pantalla los números impares.

"""
numeros = [1,2,3,4,5,6,7,8,9,10]

for e in numeros:
    if e % 2 != 0:
        print(f"El numero es impar: {e} ")
"""

#Crea una lista con los nombres de tus amigos y añade un nuevo amigo a la lista. Luego, muestra la lista por pantalla.

"""
nombres = ['Sandro', 'Sebastian', 'Ariel', 'Paul', 'Bruce', 'Jhonnathan', 'Emily', 'Adriana']

nombres.append("Preciado")

print(nombres)

# nombres.insert(2,'Preciado')
"""

#Crea una lista con los números del 1 al 10 y muestra por pantalla el primer y el último elemento de la lista.

"""
numeros = [1,2,3,4,5,6,7,8,9,10]

print(F"El primer elemento de la lista es: {numeros[1]} \n\t y el ultimo elemento es: {numeros[-1]}")
"""

#Crea una lista con los nombres de tus amigos y muestra por pantalla el número de elementos de la lista.

"""
nombres = ['Sandro', 'Sebastian', 'Ariel', 'Paul', 'Bruce', 'Jhonnathan', 'Emily', 'Adriana']

print("El numero de elementos de la lista nombres es:",len(nombres))
"""

#Crea una lista con los números del 1 al 10 y muestra por pantalla la suma de todos los elementos de la lista.

"""
numeros = [1,2,3,4,5,6,7,8,9,10]
suma = 0    

for e in numeros:
    if e <= len(numeros):
     suma = e + suma

print(f"La suma de todos los elementos es: {suma} ")

print(sum(numeros))
"""