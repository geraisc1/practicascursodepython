#leer archivos binarios

import pickle #importamos la libreria pickle

fichero = open("fichero_frutas.pckl","rb") #creamos nuestro diccionario de datos
lista_leeer = pickle.load(fichero)#leemos el diccionario con el metodo load
print(lista_leeer)#imprimimos en pantalla al diccionario
