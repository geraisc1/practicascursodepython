#Series

import pandas as pd #Importamos la libreria pandas para realizar las series

serie1 = pd.Series([3,5,7])#creamos nuestra primer serie (index)
#print (serie1)

numero = serie1[1]#Mostramos un numero de la serie
#print(numero)

asignaturas = ['matematicas','fisica','historia','informatica'] #Lista Asignaturas
calificaciones = [8,7,9,8]# Lista calificaciones

#COMBINAMOS LAS LISTAS A UNA SERIE CON UN INDEX(CALIFICACIONES)

serie_gera = pd.Series(calificaciones,index = asignaturas)


#print(serie_gera)

Titulo = serie_gera.index.name = 'Aignaturas Gera'#Agregamos un titulo a la serie
#print(Titulo)


#materia = serie_gera['informatica']
#print(materia)

calf = serie_gera[serie_gera >=8]#seleccionamos calificaciones > a 8
print(calf)#imprimimos


nombre = serie_gera.name = 'Notas Gera'#Pie de pagina de la serie
print(nombre)

dicionario = serie_gera.to_dict()#Convertimos la serie a un diccionario
#print(dicionario)

#serie = pd.Series(dicionario) # convertimos el diccionario a una serie
#print(serie)

asignaturas = ['matematicas','fisica','historia','informatica']
calificaciones = [9,9,8,5]
serie_andy = pd.Series(calificaciones,index = asignaturas)#Creamos otra serie

Titulo = serie_andy.index.name = '\nAignaturas Andy'#Agregamos un titulo a la serie
print(Titulo)

asignaturas = ['matematicas','fisica','historia','informatica']
calificaciones = [9,9,8,5]
serie_andy = pd.Series(calificaciones,index = asignaturas)
print(serie_andy)

nombre = serie_andy.name = 'Notas Andy'#Pie de pagina de la serie
print(nombre)

#Operaciones

serie_calificaciones_media = (serie_gera + serie_andy) /2 #Sumamos y dividimos la serie

Titulo = serie_calificaciones_media.index.name = '\nMedia de los dos alumnos'#Agregamos un titulo
print(Titulo)

serie_calificaciones_media = (serie_gera + serie_andy) /2
print(serie_calificaciones_media)

#Fin

















