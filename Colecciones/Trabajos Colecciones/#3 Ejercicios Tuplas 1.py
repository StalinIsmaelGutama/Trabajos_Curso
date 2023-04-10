#EJERCICIOS DE TUPLAS

#Crear una tupla vacía:

tuplas = ()

#Crear una tupla con algunos elementos:

tupla = (500, "Hola Mundo", [10,20,30], ('python',100))
print(tupla)

#Acceder a un elemento de la tupla:

print(tupla[1])

#Intentar modificar un elemento de la tupla (esto producirá un error ya que las tuplas son inmutables):

# tupla[0] = 20 

#Concatenar dos tuplas:

r = tupla + tuplas
print(r)

#Obtener la longitud de una tupla:

print(len(tupla))

#Convertir una tupla en una lista:

lista = list(tupla)
print(type(lista))

#Convertir una lista en una tupla:

tupla = tuple(lista)
print(type(tupla))