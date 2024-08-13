#todos los metodos llevan un primer parametro obligatorio (self). Siempre está en la primera posición, tanto en el init como 
#en los metodos. Sin self los metodos de una clase no tienen forma de saber a que instancia de la clase se aplican. Automatiza
#y simplifica las inicializaciones. No es una palabra reservada, se le puede dar cualquier nombre. Es una convencion

class Clase: 
    def __init__(self, valor1, valor2, valor3, valoretc): #dentro de los parentesis van los parametros
        self.valor1 = valor1 
        self.valor2 = valor2
        self.valor3 = valor3
        self.valoretc = valoretc

    def masmetodos(self):
        print(f"{self.valor1}") 

