### CURSO DE FUNDAMENTOS DE PYTHON
#1. Crear una lista de numeros del 1 al 50

lista = [1,2,3,4,5]
print(f"La lista es: {lista}")

#2. Accede al elemento 3 de la lista:

print(f"El elemento 2 es: {lista[1]}")

#3. Modifica un elemento de la lista:

lista[4]=10 
print("Se modifico el elemento 4: ", lista)

#4. Agrega el elemento 9 al final de la lista

lista.append(9)
print("Se agrega el elemento 9", lista)

#5. Eliminar el elemento 2 de la lista:

print("Se elimina el elemento 2: ", lista.pop(1))

#6. Recorrer una lista con un bucle for:

for e in lista:
    print(e)

#7. Ordenar una lista:

lista.sort(reverse= False)
print("la lista ordenada", lista)

#8. Obtener la longitud de una lista:

print("El numero de elementos es: ",len(lista))

#9. Comprobar si un elemento está en la lista:

print("este elemento si esta y se repite: ",lista.count(10), "numero de veces" )  
