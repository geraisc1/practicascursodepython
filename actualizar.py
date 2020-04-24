#Actualizar datos de la base de datos

import sqlite3

conexion = sqlite3.connect("database1.db")

cursor = conexion.cursor()

cursor.execute("UPDATE PERSONAS SET nombre = 'Andy' WHERE  nombre = 'Enrrique'")

nombre = cursor.fetchall()

conexion.commit()
conexion.close()


