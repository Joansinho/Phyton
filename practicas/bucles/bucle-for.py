#los bucles son una de estas sentencias que permiten iterar elementos
#un elemento iterable es un elemento que tiene un iterador el cual define de que manera se va a iterar, un elemento es iterable cuando tiene algo que define como se va a iterar. En si iterar es recorrer un elemento por partes

#bucle FOR (permite crear una iteracion)

#iterando una lista. funciona para tuplas y conjuntos
#un bucle recorre algo hasta acabarlo, en este caso una lista

animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [1, 36, 34, 73]

for animal in animales:
    print(f"ahora la variable animal es igual a: {animal}")
    
for numero in numeros: 
    resultado = numero * 10
    print(resultado)

#funcion zip
for numero, animal in zip(animales, numeros): #la funcion zip nos permite recorrer las listas que queramos al mismo tiempo. En este caso son dos y cada una esta separada por coma
    print(f"recorriendo lista 1:{numero}")
    print(f"recorriendo lista 2:{animal}")

#funcion range
for num in range(5,10): #ejecuta numero del 5 al 10. Para eso funciona la funcion Range. Si solo definimos un numero irá desde el cero hasta el numero definido
    print(num)

#funcion enumerate. recorre una lista con su indice
for num in enumerate(numeros):
    print(num)
    
#usando else en el for
for numero in numeros:
    print("ejecutando el ultimo bucle, valor actual: {numero}")
else: print("el bucle terminó") #else siempre se va a ejecutar independientemente de si hay elementos en la lista o no