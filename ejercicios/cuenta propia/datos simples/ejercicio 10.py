# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística
# les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda.
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido
# y calcule el peso total del paquete que será enviado.

payasos = int(input("Indique la cantidad de payasos vendidos: "))
muñecas = int(input("Indique la cantidad de muñecas vendidas: "))

peso_payasos = payasos * 112
peso_muñecas = muñecas * 75

gramos = peso_muñecas + peso_payasos 
peso_total = gramos / 1000

print(f"El peso del pedido es de {gramos}g o {peso_total}kg")