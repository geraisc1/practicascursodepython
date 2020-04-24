#OPERACIONES CON FRAMES

import pandas as pd 
import numpy as np 

serie = pd.Series([0,1,2],index = ['a','b','c'])
serie2 = pd.Series([3,4,5,6],index = ['a','b','c','d'])

suma = serie + serie2
print(suma)

#CREAMOS LOS VALORES PARA EL DATAFRAME

lista_valores = np.arange(4).reshape(2,2)


lista_indices = list('ab')
lista_columnas = list('12')

dataframe = pd.DataFrame(lista_valores, index = lista_indices, columns = lista_columnas)
print(dataframe)


#segundo dataframe

lista_valores = np.arange(4).reshape(2,2)

lista_indices = list('ab')
lista_columnas = list('12')

dataframe1 = pd.DataFrame(lista_valores, index = lista_indices, columns = lista_columnas)
print(dataframe1)

#HACEMOS UNA SUMA DE DATAFRAMES = DATAFRAME3

suma = dataframe + dataframe1
print(suma)



