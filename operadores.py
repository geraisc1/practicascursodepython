#Operaciones con arrays (+,-,*,/,**)

import numpy as np #importamos la libreria para crear arrays

array1 = np.array([1,2,3,4])#Creamos nuestro primer arreglo

suma = array1 + 3 #Le sumamos a nuestro arreglo un valor de 3
print(suma) # Imprimimos el resultado en pantalla

print(array1) #El array sigue teniendo el mismo valor del primer arreglo

array1 = array1 + 3 # Asignamos un el valor de la suma a primer array
print(array1) #Ahora el primer array ya cambio su valor

lista1 = [1,2,3,4]#Creamos dos listas para hacer operaciones
lista2 = [5,6,7,8]
lista_doble = (lista1,lista2)#Fusionamos las dos listas que definimos arriba en una sola
print(lista_doble) # Imprimimos en pantalla

array_doble = np.array(lista_doble) #CAONVERTIMOS NUESTRA LISTA_DOBLE EN UN ARRAY
print(array_doble)#LO LLAMAMOS ARRAY DOBLE Y LO MOSTRAMOS EN PANTALLA

forma = array_doble.shape#Observamos las filas y columnas del array
print(forma)#Imprimimos la forma

tipo = array_doble.dtype#Observamos el tipo de dato de el array_doble
print(tipo)#Imprimimos el tipo de dato

#REALIZAMOS UNA OPERACION * MULTIPLICAMOS EL ARRAY POR 2

multiplicacion = array_doble * 2  # FAUNCION QUE REALIZA LA MULTIPLICACION
print(multiplicacion)#Imprimimos el resultado





