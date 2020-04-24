#ENTRADA Y SALIDA ARRAYS

import numpy as np #Importamos la libreia numpy para arrays

array1 = np.arange(6)#Creamos nuestro primer arreglo
print(array1)

np.save('array1s',array1)#Guardamos el primer arreglo con el nombre de array1s
np.load('array1s.npy')#Lo volvemos a leer

array2 = np.arange(8)#creamos un segundo arreglo
print(array2)

np.savez('arrays', x = array1,y = array2)#Guardamos los 2 arreglos con x  and  y 
array_recuperado = np.load('arrays.npz')#Leemos nuestro nuevo array
print(array_recuperado)

copia = array_recuperado['x']#Obtenemos el arreglo numero 1
print(copia)

np.savetxt('mificheroarray.txt',array2,delimiter=',')#Guardamos el arreglo2 en un txt

print(array2)#Recuperamos el array2









