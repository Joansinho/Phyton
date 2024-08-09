diccionario = {
    "nombre" : "Joan",
    "apellido" : "Fontecha",
    "edad" : 17
}

clave = diccionario.keys() #devuelve las claves y tambien sirve para iterar
get = diccionario.get("edad") #devuelve el valor de las claves
clear = diccionario.clear() #elimina todo lo del diccionario
pop = diccionario.pop("nombre", "edad") #elimina un elemento del diccionario
items = diccionario.items() #itera elementos, dict_items

#comprobando el valor de una clave 
print(diccionario["edad"])

#modificando el valor de una clave
diccionario["edad"] = 20

#creando un nuevo elemento en el diccionario
diccionario["correo"] = "joaaan.fontechaa@ajaj.com"

#eliminando una clave y su valor asociado
del diccionario["correo"]

#eliminando un diccionario entero. el operador puede eliminar mas cosas que los diccionarios.
del diccionario