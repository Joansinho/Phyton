#Paquete graficos
from areas import *
from perimetros import *

#-----DATOS

#Cuadrado
print("\n----- CUADRADO -----")
lado = int(input("Ingrese los lados de el cuadrado: "))

#Rectangulo
print("\n----- RECTANGULO -----")
ancho = int(input("Ingrese el ancho del rectangulo: "))
alto = int(input("Ingrese el alto del rectangulo: "))

#Triangulo
print("\n----- TRIANGULO -----")
altura = int(input("Ingrese el alto del triangulo: "))

#Rombo
print("\n----- ROMBO -----")
diagonal = int(input("Ingrese la diagonal del rombo: "))



#-----INTERFACES

#Cuadrado
def dibujar_cuadrado(lado):
    for i in range(lado):
        for j in range(lado):
            print('°', end=' ')
        print()

#Rectangulo 
def dibujar_rectangulo(ancho, alto):
    for i in range(alto):
        for j in range(ancho):
            print('°', end=' ')
        print()

#Triangulo
def dibujar_triangulo(altura):
    for i in range(1, altura + 1):
        print('° ' * i)

#Rombo
def dibujar_rombo(diagonal):
    mitad = diagonal // 2
    for i in range(mitad):
        print(' ' * (mitad - i) + '° ' * (i + 1))
    for i in range(mitad, -1, -1):
        print(' ' * (mitad - i) + '° ' * (i + 1))

#PRINTS

#PRINT CUADRADO
print("\n----- Interfaz Cuadrado -----\n")
dibujar_cuadrado(altura)
print(f"\nEl area del cuadrado es de: {area_cuadrado(lado)}")
print(f"El perimetro del cuadrado es de: {perimetro_cuadrado(lado)}")

#PRINT RECTANGULO
print("\n----- Interfaz Rectangulo -----\n")
dibujar_rectangulo(ancho, alto)
print(f"\nEl area el rectangulo es de: {area_rectangulo(ancho, alto)}")
print(f"El perimetro del cuadrado es de: {perimetro_rectangulo(ancho, alto)}")

#PRINT TRIANGULO
print("\n----- Interfaz Triangulo -----\n")
dibujar_triangulo(altura)
print(f"\nEl area del triangulo es de: {area_triangulo(altura, altura)}")
print(f"El perimetro del triangulo es de: {perimetro_triangulo(altura)}")

#PRINT ROMBO
print("\n----- Interfaz Rombo -----\n")
dibujar_rombo(diagonal)
print(f"\nEl area del rombo es de: {area_rombo(diagonal, diagonal)}")
print(f"El perimetro del rombo es de: {perimetro_rombo(diagonal)}")