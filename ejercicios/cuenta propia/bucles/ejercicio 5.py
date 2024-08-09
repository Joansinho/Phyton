#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital
#obtenido en la inversión cada año que dura la inversión.

cantidad = int(input("Ingrese la cantidad a invertir: "))
a_interes = int(input("Ingrese el interes porcentual anual: "))
a = int(input("Años de la inversion: "))

interes = (a_interes / 100) +1

for i in range(a+1):
    capital = round(cantidad * interes ** i,)
    print(f"la inversion en el año {i} es de {capital}")