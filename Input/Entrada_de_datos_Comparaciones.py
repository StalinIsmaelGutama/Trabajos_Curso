""""
1. Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):

- Si los dos números son iguales
- Si los dos números son diferentes
- Si el primero es mayor que el segundo
- Si el segundo es mayor o igual que el primero

"""

n1 = int(input("Ingrese el primero dato: "))
n2 = int(input("Inrgese el segundo dato: "))

n3 = n1 == n2 

"""
Opcion 1
"""

print("Los numeros:" + str(n1) + "y" + str(n2) + "son iguales:" + str(n3)) 

n4 = n1 != n2
print("Los numeros:" + str(n1) + "y" + str(n2) + "son diferentes:" + str(n4))

n5 = n1 > n2
print("El numero: " + str(n1) + " es mayor que: " + str(n2) + " R: " +  str(n5))

n6 = n1 < n2 
print("El numero: " + str(n2) + " es mayor que: " + str(n1) + " R: " + str(n6))


"""
Opcion 2
"""


print(f"Los numeros {n1} y {n2} son iguales: {n3}")

print(f"Los numeros {n1} y {n2} son diferentes: {n4}")

print(f"El numero: {n1} es mayor que: {n2} R: {n5}")

print(f"El numero: {n2} es mayor que: {n2} R: {n6}")


"""
Opcion 3 
"""

print("Los numeros {} y {} son iguales: {}".format(n1, n2, n3))

print("Los numeros {} y {} son diferentes: {}".format(n1, n2, n4))

print("El numero: {} es mayor que: {} R: {}".format(n1, n2, n5))

print("El numero: {} es mayor que: {} R: {}".format(n2, n1, n6))

"""
Opcion 4
"""

print("Los numeros",n1,"y",n2,"son iguales:",n3)

print("Los numeros",n1,"y",n2,"son diferentes",n4)

print("El numero",n1,"es mayor que",n2,"R:",n5)

print("El numero",n2,"es mayor que",n1,"R:",n6)