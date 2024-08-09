#los sets son inmutables y estan definidos literalmente. Todos los objetos inmutables se pueden usar en los sets. Los sets no pueden 
#tener valores repetidos
_set = {"hola", "adios", ":v"}

#los sets no tienen indice. sus elementos se almacenan de forma aleatoria

#añadiendo un objeto a set con add
_set.add("penesin")

#eliminando valores en un set con remove. se especifica literalmente el valor que queramos eliminar. da error si intentamos eliminar un 
#elemento inexistente
_set.remove(":v")

#discar. elimina tambien un elemento en el set pero si no encuentra el elemento ignora la accion. no suelta error
_set.discard("ajaja")
