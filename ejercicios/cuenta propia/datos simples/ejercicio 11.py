#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
# Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario.
# Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear
# cada cantidad a dos decimales.

dinero = int(input("Ingrese la cantidad de dinero: "))
interes = 1 + 4 / 100

año1 = round(dinero *( interes ** 1), 2)
año2 = round(dinero *( interes ** 2), 2)
año3 = round(dinero *(interes ** 3), 2)

print (f"la cantidad al primer año sera de {año1}, en el segundo de {año2} y en el tercer año de {año3}")