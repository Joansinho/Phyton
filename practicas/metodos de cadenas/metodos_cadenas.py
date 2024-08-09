#metodos que se pueden aplicar a las cadenas para ser operadas

cadena1 = "hola soy joan"
cadena2 = "penesin"

#los metodos se definen de esta manera:

#metodos que convierten el valor
mayusculas = cadena1.upper() #upper convierte todo a mayuscula, dentro del parentesis se usan parametros
minusculas = cadena1.lower() #convierte todo a miniscula
capitalizar = cadena1.capitalize() #convierte la primer letra de cada oracion en mayuscula

#metodos que buscan un valor
buscar_find = cadena1.find("hola")  #retorna la posicion en la que se encuentra el dato (recordar q se cuenta desde 0, devuelve -1 cuando no se encuentra el valor)
buscar_index = cadena1.index("a") #la diferencia con index es q cuando no encuentra algo da un error/excepciones

#metodos que consultan
isnumeric = cadena1.isnumeric() #si es numerico devuelve true, de lo contrario devuelve false
alfanumeric = cadena1.isalpha() #si es alfanumerico devuelve true, de lo contrario false, caracteres de la A-Z (los espacios cuentan, si hay soltará false)

count = cadena1.count() #devuelve la cantidad de veces q se coincide el valor, si no se encuentra regresa 0
contar_caracteres = len(cadena1) #len es función, cuanta cuantos caracteres tiene una cadena

startswith = cadena1.startswith() #verifica si una cadena empieza con otra cadena, si es asi devuelve true, de lo contrario False
endswith = cadena1.endswith() #lo mismo que starts pero termina con

replace = cadena1.replace("hola", "pene") #reemplaza un pedazo de la cadena dada por otra, el primer parametro es el parametro antiguo, el segundo es el nuevo con el que queremos reemplazar, si no encuentra una coincidencia devuelve el anterior parametro

split = cadena1.split(" ") #separa cadenas, con la q se le entregue, en este caso entregara una lista con las palabras separadas con espacio.


print(split)