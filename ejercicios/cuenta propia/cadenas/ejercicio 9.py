#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes 
# y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

nacimiento = input("Ingrese su fecha de nacimiento con el siguiente formato dd/mm/aaaa: ")

dia = nacimiento[:nacimiento.find('/')]
mes = nacimiento[nacimiento.find('/')+1:-5]
año = nacimiento[-4:]

print(f"tu dia de nacimiento es {dia}, el mes es {mes} y el año es {año}")