def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError(f"Error: Imposible añadir elementos duplicados => {el}.")
        else:
            lista.append(el)
            print(f"Elemento {el} añadido correctamente.")
    except ValueError as ve:
        print(ve)
    finally:
        print("Gracias por usar este programa.")


mi_lista = [1, 2, 3]

# Caso donde el elemento no está en la lista
agregar_una_vez(mi_lista, 4)
print(mi_lista)

# Caso donde el elemento ya está en la lista
agregar_una_vez(mi_lista, 2)
print(mi_lista)
