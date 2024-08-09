#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

while True:
    oracion = input("Introduzca su palabra. Si desea salir escriba 'salir': ").lower()
    if oracion != 'salir':
        print(oracion)
    else:
        print("Ha finalizado la operacion.")
        break

#alternativa 
while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)