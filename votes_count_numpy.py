'''
 
 Se tiene una matriz de 8 filas y 5 columnas,
 donde las filas son los departamentos de Colombia
 y las columnas son los partidos políticos.
 En la matriz se almacenan los resultados de las
 últimas elecciones presidenciales.
 
  Hacer un programa que muestre:
 
 1.- Promedio de votos por departamento.
 2.- Promedio de votos por partido.
 3.- Donde se presentó la mayor votación.
 4.- Cual es el partido ganador.
'''

import numpy as np

def promedioDpto(Matriz):   
    PromDpto = [0]*5
    cont = 0
    for i in Matriz:
        PromDpto[cont] = int(np.mean(i)) 
        cont += 1    
    return PromDpto

def promedioPart(Matriz):
    Matriz_2 = Matriz.transpose()
    PromPart = [0]*3
    cont = 0
    for i in Matriz_2:
        PromPart[cont] = int(np.mean(i))
        cont += 1
    return PromPart

def mayorVotacion(PD, Matriz):
    Indice_Dpto = np.argmax(PD)
    VotosDpto = [0]*5
    cont = 0
    for i in Matriz:
        VotosDpto[cont] = np.sum(i)
        cont += 1
    MayorVotosDpto = VotosDpto[Indice_Dpto]
    return Indice_Dpto, MayorVotosDpto
    
def Partganador(P, Matriz):
    Indice_Partido = np.argmax(P)
    Matriz_2 = Matriz.transpose()
    VotosPartido = [0]*3
    cont = 0
    for i in Matriz_2:
        VotosPartido[cont] = np.sum(i)
        cont += 1
    MayorVotosPart = VotosPartido[Indice_Partido]
    return Indice_Partido, MayorVotosPart

#==============================================================================
# PROGRAMA PRINCIPAL
    
''' NOTA: Aquí genero la matriz automáticamente para saltar el proceso de tener 
que ingresar los datos manualmente'''
A = random_matrix = np.random.randint(100000,900000,(5,3))

# En este bloque de código agrego la columna de departamentos
# y la fila de partidos para mostrar la matriz de una manera
# ordenada

A1 = np.append([['Part_1','Part_2','Part_3']], A, axis = 0)

A2 = np.append([['Dpto/Partido'],['Antioquia    '],['Atlántico    '],
                ['Caldas       '],['Santander    '],['Cundinamarca ']], A1, axis = 1)            

print('\n> La matriz de resultados electorales por departamento y partido es:\n\n', A2)

# Promedio de votos por departamento===========================================

PD0 = np.array(promedioDpto(A))
PD1 = PD0.reshape(5,1)
PD2 = np.append([['Prm_V ']], PD1, axis = 0)

PD = np.append([['Dpto/Prom_Votos'],['Antioquia       '],['Atlántico       '],
                ['Caldas          '],['Santander       '],['Cundinamarca    ']], PD2, axis = 1) 

print('\n> El promedio de votos por departamento fue:\n\n', PD)

# Promedio de votos por partido================================================

P0 = np.array(promedioPart(A))
P1 = P0.reshape(1,3)
P2 = np.append([['  Promedio_Votos   ']], P1, axis = 1)

P = np.append([['Prom_Votos/Partido','Part_1','Part_2','Part_3']], P2, axis = 0)

print('\n> El promedio de votos por partido fue:\n\n', P)

## Departamento con mayor votación=============================================

(Indice_Dpto, MayorVotosDpto) = mayorVotacion(PD0, A)
Dptos = [['Antioquia'],['Atlántico'],['Caldas'],['Santander'],['Cundinamarca']]
print('\n> El departamento con mayor votación fue', str(Dptos[Indice_Dpto]).strip('[]'), 
      'con un total de', MayorVotosDpto, 'votos')

# Partido ganador==============================================================

(Indice_Partido, MayorVotosPartido) = Partganador(P0, A)
Partidos = [['Part_1'],['Part_2'],['Part_3']]
print('\n> El partido con mayor votación fue', str(Partidos[Indice_Partido]).strip('[]'),
      'con un total de', MayorVotosPartido, 'votos')

#==============================================================================