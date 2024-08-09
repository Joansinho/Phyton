#Sueldos
sueldo_gerente = 5_000_000
sueldo_x_hora_gerente = sueldo_gerente / 240

sueldo_subgerente = 4_000_000 
sueldo_x_hora_subgerente = sueldo_subgerente / 240

sueldo_secretaria = 2_000_000
sueldo_x_hora_secretaria = sueldo_secretaria / 240

sueldo_operario = 1_400_000
sueldo_x_hora_operario = sueldo_operario / 240

#Horas extra
hed = 1.25
hen = 1.75
hef = 2.25


#Calculo total sueldos
def sueldos(gerentes, subgerentes, secretarias, operarios):
    return (sueldo_gerente * gerentes) + (sueldo_subgerente * subgerentes) + (sueldo_secretaria * secretarias) + (sueldo_operario * operarios)

total_sueldos = sueldos(1, 2, 1, 3)
print("\n----- TOTAL SUELDOS -----")
print(f"El total de el sueldo de los empleados es de: {round(total_sueldos, 2)}\n")



print("\n----- TOTAL H. EXTRAS -----")
#calculo total horas extras
def extras(HED, HEN, HEF, operarios, subgerentes):

        #GERENTE
        total_gerente_HED = sueldo_x_hora_gerente * (hed * HED) 
        total_gerente_HEN = sueldo_x_hora_gerente * (hen * HEN)
        total_gerente_HEF = sueldo_x_hora_gerente * (hef * HEF)
        
        total_gerente = total_gerente_HED + total_gerente_HEN + total_gerente_HEF
        print(f"El total de las extras de el gerente es de: {round(total_gerente, 2)}")

        #SUBGERENTE
        total_subgerente_HED = sueldo_x_hora_subgerente * (hed * HED)
        total_subgerente_HEN = sueldo_x_hora_subgerente * (hen * HEN)
        total_subgerente_HEF = sueldo_x_hora_subgerente * (hef * HEF)
        
        total_subgerente = (total_subgerente_HED + total_subgerente_HEN + total_subgerente_HEF) * subgerentes
        print(f"El total de las extras de los subgerentes es de: {round(total_subgerente, 2)}")
        
        #SECRETARIA
        total_secretaria_HED = sueldo_x_hora_secretaria * (hed * HED)
        total_secretaria_HEN = sueldo_x_hora_secretaria * (hen * HEN)
        total_secretaria_HEF = sueldo_x_hora_secretaria * (hef * HEF)
        
        total_secretaria = total_secretaria_HED + total_secretaria_HEN + total_secretaria_HEF
        print(f"El total de las extras de la secretaria es de: {round(total_secretaria, 2)}")
        
        #OPERARIO
        total_operario_HED = sueldo_x_hora_operario * (hed * HED)
        total_operario_HEN = sueldo_x_hora_operario * (hen * HEN)
        total_operario_HEF = sueldo_x_hora_operario * (hef * HEF)
        
        total_operario = (total_operario_HED + total_operario_HEN + total_operario_HEF) * operarios
        print(f"El total de las extras de los operarios es de: {round(total_operario, 2)}\n")

        #TOTAL 
        return total_gerente + total_subgerente + total_secretaria + total_operario

total_extras = extras(5, 4, 3, 3, 2)
print(f"El total de las horas extras de los empleados es de: {round(total_extras, 2)}\n")



#BONIFICACION
print("\n----- TOTAL BONIFICACIONES -----")

def bonif(subgerentes, operarios):
    #GERENTE 
    bonif_gerente = sueldo_gerente * 0.03

    #SUBGERENTE 
    bonif_subgerente = (sueldo_subgerente * subgerentes) * 0.03
    
    #SECRETARIA
    bonif_secretaria = sueldo_secretaria * 0.05
    
    #OPERARIOS 
    bonif_operarios = (sueldo_operario * operarios) * 0.07
    
    #TOTAL BONIFICACIONES
    return bonif_gerente + bonif_subgerente + bonif_secretaria + bonif_operarios

total_bonificaciones = bonif(2, 3)
print(f"El total de las bonificaciones de los empleados es de: {total_bonificaciones}")



#INGRESOS 
total_ingresos = total_bonificaciones + total_extras + total_sueldos
print(f"EL total de los ingresos es de:  {total_ingresos}")

#PRESTACIONES
def prestaciones(subgerentes, operarios):
    #GERENTE 
    salud_gerente = sueldo_gerente * 0.05
    pension_gerente = sueldo_gerente * 0.03
    total_gerente = salud_gerente + pension_gerente
    
    #SUBGERENTE 
    salud_subgerente = (sueldo_subgerente * subgerentes) * 0.05
    pension_subgerente = (sueldo_subgerente * subgerentes) * 0.03
    total_subgerente = salud_subgerente + pension_subgerente
    
    #SECRETARIA 
    salud_secretaria = sueldo_secretaria * 0.05
    pension_secretaria = sueldo_secretaria * 0.03
    total_secretaria = salud_secretaria + pension_secretaria
    
    #OPERARIOS 
    salud_operario = (sueldo_operario * operarios) * 0.05
    pension_operario = (sueldo_operario * operarios) * 0.03
    total_operario = salud_operario + pension_operario
    
    #TOTAL PRESTACIONES 
    total_salud = salud_gerente + salud_operario + salud_subgerente + salud_secretaria
    total_pension = pension_gerente + pension_operario + pension_secretaria + pension_subgerente
    total = total_gerente + total_operario + total_secretaria + total_subgerente
    
    return [total_salud, total_pension, total]

totales = prestaciones(2, 3)

total_salud = totales[0]
total_pension = totales[1]
total_prestaciones = totales[2]

print(f"""El total de salud es: {total_salud}
El total de pension es: {total_pension}
El total de las prestaciones es de: {total_prestaciones}""")



#AHORRO 
total_ahorro = total_ingresos * 0.03
print(f"El total de los ahorros es de {total_ahorro}")



#EGRESOS
total_egresos = total_salud + total_pension + total_ahorro
print(f"Los egresos son de: {total_egresos}")



#DEVENGADO 
total_devengado = total_ingresos - total_egresos
print(f"El devengado es de: {total_devengado}")