# almacenan informacion util. En las variables se almacenan datos simples o complejos.

nombre = "Joan" # las variables se declaran y se definen. "nombre" es la declaracion y "Joan" es la definicion. las variables son modificables
nombre = "Pedrito" #acá se modifico la variable




numero = 3 
numero += 2 # el mas antes del igual indican que el numero se sumará a la anterior variable de mismo tipo tambien se puede poner -

print(numero)

# concatenar es unir dos cosas sin sumarlas. 

nombre = "Joan"
bienvenido = "Hola " + nombre + " como estas?" # es importante tener en cuenta que el espacio es un caracter
print(bienvenido)

# cuando son números es diferente

nombre = 5
bienvenido = f"Hola {nombre} como estas?" # f strings. nos sirve para poner variables, se pone la f al inicio. Convierte todo a texto
print(bienvenido)

# operadores de pertenencia o identidad

hola = "Joan ta loco"
print("loco" in hola) # esto comprobara si "loco" esta en hola, en caso de que no mostrará False
print("papu" not in hola) # tambien puede comprobar si algo no está


#camelCase. es definir una variable con más de dos palabras sin poner espacios. se usa en java

nombreCompleto = "Joan Fontecha"


#snake_case. Es usado en Phyton. Tambien definimos varaibles de mas de dos palabras

nombre_completo = "Joan Fontecha"
