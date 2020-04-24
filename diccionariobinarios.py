#Ejercicio de leer diccionarios_binarios

import pickle #importamos la libreria pickle

#CREAMOS  NUESTRO DICCIONRIO DE DATOS
diccionario = {"manzana":"aple","naranja":"orange","platano":"banana","limon":"lemon"}

fichero = open("fichero.pckl","wb")#creamos nuestro archivo.pckl con wb
pickle.dump(diccionario,fichero)#carga los datos al fichero o archivo
fichero.close()

fichero = open("fichero.pckl","rb")
lista_leer = pickle.load(fichero)#leemos los datos de el fichero.pckl
print(lista_leer)#imprimimos los datos en pantalla



