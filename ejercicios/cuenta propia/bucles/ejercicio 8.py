#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1

num = int(input("Ingrese su numero: "))

for i in range(1, num, 2):
    for j in range(i, -1, -2):
        print(j, end=" ")
    print("")