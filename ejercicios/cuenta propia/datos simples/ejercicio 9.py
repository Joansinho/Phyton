#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
# y muestre por pantalla el capital obtenido en la inversión.

cantidad = int(input("Escriba la cantidad a invertir: "))
porcentaje_anual = int(input("Escriba el interes anual (porcentaje): "))
n_años = int(input("Escriba el numero de años de la inversion: "))

interes_anual = 1 + porcentaje_anual / 100

capital_total = round(cantidad * ( interes_anual ** n_años), 2)

print(f"La capital obtenida por la inversion es de: {capital_total}")