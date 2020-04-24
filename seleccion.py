#SELECCIONAR DATOS DE UNA SERIE

#IMPORTAMOS LAS LIBRERIAS PARA SERIES Y PARA ARREGLOS

import pandas as pd
import numpy as np 

#CREAMOS LISTAS PARA NUESTRO PROGRAMA

lista_valores = np.arange(3)
lista_indices = ['i1','i2','i3']

#CONVERTIMOS LAS LISTAS A SERIES CON INDICES

serie = pd.Series(lista_valores, index = lista_indices)
#print(serie)

#MULTIPLICAMOS LAS LISTAS POR 2

serie = serie * 2
print(serie)

#HECEMOS SELECCION DE DATOS CON LOS SIGUIENTES METODOS

seleccion = serie['i2']
print(seleccion)
 
seleccion = serie[2]
print(seleccion)

seleccion = serie[0:2]
print(seleccion)

seleccion = serie[:]
print(seleccion)

#SELECCIONAMOS UN DATO RESPECTO A UNA CONDICION EN ESTE CASO QUE EL DATO SEA MAYOR A 3

seleccion = serie[serie > 3]
print(seleccion)

#ASIGNAMOS EL VALOR 6 AL DATO QUE SELECCIONAMOS

seleccion = serie[serie > 3] = 6
print(serie)



