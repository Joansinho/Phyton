#range(). repite el bucle el numero de veces indicada. recordar que el valor inicial es 0
print("range")
for i in range(5):
    print(i)

#inicio y parada con range(inicio, parada)
print("incio parada")
for i in range(4, 10):
    print(i)

#cambio de incremento con range(inicio, parada, incremento). los saltos que hará el bucle
print("incremento")
for i in range(2, 10, 2):
    print(i)

#decrementos con range(inicio, parada, decremento). se definen con el -. disminuyen numeros
print("decrementos")
for i in range(2, -10, -2):
    print(i)

#iteracion listas y tuplas con bucles. 
print("iteracion de lista")

colores = ["rojo", "azul", "verde", "amarillo"]
print("los colores son:")

for i in colores:
    print(f"el color es: {i}")

#omitir iteraciones con continue. Condicionales en bucles.
print("omitiendo iteracion")

colores = ["rojo", "azul", "verde", "amarillo"]
print("los colores son:")

for i in colores:
    if i == "rojo":
        print("el color rojo ha sido omitido")
        continue
    print(f"el color es: {i}")

#terminando bucle con break. finaliza el bucle antes de tiempo
print("terminando bucle con break")
for i in colores:
    if i == "verde":
        print("termino el bucle")
        break
    print(f"el color es: {i}")

#bucle while.
#incremento while
print("incremento")
i = 1
while i < 5:
    i += 1
    print(f"valor: {i}")

#decremento while
print("decremento")
i = 1
while i >= -5:
    print(f"valor: {i}")
    i -= 1

#finalizar un bucle while manualmente
while True:
    salir = input("introdzuca 'salir' para finalizar. \n").lower()
    if salir == 'salir':
        break
    

