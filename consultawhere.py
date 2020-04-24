#CONSULTAR DATOS CON WHERE

import sqlite3 #importamos la libreria para poder utilizar sql

conexion = sqlite3.connect("database1.db")#creamos una base de datos o ponemos el nombre de una existente
cursor = conexion.cursor()#Con este metodo ejecutamos sentencias sql

cursor.execute("SELECT * FROM PERSONAS WHERE edad = 20 ")#Definimos la accion a realizar coon execute

edad = cursor.fetchall() #creamos una vaiable de lo queremos obtener y recogemos datos con fenchall

for edad in edad: #utilizamos un ciclo for para recorrer los datos que temos en la base de datos
    print(edad)#imprimimos la varible o el dato de lo que deseamos buscar

conexion.close() #cerramos la conexion


