#ORDENAR Y CLASIFICAR

#IMPORTAMOS LIBRERIAS
import pandas as pd 
import numpy as np 

#CREAMOS LISTAS PARA CREAR UNA SERIE
lista_valores = range(4)
lista_indices = list('CDAB')

serie = pd.Series(lista_valores, index = lista_indices)
#print(serie)

#METODOS DE ORDENAMIENTO

#POR INDICE
ordenar = serie.sort_index()
print(ordenar)

#POR VALOR
ordenar = serie.sort_values()
print(ordenar)

#POR EL RANGO -VALOR MAS ALTO
ordenar = serie.rank()
print(ordenar)

#SERIE CON NUMEROS ALEATORIOS
serie1 = pd.Series(np.random.random(10))
print(serie1)

#ORDENAR POR RANGO - VALOR MAS ALTO
ordenar = serie1.rank()
print(ordenar)

#POR VALOR MIN-ALTO
ordenar = serie1.sort_values()
print(ordenar)

#POR INDICE
ordenar = serie1.sort_index()
print(ordenar)












