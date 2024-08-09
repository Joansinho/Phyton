#lambda es una forma de crear una funcion anonima
multiplicar_por_dos = lambda x : x*2

print(multiplicar_por_dos(23))

#se usan cuando se hace algo sencillo. retornan automaticamente. No son aptas cuando hay que dar mas de una instruccion

#creando funcion que diga si un numero es par o no
numeros = [1,354,43,12,65,72,78]
numeros_pares = filter(lambda numero:numero%2==0, numeros)
print(list(numeros_pares))