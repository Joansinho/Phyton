# los datos compuestos son varios datos simples juntos.

# Lista. [] Agrupa datos

lista = ["Carro", "Moto", 20, 1.2]
tupla = ("Carro", "Moto", 20, 1.2) #las tuplas no se pueden modificar como las otras variables
print(lista[2])  #aqui le estamos pidiendo el dato 2. En realidad nos esta dando el tercer elemento ya que se cuenta desde 0


#conjuto (set)

lista = {"Carro", "Moto", 20, 1.2} # no tienen orden y pueden cambiar, son parecidas a la lista. No se pueden modificar los elementos. Y no se puede acceder a un indice en especial, no permite repetir elementos. son datos desordenados

# diccionario. No tienen orden. Clave : Valor. Se separa con comas
diccionario = {
    'nombre' : "Joan",
    'apellido' : "Fontecha",
    'edad' : 17
}

print(diccionario['nombre'])