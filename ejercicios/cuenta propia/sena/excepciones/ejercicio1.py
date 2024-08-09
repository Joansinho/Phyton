lista = [3, 5, 6, 8]

while True:
    try:
        pos = int(input("Ingrese la posición del elemento que desea obtener: "))
        print(f"El valor en la posición {pos} es {lista[pos]}")
        break  # Rompe el bucle si la operación se realiza correctamente
    except ValueError:
        print("La posición ingresada no es válida. Por favor, ingrese un número entero.")
    except IndexError:
        print("La posición no existe. Por favor, ingrese una posición dentro del rango de la lista.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
