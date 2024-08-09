#metodos que se pueden aplicar a listas para operarlas

#de esta manera se crea una lista con list (no se suele hacer)
lista = list(["hola", "soy", "joan", 23]) #ponemos las llaves ya que esta es la manera de declarar una lista

len = len(lista) #en este caso len devuelve la cantidad de elementos de la lista

#todos estos no se imprimen con la variable directamente, ya q agrega/elimina contenido a la lista. Por eso no hay variables antes de los metodos.
lista.append(":v")#agrega elementos a la lista
lista.insert(2, "holota") #tambien agrega un elemento a la lista pero en un indice especifico. Primero va el indice y despues lo que agregaremos
lista.extend([1, 3, "hola"]) #agrega varios elementos a la lista. se pone adentro de las llaves.

lista.pop(-1) #elimina elementos por medio del indice, cuando ponemos -1 elimina el ultimo elemento de la lista, si ponemos -2, elimina el penultimo y asi sucesivamente
lista.remove(":v") #remueve elementos de la lista por su valor
lista.clear() #elimina todos los elementos de la lista


lista.sort(reverse=True) #ordena los objetos de forma ascendente, solo funciona con caracteres numericos. Cuando le decimos reverse=True ordena de forma descendente. Este metodo tambien puede ordenar False y True. False yendo primero que cualquier otro caracter, y true seguido de False

lista.reverse() #invierte los elementos de una lista (no es lo mismo que el reverse del sort ya que si no organizamos la lista antes va a invertirlos de igual forma)



