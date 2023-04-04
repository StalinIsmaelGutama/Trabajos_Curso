"""
17. Escribir un programa que pida al usuario una nota del 0 al 10 y muestre por pantalla la calificación según la siguiente tabla:
- 0-2: Muy deficiente
- 3-4: Insuficiente
- 5-6: Suficiente
- 7: Bien
- 8-9: Notable
- 10: Sobresaliente
"""

n = float(input("Ingrese la nota: "))

if n >= 0 and n <= 2:

    print(f"La nota de {n} es muy deficiente")
elif n >= 3 and n <= 4:
    print(f"La nota de {n} es insuficiente")
elif n >= 5 and n <= 6:
    print(f"La nota de {n} es suficiente")
elif n == 7:
    print(f"La nota de {n} esta bien")
elif n >= 8 and n <= 9:
    print(f"La nota de {n} es notable")
elif n == 10:
    print(f"La nota de {n} es sobresaliente")
else:
    print(f"La nota de {n} no existe")
