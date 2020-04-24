#Base de datos

import sqlite3 #importamos la libreria sqlite para trabajar con base de datos

conexion = sqlite3.connect("database1.db")#abrimos la conexion y creamos una base de datos

cursor = conexion.cursor()#herramienta para seleccionar la base de datos

cursor.execute("CREATE TABLE PERSONAS (nombre text, apellidos1 text, apellidos2 text, edad integer)")#cramos una tabla con los parametreos que tendra
conexion.commit()#commit para aceptar los cambios hechos

conexion.close()#cerramos la conexion





