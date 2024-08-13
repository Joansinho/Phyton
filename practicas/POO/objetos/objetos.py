#elementos creados a partir de una clase, tienen los atributos y metodos de la clase a la que pertenecen, pero pueden tener 
#algunos propios

class Clase():
    atributo1 = "valor1"
    atributo2 = "valor2"
    
    def metodo1(self):
        print("metodo1 de clase")
    def metodo2(self):
        print("metodo2 de clase")


#instanciando un objeto
objeto = Clase()


#llamada al metodo
objeto.metodo1()


#se pueden crear cualquier cantidad de objetos para una clase


#accediendo al atributo de un objeto
objeto.atributo1


#almacenando externamente valores de los objetos
valor = objeto.atributo1


#reasignando valores a atributos de un objeto
objeto.atributo1 = "valor a asignar"


#crear atributos inexistentes en la clase (solo para un objeto)
objeto.atributo_nuevo = "valor del atributo"

#los atributos inexistentes tienden a la equivocación por parte del programador. Es más sencillo crear los atributos para la clase.
