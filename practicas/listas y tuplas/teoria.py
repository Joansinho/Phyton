#imprimiendo una lista completa
lista = ["aasd", "b", "c", "d"]

print(lista)

#accediendo a un solo elemento de la lista
print(lista[0]) 

#accediendo a un caracter en especifico dentro de la lista
print(lista[0][2])

#posiciones negativas
print(lista[-1])

#reasingando valores a una lista
#se reemplaza "b" por "hola"
lista[1] = "hola"

#añadiendo valores (se añaden al final de la lista)
lista.append("jajaj")

#añadiendo valores con insert. controla la posicion especifica del elemento
lista.insert(-2, "SML")

#vaciando lista con clear
abc = [1, 2, 3, 4]

abc.clear()

#eliminando un solo elemento con pop
lista.pop(3)

#eliminando elemento con remove (indicas el valor especifico para remover)
lista.remove("jajaj")

#duplicando listas con copy. Copia el contenido de una lista a otra
abc = lista.copy()

#contando valores repetidos en listas con count
print(lista.count("a"))

#buscar la posicion de un elemento especificandolo con index (busca la primera ocurrencia)
print(lista.index("hola"))

#invirtiendo el orden de los elementos en una lista con reverse
lista.reverse()

#ordenando alfabeticamente ascendente los elementos de la lista con sort. Tambien ordena numeros de la misma forma que letras
lista.sort()
#descendente
lista.sort(reverse=True)

#uniendo listas con extend()
lista.extend(abc)

#contando cantidad de objetos en una lista con len
print(len(lista))

#podemos sustituir un elemento de una lista con su indice:
lista[0]= "azul"


#Tuplas. son parecidas a la listas. Las tuplas son inmutables (no se pueden cambiar)
