#DATA FRAME

import pandas as pd 

import webbrowser

#website = 'https://capplatam.com/articulos-guias/autos-aceptados-para-uber/' #Abrimos una pagina de internet
#webbrowser.open(website)#Abrimos la pagina

#dataframe_uber = pd.read_clipboard()# Accion para pegar lo que tenemos en control ^C
#print(dataframe_uber) #imprimimos en pantalla

lista_asignaturas = ['matematicas','programacion','base de datos']#Creamos una lista de asignaturas
lista_notaa = [8,9,7]#Creamos una lista de calificaciones
diccionario = {'Materias':lista_asignaturas,'Notas':lista_notaa} #Agregamos un diccionario para concatenar lista de materias y lista de las notas
print(diccionario)

dataframe_notas = pd.DataFrame(diccionario)#Convertimos el diccionario a un dataframe
print(dataframe_notas)#Imprimimos en pantalla






