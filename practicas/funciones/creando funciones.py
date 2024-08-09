#def. le decimos al programa que vamos a crear nuestras propias funciones, seguido del nombre de la funcion


#funcion simple
def saludo():
    print("hola joan q ta chendo")
    
saludo() #si ponemos asi la funcion se va a ejecutar 

#funcion con parametro (variable)
def saludar(nombre, sexo):
    sexo = sexo.lower()
    
    if(sexo== "mujer"): 
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "maestro"
    else:
        adjetivo = 'lo que seas'
    
    print(f"hola {nombre}, mi {adjetivo} como estás?")
    
saludar("Joan", "hombre") #lo que pongamos dentro va a ser la variable modificada. En este caso nombre pasará a ser Joan

#funcion que retorna valores 
def contraseña_randi(num):
    listado_caracteres = "abcdefghij"
    numero_entero = str(num)
    num = int(numero_entero[0]) 
    c1 = num - 2
    c2 = num 
    c3 = num - 5
    contraseña = f"{listado_caracteres[c1]} {listado_caracteres[c2]}{listado_caracteres[c3]}{num * 2}"
    return contraseña #retorna variables o cosas xd
    
contraseña_randi(98)