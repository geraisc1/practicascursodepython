#BORRAR DATOS DE UNA DB

import sqlite3

conexion = sqlite3.connect("database1.db")
cursor = conexion.cursor()

cursor.execute("DELETE FROM PERSONAS WHERE edad = 20")

edad = cursor.fetchall()

conexion.commit()
conexion.close()

