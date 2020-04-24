
import numpy as np #importamos la libreria para crear arreglos con un alias llamado np

hola = np.ones(4) # Define un arreglo de 4 datos con valor = 1

print (hola)

arreglo = np.zeros(8)#Define un arreglo de 8 datos con valor = 0
print (arreglo)

arreglo = np.arange(6)#Define un rango de numeros del 0 al 6
print(arreglo)

arreglo = np.arange(2,20,3)
print (arreglo)

lista1 = [1,2,3,4]

arreglo1 = np.array(lista1)#Convierte una lista a un arreglo
print(arreglo1)

lista1 = [1,2,3,4]#Definimos 2 listas
lista2 = [5,6,7,8]

lista_doble = (lista1,lista2)#Unimos la dos listas en una sola
print(lista_doble)#La imprimimos en pantalla

array_doble = np.array(lista_doble)#Convertimos la union de las dos listas en un array
print(array_doble)#Imprimimos el array en pantalla

forma = array_doble.shape#.shape verificamos la estructura del array(filas,columnas)
print(forma)

tipo = array_doble.dtype#.dtype = Observamos el tipo de dato
print(tipo)












