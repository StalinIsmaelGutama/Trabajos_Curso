"""
7.La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.

- Ingredientes vegetarianos: Pimiento y tofu.
- Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe 
mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""

print('\n\tPizzería Napolitana\n\n\tMenú de Pizzas\n1.Pizzas vegetarianas\n2.Pizzas no vegetarianas')

opción=int(input('Ingrese una opción del menú: '))

if opción==1:
    print('\tUsted eligio el tipo de pizzas vegetarianas\nLos ingredientes disponibles son:\n1.Pimiento\n2.tofu\n Solo puede elegir un ingrediente!!!')
    ingredientev=int(input('Escriba el numero del ingrediente que le quiere agregar a su pizza: '))
    if ingredientev==1:
        print('Su pizza consta de Pimiento, mozzarella y tomate!!')
    elif ingredientev==2:
        print('Su pizza consta de Tofu, mozzarella y tomate!!')
    else:
        print('El valor que ingreso no corresponde a un valor del menú')
elif opción==2:
    print('\tUsted eligio el tipo de pizzas no vegetarianas\nLos ingredientes disponibles son:\n1.Peperoni\n2.Jamón\nSalmon\nSolo puede elegir un ingrediente!!!')
    ingredientesn=int(input('Escriba el numero del ingrediente que le quiere agregar a su pizza: '))
    if ingredientesn==1:
        print('Su pizza consta de Peperoni, mozzarella y tomate!!')
    elif ingredientesn==2:
        print('Su pizza consta de Jamón ,mozzarella y tomate!!')
    elif ingredientesn==3:
        print('Su pizza consta de Salmon, mozzarella y tomate!!')
    else:
        print('El valor que ingreso no corresponde a un valor del menú')