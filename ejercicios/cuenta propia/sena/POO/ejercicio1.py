class Estudiante:
    def __init__(self, nombre, nota1, nota2):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2

    def obtener_nota_promedio(self):
        return (self.nota1 + self.nota2) / 2

    def mostrar_informacion(self):
        promedio = self.obtener_nota_promedio()
        print(f"Nombre: {self.nombre}")
        print(f"Nota 1: {self.nota1}")
        print(f"Nota 2: {self.nota2}")
        print(f"Promedio: {promedio}")

#Prueba
estudiante1 = Estudiante("Ana", 5, 3)
estudiante1.mostrar_informacion()

estudiante2 = Estudiante("Juan", 2, 4)
estudiante2.mostrar_informacion()
