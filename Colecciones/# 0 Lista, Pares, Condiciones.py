"""
pares = [1,2,3,4,5,6,7,8,9,10]

for e in pares:
    if e % 2 == 0:
        print("el numero es par",e )
"""



"""
nombres = ["Sebastian","Sandro","Bruce","Emily","Ariel","Paul","Jhonnathan"]
print(nombres)

for e in nombres:
    print(e.upper())
"""



"""
elementos = [0,1,-1,0,5,-2,-6,8,10,9,-3,-5,-10,0]
print(elementos)

for e in elementos:
    if e > 0:
        print(f"El numero {e} es positivo")
    elif e == 0:
        print(f"El numero {e} igual a cero")
    else:
        print(f"El numero {e} es negativo")
"""

elementos = [0,1,-1,0,5,-2,-6,8,10,9,-3,-5,-10,0]

ceros = []
positivos = []
negativos = []

for e in elementos:
    if e == 0:
        ceros.append(e)
    elif e > 0:
        positivos.append(e)
    else:
        negativos.append(e)


print(f"Los numeros de valor son: \n\t{ceros} ")
print(f"Los numeros de valor positivo son: \n\t{positivos} ")
print(f"Los numeros de valor negativo son: \n\t{negativos} ")
