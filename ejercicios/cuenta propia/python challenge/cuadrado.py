a = int(input("Ingresa la longitud del lado a en cm: "))

area = a * a
perimetro = a * 4
print(f"el area del cuadrado es de {area}cm². el perimetro es de {perimetro}cm")

#con funciones. parametros
def area(lado):
    print(lado * lado)

area(5)
