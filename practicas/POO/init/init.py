#metodo de phyton que se puede incluir en clases. Se incluye en todas las clases creadas. No es llamado explicitamente. 
#Este metodo constructor se puede dar un estado inicial a un objeto
#Mejora el proceso de construccion de los objetos


#Atributos de clase. Estan en el codigo de la clase, dan un mismo valor a todos los objetos instanciados
class Clase:
    atributo1 = "valor"


#Atributos de instancias. Pueden ser diferentes en cada objeto. Se hace con el metodo init 
class Clase: 
    def __init__(self, valor1, valor2, valor3, valoretc): #dentro de los parentesis van los parametros
        self.valor1 = valor1 
        self.valor2 = valor2
        self.valor3 = valor3
        self.valoretc = valoretc

    def masmetodos():
        pass


objeto = Clase("contenido de valor1", "contenido de valor2", "contenido de valor3", "contenido de otros valores")


#el metodo init obliga a inicializar un objeto con todos los parametros del mismo.