#CONSULTAR TABLA

import sqlite3

conexion = sqlite3.connect("database1.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS")#Accion para consulrar la base de datos

personas = cursor.fetchall()

for personas in personas:
    print(personas)

conexion.close()




