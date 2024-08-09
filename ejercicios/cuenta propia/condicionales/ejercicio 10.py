#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a
#continuación.
#
#    Ingredientes vegetarianos: Pimiento y tofu.
#    Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con
#los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas
#la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

vegetariana = "pimiento", "tofu"
no_vegetariana = "peperoni", "jamon", "salmon"

pizza = input("Que tipo de pizza desea? Vegetariana o no vegetariana: ")

if pizza.lower() == "vegetariana":
    print(f"Los ingredientes vegetarianos son: {vegetariana}")
elif pizza.lower() == "no vegetariana":
    print(f"Los ingredientes no vegetarianos son: {no_vegetariana}" )
else: 
    print("Respuesta no valida")
    exit()

pizza = input("Escoge un ingrediente (solo puedes escoger uno): ")

if pizza.lower() == "pimiento":
    print("tu pizza vegetariana llevará mozarella, tomate y pimiento")
elif pizza.lower() == "tofu":
    print("tu pizza vegetariana llevará mozarella, tomate y tofu")
elif pizza.lower() == "peperoni":
    print("tu pizza no vegetariana llevará mozarella, tomate y peperoni")
elif pizza.lower() == "jamon": 
    print("tu pizza no vegetariana llevará mozarella, tomate y jamon")
elif pizza.lower() == "salmon":
    print("tu pizza no vegetariana llevará mozarella, tomate y salmon")
else:
    print("No has escogido una opcion valida")
    exit()