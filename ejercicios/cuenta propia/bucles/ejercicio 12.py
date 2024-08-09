#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la 
#letra en la frase.

frase = input("Ingrese su frase: ")
letra = input("Ingrese su letra: ")

contador = frase.count(letra)
print(f"El numero de veces que se repite la letra es de: {contador}")

#alternativa con bucles (no supe hacerlo)
frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))