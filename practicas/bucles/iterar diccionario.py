
diccionario = {
    "nombre": 'Joan',
    "apellido": "Fontecha",
    "edad": "17"
}

#para recorrer un diccionario se hace de la siguiente forma 
for key in diccionario: 
    print(key) #asi solo mostrara las keys
    
#para mostrar los value se hace asi:
for key in diccionario.items(): #asi muestra las keys y values
    print(key)

#-----------------------------------------
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")