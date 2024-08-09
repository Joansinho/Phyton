# logico añadir tareas, ver tareas, completar tareas, eliminar tareas. 

tareas = []

def añadir_tarea(tarea):
    tarea = input("\n Añade una tarea: ")
    tareas.append(tarea)
    
    print("\n")
    
    print("\n ----- Tarea añadida! -----\n")
    print(" Estas son las tareas: ")
    
    for i in tareas:
        print(" =>", i, end="\n")
    
    print("\n --------------------------\n")
    
    añadir = input(" Desea añadir otra tarea? y/n\n")
    
    if añadir == "y":
        añadir_tarea(input)
    elif añadir == "n":
        print("\n Gracias por usar el software. Hasta luego!")
    else: 
        print("\n Ingreso invalido.")

