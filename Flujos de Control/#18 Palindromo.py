"""
18. Escribir un programa que pida al usuario una frase y determine si es un palíndromo. 
Ignorar espacios en blanco y mayúsculas/minúsculas al determinar si la frase es un palíndromo o no.
-Un palíndromo es una palabra, número o frase que se lee igual de izquierda a derecha que de derecha a izquierda. 
Por ejemplo, "ana", "radar" y "aibohphobia" son palíndromos.
"""

palabra = input("Ingrese la palabra a comprobar: ")

if str(palabra) == str(palabra)[::-1] : # Primero calculamos el valor inverso de la palabra original con [::-1] como índice de lista.
    print(f"La palabra ingresada {palabra},si es un Palindromo")
else:
    print(f"La palabra ingresada {palabra},no es Palindromo")