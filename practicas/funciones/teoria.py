#las funciones son bloques de codigo que se pueden llamar cada vez que lo necesitemos. reutilizamos codigo de manera practica.

#sintaxis funciones
def nombre_de_la_funcion(opcionalmente_parametros):
    #codigo de la funcion
    return #solo si se deben devolver valores

#ejemplo de funcion
def saludar():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola {nombre}")

#llamando la funcion
saludar()

#parametros de funciones. son datos que podemos introducir en las funciones
def saludar(nombre):
    print(f"Hola {nombre}")

saludar("Joan")

#funcion con varios parametros. Si ponemos varios parametros al llamar la funcion estos DEBEN coincidir con cada uno de los mismos
def saludar(nombre, edad): #parametros
    print(f"Hola {nombre}, tu edad es de {edad}")

saludar("Joan", 17) #argumentos posicionales. coinciden con la posicion de los parametros 

#arguentos de clave. no requiere orden posicional
saludar(nombre="papu", edad=17)

#funcion return. devuelve resultados al programa para poder utilizarlo
def suma(n1, n2):
    return n1 + n2

resultado = suma(10,50) #aca estamos guardando el valor para usar el valor en cualquier momento 
print(resultado)

#funciones predefinidas. serie de funciones integradas en python
        #todas las funciones: docs.python.org/3/library/functions.html

