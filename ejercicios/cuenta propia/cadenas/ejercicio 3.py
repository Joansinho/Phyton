#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por
# pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen
# el nombre.

nombre = input("Escriba su nombre: ")

mayusculas = nombre.upper()
número = len(mayusculas)

print(f"Su nombre es {mayusculas} y contiene {número} de letras")
