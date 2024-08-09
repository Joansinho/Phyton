class Estudiante:
    def __init__(self, nombre, nota1, nota2):
        self.__nombre = nombre
        self.__nota1 = None
        self.__nota2 = None
        self.set_nota1(nota1)
        self.set_nota2(nota2)

    def obtener_nota_promedio(self):
        return (self.__nota1 + self.__nota2) / 2

    def mostrar_informacion(self):
        promedio = self.obtener_nota_promedio()
        print(f"Nombre: {self.__nombre}")
        print(f"Nota 1: {self.__nota1}")
        print(f"Nota 2: {self.__nota2}")
        print(f"Promedio: {promedio}")

    def get_nombre(self):
        return self.__nombre

    def get_nota1(self):
        return self.__nota1

    def get_nota2(self):
        return self.__nota2

    def set_nota1(self, nota):
        if 0 <= nota <= 5:
            self.__nota1 = nota
        else:
            raise ValueError("La nota debe estar entre 0 y 5")

    def set_nota2(self, nota):
        if 0 <= nota <= 5:
            self.__nota2 = nota
        else:
            raise ValueError("La nota debe estar entre 0 y 5")

    def __str__(self):
        promedio = self.obtener_nota_promedio()
        return f"Nombre: {self.__nombre}, Promedio: {promedio:.2f}"

# Prueba de la clase
try:
    estudiante1 = Estudiante("Ana", 4.5, 4.8)
    print(estudiante1)  # Usando el método __str__

    estudiante2 = Estudiante("Juan", 3.7, 2.9)
    print(estudiante2)  # Usando el método __str__
    
    # Intentar establecer una nota inválida para probar la validación
    estudiante3 = Estudiante("Luis", 6, 4)
except ValueError as ve:
    print(ve)

try:
    estudiante4 = Estudiante("María", 4, 5)
    estudiante4.set_nota1(6)  # Esto debería lanzar una excepción
except ValueError as ve:
    print(ve)
