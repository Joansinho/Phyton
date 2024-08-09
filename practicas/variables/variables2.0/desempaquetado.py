# es una técnica para asignar valores avariables
#de esta manera se desempaquetan variables
#el desempaquetado solo funciona si el numero de variables que se quieren asignar es igual al numero de datos asignados. En este caso asignados a la tupla

datos = ("Joan", "Fontecha") #esto es una tupla. Funciona tambien con listas, y conjuntos

nombre, apellido = datos #asi se crean variables nuevas a partir de lo que hay dentro de la tupla

print(nombre, apellido) #mostrará que nombre es Joan y apellido es Fontecha
