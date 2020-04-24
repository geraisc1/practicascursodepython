#CREACION DE MATRICES TRASPUESTAS 

import numpy as np 

array = np.arange(15).reshape((3,5))#CREAMOS UNA MATRIZ DE 3 FILAS Y 5 COLUMNAS
print(array)#Imprimimos la matriz en pantalla

valor = array[1][1]#Seleccionamos la segunda fila y el segundo dato(numero) del array
print(valor)#Imprimimos ese dato en pantalla

array_tras = array.T#Cabiamos la posicion de las filas y las columnas ahora sera 5 filas y 3 columnas
print(array_tras)#Mostramos la nueva matriz en pantalla

