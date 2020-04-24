#Indices

import pandas as pd 
'''

lista_valores = [1,2,3]  #creamos una lista ded valores
lista_indices = ['a','b','c'] #Creamos una lista de indices para los valores
serie = pd.Series(lista_valores, index = lista_indices) Convertimos las listas en series
print(serie) # imprimimos la serie

tupla = serie.index = ponemos la serie en una tupla o fila
print(tupla)

num = serie.index[0] #mostramos un indice de la serie 
print(num)
'''
# CREAMOS LISTAS DE ALUMNOS Y CALIFICACIONES
#INDICES

lista_valores = [[7,8,9],[7,5,9],[8,9,9]]
lista_indices = ['programacion','redes','ingles']
lista_nombres = ['pablo','pedro','andy']
 
 #HACEMOS UN DATAFRAME CON LAS LISTAS
dataframe = pd.DataFrame(lista_valores, index= lista_indices, columns = lista_nombres)
print(dataframe)
#IMPRIMIMOS EL DATA FRAME







