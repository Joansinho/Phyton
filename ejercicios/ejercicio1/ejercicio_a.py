#cuando vamos a desarrollar ejercicios de este tipo lo primero que debemos hacer es anotar los datos.

#duraciones/promedios cursos X
cursos_x_min = 2.5
cursos_x_max = 7
cursos_x_promedio = 4

#duraciones/promedios dalto
dalto_curso = 1.5

#promedio de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#diferencias de duración con el curso X más rápido

diferencia_con_min = 100 - dalto_curso / cursos_x_min * 100 #con esta formula sacamos la diferencia que hay con los otros cursos
diferencia_con_max = 100 - dalto_curso * 1000 // cursos_x_max / 10 #si no lo hacemos de esta forma nos dará demasiados decimales. El *1000 es para que nos de más decimales, sirve para mover la coma. el 1000 mueve la coma una vez. 10000 dos veces y asi sucesivamente. si se aumenta el valor de la multiplicacion se debe aumentar un 0 en la division.
diferencia_con_promedio = 100 - dalto_curso / cursos_x_promedio * 100

#diferencias de crudos entre dalto y cursos X

tiempo_crudo = 100 - cursos_x_promedio * 1000 // crudo_promedio / 10
tiempo_crudo_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10



print("-" * 100) #separador

#(a) diferencias de duración
print(f"El curso de dalto dura un {diferencia_con_min}% menos que el más rápido, un {diferencia_con_max}% menos que el video más lento y un {diferencia_con_promedio}% menos que el promedio de duracion de los cursos X")

print("-" * 100) #separador

#(b) porcentaje de crudo
print(f"El crudo promedio de los cursos X fue de un {tiempo_crudo}% \nEl crudo de dalto fue de un {tiempo_crudo_dalto}%")

print("-" * 100) #separador

#(c) diferencias si los cursos duraran 10h 
print(f"ver 10 horas de el curso de dalto equivale a ver {cursos_x_promedio * 100 // dalto_curso / 10} horas en los cursos X")
print(f"ver 10 horas en los cursos X equivale a ver {dalto_curso * 100 // cursos_x_promedio / 10} horas en los otros cursos")

print("-" * 100) #separador