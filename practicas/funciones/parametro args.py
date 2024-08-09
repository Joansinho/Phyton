#args (*numeros) esto lo que hace es tomar todos los numeros o datos que le estamos dando como si fuera una lista para despues sumarlos. es importante saber que es el unico parametro que se puede usar. si despues se quiere usar otro parametro despues de args no se ejecutará, lo optimo ponerlo siempre de ultimas
def suma(*numeros):
    return sum(numeros)

resultado = suma(2,4,2,3,6)
print(resultado)