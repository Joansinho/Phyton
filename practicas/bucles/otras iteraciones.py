frutas = ["banano", "manzana", "ciruela", "pera", "naranja", "granadilla", "durazno"]
cadena = "penesin ejeje"
numeros = [2, 3, 4, 5]


#continue. Sigue recorriendo la lista pero evita el elemento
for fruta in frutas: 
    if fruta == "granadilla": 
        continue #continue saltea el elemento y no lo cuenta dentro del bucle
    print(f"me voy a comer una {fruta}")
    
#break. Para el bucle

for fruta in frutas: 
    if fruta == "manzana":
        break 
    print(f"me voy a comer una {fruta}")

print("terminó el bucle")

#iterando(recorriendo) una cadena de texto. se recorre caracter por caracter 

for letra in cadena: 
    print(letra)
    

#duplicando numeros en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)