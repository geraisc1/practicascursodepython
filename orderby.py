#ORDENAMOS DATOS DE LA DB

import sqlite3

conexion = sqlite3.connect("database1.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS ORDER BY edad ")

lista1 = cursor.fetchall()

for personas in lista1:
    print(personas)

conexion.close
