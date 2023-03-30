"""
3. Escribir un programa que almacene la cadena de caracteres <b>contraseña</b> en una variable, 
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario
 coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""
x = "Sgt2803"

contra = input("Ingrese la contraseña: ")
# lower = convierte las cadenas a minusculas
if contra.lower() == x:
    print("Contraseña correcta")
else: 
    print("Contraseña incorrecta")
