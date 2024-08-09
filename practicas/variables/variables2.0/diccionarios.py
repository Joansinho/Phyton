#creando diccionarios con dict()

diccionario = dict(nombre="Joan", apellido="Fontecha") #esta es la estructura para crear el diccionario con dict

#las tuplas pueden ser claves, pero las listas no, ni los conjuntos. Con frozenset si se puede.

diccionario = {("joan", "fontecha"):"hola"}

#cracion de diccionario con frokeys. Funcion que permite crear un diccionario con todos los valores en None (ninguno, sin asignar)
diccionario = dict.fromkeys(["nombre", "apellido"], "no se") #es un iterable. Si ponemos algun valor fuera de las llaves cambiaremos el valor por defecto de none al valor que asignamos
