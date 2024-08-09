#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
#Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad = int(input("Escriba su edad: "))
ingresos = int(input("Escriba sus ingresos mensuales: "))

if edad < 16 and ingresos > 1000:
    print("Aun no cumple con la edad necesaria para tributar.")
elif edad > 16 and ingresos < 1000:
    print("Cumple con la edad para tributar pero no con los ingresos.")
else:
    print("Ya tiene que tributar")
