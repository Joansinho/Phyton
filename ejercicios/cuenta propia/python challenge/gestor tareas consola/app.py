import funciones #as fn -> nos referimos al modulo como fn

#menu de usuario----
#-----titulo de aplicacion
#-----añadir tareas
#-----ver tareas
#-----completar tarea
#-----eliminar tarea
#-----salir del programa


#bucle principal
while True: 
    #menu de aplicaciones
    print("\n ----- Gestor de tareas -----\n")
    print("\n  1. Añadir tarea")
    print("\n  2. Ver tareas")
    print("\n  3. Completar tarea")
    print("\n  4. Eliminar tarea")
    print("\n  5. Salir\n")

    #Entrada de usuario 
    opcion = input("Introduzca la opcion que desee: ")
    

    match opcion:
        case "1":
            funciones.añadir_tarea(input)
        case "2":
            print("Estas son las tareas: ")
        case "3": 
            tarea_completada = input("Selecciona la tarea a completar: ")
        case "4":
            tarea_eliminada = input("Selecciona la tarea a eliminar: ")
        case "5":
            print("Gracias por usar. Saliendo del programa...")
            break
        case _:
            print("Opción invalida.")