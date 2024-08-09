#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.
palabra = input("Ingrese su palabra: ")
letras = []
vocales = ["a", "e", "i", "o", "u"]

for letra in palabra:
    letras.append(letra)

for vocal in vocales:
    conteo = letras.count(vocal)
    print(f"Tu palabra tiene {conteo} letras de la vocal {vocal}")


