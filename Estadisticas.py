#Estadisticas con dataframes

#IMPORTAMOS LIBRERIAS
import pandas as pd
import numpy as np 

#CREAMOS UN DATA FRAME POR MEDIO DE UN ARRAY
array = np.array([[1,8,3],[5,6,7]])
dataframe = pd.DataFrame(array, index = ['a','b'], columns = list('123'))
print(dataframe)

#SUMAMOS EL DATA FRAME

suma = dataframe.sum()
print(suma)

#SUMAMOS LAS FILAS DEL DATAFRAME
suma = dataframe.sum(axis=1)
print(suma)

#CALCULAMOS LOS VALORES MINIMOS DEL DATAFRAME
minimo = dataframe.min()
print(minimo)

#CALCULAMOS LOS VALORES MAXIMOS DEL DATAFRAME
maximo = dataframe.max()
print(maximo)

#CALCULAMOS EL VALOR MAXIMO DE LA FILA
maximo = dataframe.max(axis=1)
print(maximo)

#CALCULAMOS EL VALOR MINIMO DEL INDICE
indice = dataframe.idxmin()
print(indice)

#DESCRIBIMOS EL CONTENIDO DEL DATAFRAME(ESTADISTICO)
describir = dataframe.describe()
print(describir)

