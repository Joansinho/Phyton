# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo 
# del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra
# del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

nombre = input("Introduzca su nombre: ")

minusculas = nombre.lower()
mayusculas = nombre.upper()
capatalize = nombre.capitalize()

print(f"Su nombre es {nombre}" + "\n" + f"En minisculas es {minusculas}" + "\n" + f"En mayusculas es {mayusculas}" + "\n" + f"Capitalizado es {capatalize}" )