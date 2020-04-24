#Funciones con arrays

import numpy as np 

array = np.arange(5)#Creamos nuetro primer array
print(array)

raiz = np.sqrt(array)#Calculamos la raiz de nuestro arreglo
print(raiz)

aleatorios = np.random.random(5)#Creamos numeros aleatorios random . random (5) valores
print(aleatorios)


lista = [5,6,7,8,9]#Creamos una lista de datos
array2 = np.array(lista)#Convertimos la lista a un arreglo
print(array2)

suma = np.add(array,array2)#Sumamos los dos arreglos (array + array2)

print(suma)









