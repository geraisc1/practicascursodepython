#indexaxion con arrays

import numpy as np #Importamos la libreria para definir arrays con el alias de np

array = np.arange(0,11) #Definimos un array respecto a un rango de (0,11) "np.arange"
print(array)#imprimimos el array en pantalla

posicion = array[0:3] #Seleciona una posicion inicial y una final
print(posicion)#Imprime los valores de las posiciones definidas

posicion = array[2:5]#Seleciona una posicion inicial y una final
print(posicion)#Imprime los valores de las posiciones definidas

posicion = array[:]#Selcciona todos los valores del arreglo
print(array)#Imprime el array completo

array_copia = array.copy()#Hace una copia del arreglo original
print(array_copia)#Muestra la copia del arreglo original

array_copia[0:3] = 20 #selecciona posicion de 0 a 3 y les asigna un valor de 20
print(array_copia)#MUestra los nuevos valores de las tres primeras posiciones del array

array2 = np.array(([1,2,3],[4,5,6],[7,8,9]))#Creamos y arreglo matricial
print(array2)#imprimimos el arreglo en pantalla

fila1 = array2[1]#seleccionamos la segunda fila del array
print(fila1)#Mostramos la fila en pantalla

valor = array2[1][1]#Seleccionamos la segunda fila y el segundo dato(numero) del array
print(valor)#Imprimimos ese dato en pantalla











