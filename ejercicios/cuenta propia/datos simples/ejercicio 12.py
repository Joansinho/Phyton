#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar 
# el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

barras = int(input("Ingrese la cantidad de barras que no son del dia: "))
pan = 3.49
descuento = 0.6

coste = round(barras * pan * (1 - descuento), 2)

print(f"el precio habitual es {pan}€ el descuento es de 60% y el coste final es de {coste}€")
