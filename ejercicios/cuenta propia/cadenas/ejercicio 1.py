# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas
# el nombre del usuario tantas veces como el número introducido.

nombre = input("Escriba su nombre: ")
cantidad = int(input("Escriba el numero de veces: "))

print((nombre + "\n")* cantidad)