#funcion max/min (encuentra el numero mayor/menor). Funciona para todo tipos iterables
numeros = [3, 2, 4, 11, 98, 323, 1]

numero_mas_alto = max(numeros) #tambien se puede poner min y encontrará el numero menor
print(numero_mas_alto)

#round nos permite elegir cuantos decimales habrán en un float

numerote = 23191.1781283123
numero = round(12.448941, 2) #despues de la coma dejaremos la cantidad de decimales que queremos que queden, tambien se puede poniendo variables en el round "round(numerote, 12)"
print(numero)

#bool retorna false si le damos un numero vacio o 0. en caso contrario devuelve true
resultado = bool(0)

#sum. suma todos los numeros dentro de la lista
suma_total = sum(numeros)