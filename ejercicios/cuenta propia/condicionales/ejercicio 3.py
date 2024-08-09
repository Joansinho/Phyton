#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

n1 = int(input("Introduzca el primer numero: "))
n2 =  int(input("Introduzca el segundo numero: "))

division = n1 / n2 

if n2 == 0:
    print("Error")
else:
    print(division)
