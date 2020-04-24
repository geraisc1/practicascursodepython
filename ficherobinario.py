#FICHEROS BINARIOS

import pickle #importamos la libreria pickle

list = ["Mango","Pera","Zandia","Naranja"] #contruimos nuestro diccionario de datos
fichero = open ("fichero_frutas.pckl","wb")#creamos un nuevo fichero con el metodo wb y pckl
pickle.dump(list,fichero)#con el metodo dump cargamos los datos al fichero(diccionario)
fichero.close() #cerramos el fichero




