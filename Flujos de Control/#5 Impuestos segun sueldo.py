"""
5. Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
"""
salario = int(input("Ingrese el salario: "))
porcentaje = 0

if salario > 10000:
    porcentaje = 5/100
elif salario >= 10000 and salario < 20000:
    porcentaje = 15/100
elif salario >= 20000 and salario < 35000:
    porcentaje = 20/100
elif salario >= 35000 and salario < 60000:
    porcentaje = 30/100
elif salario >= 60000:
    porcentaje = 45/100
else:
    print("El salario ingresado es correcto")

total = salario * porcentaje

print("El valor del impuesto a pagar es:", total)

print("El salario que recibes es:",salario-total) 


