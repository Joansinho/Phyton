#Las herencias de clases permiten tener funcionalidades permitiendo reutiliar codigo.
#Clase base/padre/madre/superclase = Clase principal, en este caso ciudadano
#Clase derivada/hijo/hija/subclase = la clase que hereda, en este caso medico.


#Ejemplo. Esta clase crea ciudadanos generales para despues generar ciudadanos mas especificos
class Ciudadano:
    def __init__(self, nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion
    def saludar(self):
        print(f"Hola soy {self.nombre}. Mi profesion es {self.profesion}")


#creacion ciudadano especifico (estamos repitiendo mucho codigo)
class Medico: 
    def __init__(self, nombre):
        self.nombre = nombre
        self.profesion = "medico" #nos ahorramos especificar la profesion

    def saludar(self):
        print(f"Hola soy {self.nombre}. Mi profesion es {self.profesion}")


#Creando una clase con herencia de clases. Se hereda todo de la clase padre
class Policia(Ciudadano): #entre los parentesis indicamos de que clase queremos heredar
    def __init__(self, nombre):
        super().__init__(nombre, "Policia") #con esta funcion podemos utilizar/acceder partes especificas de la clase padre, indicamos lo que irá por defecto

    def pedir_refuerzos(self):
        print("A todas las unidades, solicito refuerzos.") #lo ideal es que cada subclase tenga comportamientos diferentes/unicos

    #sobre escribiendo un metodo
    def saludar(self):
        print("hola papus soy policia ajajaj")

#instanciando objetos
a = Ciudadano("Joan", "Developer")
b = Medico("Andres")
c = Policia("Papu")

#usando los metodos
a.saludar()
b.saludar()
c.saludar()

c.pedir_refuerzos()

#tipos de herencia: Simple/unica, multiple, multinivel, jerarquica e hibrida.

#herencia simple. Proviene de una unica clase padre
class A(object):
    pass

class B(A):
    pass

#herencia multiple. Una clase que recibe herencia de multiples clases
class C(object):
    pass

class D(object):
    pass

class E(object):
    pass

class F(C, D, E):
    pass


#herencia multinivel. Herencia que hereda de otras herencias.
class G(object):
    pass

class H(G):
    pass

class I(H):
    pass

class J(I):
    pass

#MRO. METHOD RESOLUTION ORDER, orden de resolucion de metodos.
print(A.mro()) #permite observar las herencias


#herencia jerarquica. Mas de una subclase que hereda de una clase padre
class K(object):
    pass

class L(K):
    pass

class M(K):
    pass

class N(K):
    pass


#herencia hibrida. se mezclan varias heredaciones en una. (pendiente cap 118)