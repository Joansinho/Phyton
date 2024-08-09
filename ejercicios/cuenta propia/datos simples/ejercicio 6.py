#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros
# desde 1 hasta N La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

num = int(input("introduzca un numero entero: "))
suma = num * (num + 1) / 2

print(f"La suma de los primeros numeros enteros desde 1 hasta {num} es {suma}")