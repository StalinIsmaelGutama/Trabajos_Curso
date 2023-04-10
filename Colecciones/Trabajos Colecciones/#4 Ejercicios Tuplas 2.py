#EJERCICIOS DE TUPLAS

#Crear una tupla de números enteros y calcular su suma y promedio.

tupla = (5,10,8,89,74,85,85,96,32,65,24,23,21,74,1,3,2,4,5,6,7,8,9)
print("La suma de la tupla: ",sum(tupla))
print("El promedio de la tupla: ",sum(tupla)/len(tupla))

#Crear dos tuplas de la misma longitud y crear una nueva tupla que contenga la suma de los elementos correspondientes de ambas tuplas.

suma = 0
t1 = (0,1,2,3,4,5,6,7,8,9)
t2 = (9,8,7,6,5,4,3,2,1,0)
for i in range(len(t1)):
        suma += (t1[i]+t2[i])

print("El resultado de la suma es: ",suma)

#Crear una tupla de nombres y ordenarla alfabéticamente.

nombres = ("Stalin","Sandro","Sebastian","Ariel","Paul")
print(sorted(nombres))

#Crear una tupla de números y encontrar el valor mínimo y máximo.

print("El valor minimo de la tupla es: ", min(tupla))
print("El valor maximo de la tupla es: ", max(tupla))

#Crear una tupla de números y convertirla en una lista.

tupla = (5,10,8,89,74,85,85,96,32,65,24,23,21,74,1,3,2,4,5,6,7,8,9)
lista = list(tupla)
print(type(lista))

#Crear una tupla con los días de la semana y mostrar el tercer elemento.

semana = ("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
print(semana[3])

#Crear una tupla con números enteros y mostrar aquellos que son pares.

tupla = (5,10,8,89,74,85,85,96,32,65,24,23,21,74,1,3,2,4,5,6,7,8,9)
pares = 0 

for i in tupla:
    if i % 2 == 0:
          print("Los numeros pares son:",i)

#Crear una tupla con los meses del año y mostrar aquellos que tienen más de cinco letras.

meses = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
for mes in meses:
      if len(mes) > 5:
            print(mes)

#Crear una tupla con las edades de varias personas y mostrar la cantidad de personas mayores de 18 años.

edades = (12, 25, 32, 16, 20, 18, 19, 22, 15, 30)
contador = 0
for edad in edades:
    if edad > 18:
        contador += 1

print("Cantidad de personas mayores de 18 años:", contador)

#Crear una tupla de tuplas que contienen información de libros y mostrar el título del tercer libro.

libros = (
    ("El señor de los anillos", "J.R.R. Tolkien", 1954),
    ("Cien años de soledad", "Gabriel García Márquez", 1967),
    ("Don Quijote de la Mancha", "Miguel de Cervantes", 1605),
    ("1984", "George Orwell", 1949),
    ("Matar a un ruiseñor", "Harper Lee", 1960)
)

print(libros[2][0])
