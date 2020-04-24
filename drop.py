#Eliminar series

#IMPORTAMOS DOS LIBRERIAS PARA REALIZAR EL CODIGO

import pandas as pd 
import numpy as np 

#CREAMOS UN ARREGLO CON ARANGE

arreglo = np.arange(4) 
print(arreglo)

#CONVERTIMOS EL ARREGLO A UNA SERIE CON INDICES

serie = pd.Series(np.arange(4), index = ['a','b','c','d'])
print(serie)

#BORRAMOS UN INDICE DE LA SERIE 'C'

borrar = serie.drop('c')
print(borrar)

#CREAMOS UNA MATRIZ POR MEDIO DE UN ARRAY = NP.ARANGE(9)

matriz = np.arange(9).reshape(3,3)
print(matriz)

lista_valores = np.arange(9).reshape(3,3)

#DEFINIMOS LISTAS PARA CREAR UN DATAFRAME

lista_indices = ['a','b','c']
lista_columnas = ['c1','c2','c3']

#CREAMOS LA ESTRUCTURA DE COMO QUEDARA EL DATA FRAME
dataframe = pd.DataFrame(lista_valores, index = lista_indices, columns = lista_columnas)
print(dataframe)

#BORRAMOS UN DATO DEL DATAFRAME = 'B'

borrar = dataframe.drop('b')
print(borrar)

#BORRAMOS UNA COLUMNA DEL DATAFRAME

borrar = dataframe.drop('c3', axis = 1)
print(borrar)












