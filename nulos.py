#VALORES NULOS

#IMPORTAMOS LIBRERIAS
import pandas as pd 
import numpy as np 

#CREAMOS UNA SERIE CON VALORES NULOS
lista_valores = ['1','2',np.nan,'4']
serie = pd.Series(lista_valores, index = list('abcd'))
print(serie)

#CONSULTAMOS LOS DATOS NULOS (TRUE-FALSE)
nulo = serie.isnull()
print(nulo)

#BORRAMOS A EL INDEX A
borrar = serie.dropna()
print(borrar)

#ASIGNAMOS EL VALOR DEL BORRADO A LA SERIE ORIGINAL
serie = serie.dropna()
print(serie)

#CREAMOS LISTAS PARA LOS DATAFRAMES
lista_valores =[[1,2,3],[4,np.nan,5],[6,7,np.nan]]
lista_indices = list('123')
lista_columnas = list('abc')

#CREAMOS EL DATAFRAME
dataframe = pd.DataFrame(lista_valores, index = lista_indices, columns = lista_columnas)
print(dataframe)

#VERIFICAMOS LOS VALORES NULOS (TRUE-FALSE)
nulo = dataframe.isnull()
print(nulo)

#BORRAR LETRA A DE EL DATAFRAME
borrar = dataframe.dropna()
print(borrar)

#PONEMOS CEROS EN LOS LUGARES DE LOS DATOS NULOS
fila = dataframe.fillna(0)
print(fila)






