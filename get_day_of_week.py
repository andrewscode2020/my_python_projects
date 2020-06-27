
'''OBTAIN THE DAY OF THE WEEK BY INPUTTING A DATE'''

'''=============================== DATOS ==================================='''

meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto',
         'Septiembre','Octubre','Noviembre','Diciembre']

diasxmes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

dias_semana = ['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']

dia = int(input('Ingrese día: '))
mes = int(input('Ingrese mes: '))
año = int(input('Ingrese año: '))

rango = abs(año-1917)
secuencia_dias = [0]*rango  
c = 0
a = 1917

if año > a:
    aux = 1
    for i in range(rango):    
    
        if a%4 != 0:
            c += aux
        elif a%100 != 0:
            c += aux*2
        elif a%400 != 0:
            c += aux
        else:
            c += aux*2
    
        if c >= 6:
            c -= 7
    
        secuencia_dias[i] = dias_semana[c]
        a += aux
else:
    aux = -1
    for i in range(rango):    
        a += aux
    
        if a%4 != 0:
            c += aux
        elif a%100 != 0:
            c += aux*2
        elif a%400 != 0:
            c += aux
        else:
            c += aux*2

        if c <= -7:
            c += 7
    
        secuencia_dias[i] = dias_semana[c]

if rango == 0:
    c = 0

'''=============== DETERMINANDO NRO DE DÍAS TRANSCURRIDOS =================='''
dias_acumulados = []
acumulado = 0
for i in diasxmes:
    acumulado += i
    dias_acumulados.append(acumulado)

if mes == 1:
    Nro_dia_año = dia
else:
    if año % 4 == 0:
        if mes > 2:
            Nro_dia_año = dia + dias_acumulados[mes-2] + 1
    else:
        Nro_dia_año = dia + dias_acumulados[mes-2]

'''=============== DETERMINANDO DÍA DE LA SEMANA INGRESADO ================='''
    
dia_1ero = dias_semana[c]

indice_dia_ref = dias_semana.index(dia_1ero)

indice_dia = indice_dia_ref + (Nro_dia_año-1)%7
if indice_dia > 6:
    indice_dia -= 7

dia_semana = dias_semana[indice_dia]

'''================== IMPRIMIENDO EL RESULTADO =============================='''

print(f'\n> La fecha ingresada fue: {dia} de {meses[mes-1]} de {año}')
print(f'\n> Ese día fue {dia_semana}')
print(f'\n> Día número {Nro_dia_año} del año {año}')
print(f' ({(Nro_dia_año-1)//7} semanas y {(Nro_dia_año-1)%7} días transcurridos)')