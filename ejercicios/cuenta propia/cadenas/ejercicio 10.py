#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla 
#cada uno de los productos en una línea distinta.

productos = input("Ingrese los productos separados con coma: ")

separador = productos.replace(",", "\n")
lista = separador.replace(" ", "")

print("la lista con tus productos es: \n", lista)