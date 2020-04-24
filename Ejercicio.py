#Ejercicio

#IMPORTAMOS LIBRERIAS
import pandas as pd 
import numpy as np 

#CREAMOS VARIABLES NECESARIAS
minimo = 10
maximo = 40
numero = 3

#CREAMOS UNA LISTA DE ALUMNOS EN EL *RANDOM
alumnos = np.random.randint(minimo,maximo,numero)

#CREAMOS TRES CLASES
classes = ['clase1','clase2','clase3']
#CREAMOS UNA SERIES
serie = pd.Series(alumnos, index = classes)
print(serie)

#ELEGIMOS LA CATIDAD DE ALUMNOS DE LA CLASE DOS
elegir = serie['clase2']
print(elegir)



