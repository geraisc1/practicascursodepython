#SELECIONAR DATOS DE ENTRADA DE UN DATAFRAME

#IMPORTAMOS LIBRERIAS
import pandas as pd 
import numpy as np 

#CREAMOS NUESTRAS LISTAS PARA EL DATAFRAME
lista_valores = np.arange(25).reshape(5,5)
lista_indices = ['i1','i2','i3','i4','i5']
lista_columnas =['c1','c2','c3','c4','c5']

#CREAMOS EL CODIGO PARA GENRERAR EL DATAFRAME

dataframe = pd.DataFrame(lista_valores, index = lista_indices, columns = lista_columnas)
print(dataframe) #IMPRIMIMOS EN PANTALLA

#SELECCIONA DATOS DE LA COLUMNA1 AL INDICE2

seleccionar = dataframe['c2']['i2']
print(seleccionar)

#SELCCION DE COLUMNA 2 Y COLIMNA 4

seleccionar = dataframe[['c2','c4']]
print(seleccionar)

seleccionar = dataframe[dataframe['c2'] > 15]
print(seleccionar)









