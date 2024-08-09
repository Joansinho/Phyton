#creando conjuntos con set
conjunto = set(["dato1", "dato2"])

#conjunto dentro de otro conjunto

conjunto1 = frozenset(["dato1" , "dato2"]) #se usa la funcion frozenset. Significa conjunto congelado. El conjunto es inmutable y hashable
conjunto2 = {conjunto1, "dato3", "dato4"}


#teoria de conjuntos 

conjunto1 = {1,3,5,7,9,11}
conjunto2 = {1,3,7}

resultado = conjunto2.issubset(conjunto1) #el metodo devuelve si conjunto 2 es subconjunto, tambien el metodo puede ser <= es otra manera de verificarlo
resultado = conjunto1.issuperset(conjunto2) #es lo mismo pero con los superconjuntos tambien puede ser >=
resultado = conjunto2.isdisjoint(conjunto1) #muestra true solamente cuando no hay ningun numero en comun dentro del conjunto, de lo contrario será false
print(conjunto2) 