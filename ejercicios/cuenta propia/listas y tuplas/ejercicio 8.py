#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
palabra = input("ingrese su palabra: ")
letras = []

for letra in palabra:
    letras.append(letra)

letras_invertida = letras[::-1]

if letras == letras_invertida:
    print("es palindroma")
else: 
    print("no es palindroma")

