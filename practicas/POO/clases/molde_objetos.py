#creando una clase que tenga sentido. Un vehiculo.

class Vehiculo():
    #atributos
    color = None #indica que no tiene un valor asignado, para que no haya un error de inicialización
    longitud = None
    ruedas = 4
    
    #metodos
    def arrancar(self):
        print("Se ha arrancado el motor.")
    
    def detener(self):
        print("Se ha apagado el motor.")