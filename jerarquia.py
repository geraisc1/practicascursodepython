#JERARQUIA DE INDICES 

#IMPORTAMOS LIBRERIAS
import pandas as pd 
import numpy as np 

#CREAMOS LISTAS PARA SERIE
lista_valores = np.random.random(6)
lista_indices = [ [1,1,1,2,2,2], ['a','b','c','a','b','c'] ]
serie = pd.Series(lista_valores, index = lista_indices)
print(serie)

#ELEGIMOS LA PRIMERA POSICION
uno = serie[1]
print(uno)

#ELEGIMOS POCICIONES
pocicion = serie[1]['b']
print(pocicion)

#CONVERTIMOS LA SERIE EN UN DATAFRAME
dataframe = serie.unstack()
print(dataframe)
#CREAMOS LISTAS PARA UN SEGUNDO DATAFRAME
lista_valores = np.arange(16).reshape(4,4)
lista_indices = list('1234')
lista_columnas = list('abcd')

dataframe2 = pd.DataFrame(lista_valores, index = lista_indices, columns = lista_columnas)
print(dataframe2)
#PONEMOS EL DATAFRAME EN FILAS
serie2 =  dataframe2.stack()
print(serie2)







