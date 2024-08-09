#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
#pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe
#mostrar por pantalla las asignaturas que el usuario tiene que repetir.

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
reprovadas = []

for i in asignaturas:
    nota = int(input(f"Ingrese la nota que ha sacado en {i}: "))
    if nota < 5:
        reprovadas.append(i)

print("Las materias que debes repetir son: ")
for i in reprovadas:
    print(i, end="\n")