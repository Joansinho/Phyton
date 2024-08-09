#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida
#empezando por la última.

palabra = reversed(input("Introduzca una palabra: "))

for i in palabra: 
    print(i, end="")

#alternativa

word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])