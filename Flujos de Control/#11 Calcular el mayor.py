
"""
11. Determinar el mayor de tres números:
"""

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el terser numero: "))

if a>b and a >c :
    print(f"el numero {a} es mayor al segundo y tercer numero")
elif b>a and b >c :
    print(f"el numero {b} es mayor al primer y tercer numero")
elif c>b and c >a :
    print(f"el numero {c} es mayor al primer y segundo numero")
else :
    print(f"Ninguno de los tres numeros {a}, {b}, {c} es mayor ")